from PySide6.QtCore import Qt,QRectF
from PySide6.QtGui import QColor, QPixmap, QBrush
from PySide6.QtWidgets import QGraphicsView, QGraphicsItem, QGraphicsRectItem, QGraphicsPixmapItem, QGraphicsScene

class ResizableRect(QGraphicsRectItem):
    def __init__(self, *args):
        super().__init__(*args)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setCursor(Qt.SizeAllCursor)
        self.setBrush(QBrush(QColor('red')))
        self.setOpacity(0.2)
        self.selected_edge = None
        self.click_pos = self.click_rect = None

    def mousePressEvent(self, event):
        """ The mouse is pressed, start tracking movement. """
        self.click_pos = event.pos()
        rect = self.rect()
        if abs(rect.left() - self.click_pos.x()) < 20:
            self.selected_edge = 'left'
        elif abs(rect.right() - self.click_pos.x()) < 20:
            self.selected_edge = 'right'
        elif abs(rect.top() - self.click_pos.y()) < 20:
            self.selected_edge = 'top'
        elif abs(rect.bottom() - self.click_pos.y()) < 20:
            self.selected_edge = 'bottom'
        else:
            self.selected_edge = None
        self.click_pos = event.pos()
        self.click_rect = rect
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """ Continue tracking movement while the mouse is pressed. """
        # Calculate how much the mouse has moved since the click.
        pos = event.pos()
        x_diff = pos.x() - self.click_pos.x()
        y_diff = pos.y() - self.click_pos.y()

        # Start with the rectangle as it was when clicked.
        rect = QRectF(self.click_rect)

        # Then adjust by the distance the mouse moved.
        if self.selected_edge is None:
            rect.translate(x_diff, y_diff)
        elif self.selected_edge == 'top':
            rect.adjust(0, y_diff, 0, 0)
        elif self.selected_edge == 'left':
            rect.adjust(x_diff, 0, 0, 0)
        elif self.selected_edge == 'bottom':
            rect.adjust(0, 0, 0, y_diff)
        elif self.selected_edge == 'right':
            rect.adjust(0, 0, x_diff, 0)

        # Figure out the limits of movement.
        scene_rect = self.scene().sceneRect()
        view_left = scene_rect.left()
        view_top = scene_rect.top()
        view_right = scene_rect.right()
        view_bottom = scene_rect.bottom()

        # Next, check if the rectangle has been dragged out of bounds.
        if rect.top() < view_top:
            if self.selected_edge is None:
                rect.translate(0, view_top-rect.top())
            else:
                rect.setTop(view_top)
        if rect.left() < view_left:
            if self.selected_edge is None:
                rect.translate(view_left-rect.left(), 0)
            else:
                rect.setLeft(view_left)
        if view_bottom < rect.bottom():
            if self.selected_edge is None:
                rect.translate(0, view_bottom - rect.bottom())
            else:
                rect.setBottom(view_bottom)
        if view_right < rect.right():
            if self.selected_edge is None:
                rect.translate(view_right - rect.right(), 0)
            else:
                rect.setRight(view_right)

        # Also check if the rectangle has been dragged inside out.
        if rect.width() < 20:
            if self.selected_edge == 'left':
                rect.setLeft(rect.right() - 20)
            else:
                rect.setRight(rect.left() + 20)
        if rect.height() < 20:
            if self.selected_edge == 'top':
                rect.setTop(rect.bottom() - 20)
            else:
                rect.setBottom(rect.top() + 20)

        # Finally, update the rect that is now guaranteed to stay in bounds.
        self.setRect(rect)


class PDFViewer(QGraphicsView):
    def __init__(self, parent=None):
        super(PDFViewer, self).__init__(parent)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)

        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.selectionRects = []

        self.setStyleSheet('border: 2px solid white;')
        
    def setPixmap(self, pixmap):
        self.scene.clear()
        self.scene_img = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.scene_img)
        self.scene_img.setScale(1.0)
        self.fitInView(self.scene_img)
        
    def setRubberband(self):
        self.selectionRect = ResizableRect()
        self.selectionRects.append(self.selectionRect)
        center = self.mapToScene(self.viewport().rect().center())
        x = center.x() - 25
        y = center.y() - 25
        self.selectionRect.setRect(x, y, 1500, 1500)
        self.selectionRect.setParentItem(self.scene_img)

    def deleteRubberband(self):
        self.scene.removeItem(self.selectionRects.pop())

    def getRectCoords(self):
        imageSize = self.scene_img.pixmap().size()
        rect = self.scene_img.mapRectToParent(self.selectionRect.rect())
        
        coords = rect.getCoords()
        coordsRelative = [coords[0]/imageSize.width(), coords[1]/imageSize.height(), coords[2]/imageSize.width(), coords[3]/imageSize.height()]

        return coordsRelative
        

