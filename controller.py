from PySide6.QtWidgets import QApplication, QListWidgetItem, QDialog, QGraphicsDropShadowEffect, QMainWindow, QFileDialog, QLabel
from PySide6.QtGui import QCloseEvent, QIcon, QColor, QAction, QPixmap, QGuiApplication, QPainter, QPen, QImage
from PySide6.QtCore import Qt, QRect, QPoint, Signal, QSize
import os
import sys
import fitz
import json

from UI.ATOM import Ui_ATOM
from UI.selectionDialog import Ui_selectionDialog
from pdfViewer import PDFViewer


class SelectionDialog(Ui_selectionDialog, QDialog):
    cancelSelection = Signal()
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.selectionBox.addItems(sorted(['File', 'Drawing', 'Sheet', 'Area', 'P&ID', 'Project No', 'POS', 'IDENT', 'NPS/DN', 'Description', 'QTY', 'BOM']))
        self.cancelButton.clicked.connect(lambda: self.close())


class AtomApp(Ui_ATOM, QMainWindow):
    def __init__(self):
        super(AtomApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('ATOM')
        self.setWindowIcon(QIcon('UI/resources/blueprint.png'))

        self.exitButton.clicked.connect(self.exit)
        self.clearAllButton.clicked.connect(lambda: self.selectionsList.clear())

    def setShadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.exitButton.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.pickFileButton.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.sideWidget.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.fileDisplayWidget.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.extractButton.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.clearAllButton.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.previousButton.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.nextButton.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.applySelection.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(4)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.makeSelection.setGraphicsEffect(shadow)

    def startApp(self):
        self.setShadow()
        pos = QGuiApplication.primaryScreen().availableGeometry().center()
        self.move(pos.x() - self.rect().center().x(), pos.y() - self.rect().center().y())

        self.show()
        self.showMaximized()
            
    def exit(self):
        self.close()


class Controller:
    def __init__(self) -> None:
        
        if getattr(sys, 'frozen', False):
            self.current_dir = os.path.dirname(sys.executable)
        elif __file__:
            self.current_dir = os.path.dirname(os.path.realpath(__file__))
        
        os.chdir(self.current_dir)

        if os.path.exists('Coordinates'):
            pass
        else:
            os.mkdir('Coordinates')

        #necessary variables
        self.jsonData = {}

        #init UI elements
        self.mainApplication = AtomApp()
        self.selectionDialog = SelectionDialog(self.mainApplication)
        self.PDFViewer = PDFViewer(self.mainApplication.fileDisplayWidget)
        self.mainApplication.horizontalLayout_3.addWidget(self.PDFViewer)
        self.mainApplication.nextButton.setEnabled(False)
        self.mainApplication.previousButton.setEnabled(False)

        #init config, signals and slots
        self.mainApplication.pageLabel.clear()
        self.mainApplication.applySelection.hide()
        self.mainApplication.makeSelection.setEnabled(False)
        self.mainApplication.pickFileButton.clicked.connect(self.openFile)
        self.mainApplication.makeSelection.clicked.connect(self.startSelection)
        self.mainApplication.applySelection.clicked.connect(self.applySelection)
        self.selectionDialog.cancelButton.clicked.connect(self.closeSelectionDialog)
        self.selectionDialog.saveButton.clicked.connect(self.saveSelection)
        self.mainApplication.nextButton.clicked.connect(self.moveToNextPage)
        self.mainApplication.previousButton.clicked.connect(self.moveToPreviousPage)

        #start application
        self.mainApplication.startApp()

    def openFile(self):
        options = QFileDialog.Options()
        filepath, _ = QFileDialog.getOpenFileName(self.mainApplication, "Open PDF File", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        if filepath:
            self.loaded_pdf_path = filepath
            self.doc = fitz.open(filepath)
            self.currentpage = 0
            page = self.doc.load_page(0)
            dpi = 1000
            zoom = dpi / 72  # Default DPI in PyMuPDF is 72
            mat = fitz.Matrix(zoom, zoom)

            pix = page.get_pixmap(matrix=mat) #dpi=1200
            qt_img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_img)
            self.PDFViewer.setPixmap(pixmap)
            self.mainApplication.makeSelection.setEnabled(True)
            self.num_pages = self.doc.page_count
            self.mainApplication.pageLabel.setText(f'Page {self.currentpage + 1}/{self.num_pages}')
            self.doc.close()


            self.coordinatesFile = f"Coordinates/{filepath.split('/')[-1].split('.')[0]}.json"
            if os.path.exists(self.coordinatesFile):
                with open(self.coordinatesFile, 'r') as f:
                    self.jsonData = json.load(f)
            else:
                self.jsonData = {f'Page {self.currentpage}': {}}
                with open(self.coordinatesFile, 'w') as f:
                    json.dump(obj=self.jsonData, fp=f, indent=4)

            self.mainApplication.nextButton.setEnabled(True)
            self.mainApplication.previousButton.setEnabled(True)

    def moveToNextPage(self):
        self.currentpage += 1
        self.doc = fitz.open(self.loaded_pdf_path)
        page =self.doc.load_page(self.currentpage)
        dpi = 1000
        zoom = dpi / 72 
        mat = fitz.Matrix(zoom, zoom)

        pix = page.get_pixmap(matrix=mat)
        qt_img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_img)
        self.PDFViewer.setPixmap(pixmap)
        self.doc.close()

    def moveToPreviousPage(self):
        self.currentpage -= 1
        self.doc = fitz.open(self.loaded_pdf_path)
        page =self.doc.load_page(self.currentpage)
        dpi = 1000
        zoom = dpi / 72 
        mat = fitz.Matrix(zoom, zoom)

        pix = page.get_pixmap(matrix=mat)
        qt_img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_img)
        self.PDFViewer.setPixmap(pixmap)
        self.doc.close()

    def startSelection(self):
        self.mainApplication.applySelection.show()
        self.mainApplication.makeSelection.hide()
        self.PDFViewer.setRubberband()
        self.mainApplication.nextButton.setEnabled(False)
        self.mainApplication.previousButton.setEnabled(False)

    def applySelection(self):
        self.mainApplication.applySelection.hide()
        self.mainApplication.makeSelection.show()
        self.showSelectionDialog()
        self.mainApplication.nextButton.setEnabled(True)
        self.mainApplication.previousButton.setEnabled(True)
    
    def showSelectionDialog(self):
        pos = QPoint(self.mainApplication.pos().x() + self.mainApplication.rect().center().x() - self.selectionDialog.rect().center().x(), 
               self.mainApplication.pos().y() + self.mainApplication.rect().center().y() - self.selectionDialog.rect().center().y())
        self.selectionDialog.move(pos)
        self.selectionDialog.open()

    def saveSelection(self):
        selectionType = self.selectionDialog.selectionBox.currentText()
        item = QListWidgetItem(selectionType)
        self.mainApplication.selectionsList.addItem(item)
        self.selectionDialog.close()
        coords = list(self.PDFViewer.getRectCoords())

        try:
            currentNumberOfSelections = len(self.jsonData[f'Page {self.currentpage}'].keys())
            self.jsonData[f'Page {self.currentpage}'].update({f'Coordinate {currentNumberOfSelections}': {selectionType: coords}})
        except KeyError:
            currentNumberOfSelections = 0
            self.jsonData[f'Page {self.currentpage}'] = {f'Coordinate {currentNumberOfSelections}': {selectionType: coords}}
    
        with open(self.coordinatesFile, 'w') as f:
            json.dump(obj=self.jsonData, fp=f, indent=4)

    def closeSelectionDialog(self):
        self.mainApplication.applySelection.hide()
        self.mainApplication.makeSelection.show()
        self.PDFViewer.deleteRubberband()
        self.selectionDialog.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cont = Controller()
    sys.exit(app.exec())