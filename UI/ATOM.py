# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ATOM.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_ATOM(object):
    def setupUi(self, ATOM):
        if not ATOM.objectName():
            ATOM.setObjectName(u"ATOM")
        ATOM.resize(1280, 720)
        ATOM.setMinimumSize(QSize(1280, 720))
        self.centralwidget = QWidget(ATOM)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background:rgba(30, 33, 36, 255);\n"
"border: 0px;\n"
"border-radius: 0px;\n"
"}\n"
"QWidget{\n"
"background: rgba(51, 57, 73, 255);\n"
"border-radius: 10px;\n"
"font-family: Poppins;\n"
"font-size: 16px;\n"
"font-weight: 400;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QToolButton{\n"
"border: 0px;\n"
"background: rgba(0, 128, 255, 255);\n"
"color: rgba(255, 255, 255, 255);\n"
"font-weight: 400;\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 2px solid transparent;\n"
"}\n"
"QToolButton#extractButton{\n"
"background: transparent;\n"
"padding-left:20px;\n"
"}\n"
"QToolButton#exitButton{\n"
"padding-left:35px;\n"
"}\n"
"QToolButton#pickFileButton{\n"
"padding-left:10px;\n"
"}\n"
"QPushButton{\n"
"border: 0px;\n"
"background: rgba(0, 128, 255, 255);\n"
"color: rgba(255, 255, 255, 255);\n"
"font-weight: 400;\n"
"border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"border: 2px solid transparent;\n"
"}\n"
"QPushButton#nextButton, #previousButton, #clearAllButton{\n"
""
                        "background: transparent;\n"
"}\n"
"QPushButton#cancelSelection{\n"
"background: rgba(255, 255, 255, 255);\n"
"color: rgba(0, 128, 255, 255);\n"
"}\n"
"QLabel#titleLabel,#pageLabel{\n"
"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"}\n"
"QListWidget::item{\n"
"height: 30px;\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"}\n"
"QListWidget::item:selected{\n"
"background: rgba(0, 128, 255, 64);\n"
"}\n"
"QListWidget{\n"
"padding: 20 5 10 5;\n"
"}s")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.previousButton = QPushButton(self.centralwidget)
        self.previousButton.setObjectName(u"previousButton")
        self.previousButton.setMinimumSize(QSize(50, 50))
        self.previousButton.setMaximumSize(QSize(50, 16777215))
        icon = QIcon()
        icon.addFile(u"UI/resources/left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previousButton.setIcon(icon)
        self.previousButton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.previousButton, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 5, 80, 5)
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMinimumSize(QSize(0, 25))
        self.titleLabel.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.titleLabel)

        self.exitButton = QToolButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setMinimumSize(QSize(120, 25))
        self.exitButton.setMaximumSize(QSize(100, 25))
        icon1 = QIcon()
        icon1.addFile(u"UI/resources/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitButton.setIcon(icon1)
        self.exitButton.setIconSize(QSize(16, 16))
        self.exitButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout.addWidget(self.exitButton)

        self.pickFileButton = QToolButton(self.centralwidget)
        self.pickFileButton.setObjectName(u"pickFileButton")
        self.pickFileButton.setMinimumSize(QSize(120, 25))
        self.pickFileButton.setMaximumSize(QSize(100, 25))
        icon2 = QIcon()
        icon2.addFile(u"UI/resources/open-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pickFileButton.setIcon(icon2)
        self.pickFileButton.setIconSize(QSize(16, 16))
        self.pickFileButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout.addWidget(self.pickFileButton)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 7)

        self.nextButton = QPushButton(self.centralwidget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setMinimumSize(QSize(50, 50))
        self.nextButton.setMaximumSize(QSize(50, 16777215))
        icon3 = QIcon()
        icon3.addFile(u"UI/resources/right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextButton.setIcon(icon3)
        self.nextButton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.nextButton, 1, 6, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 5, 80, 5)
        self.pageLabel = QLabel(self.centralwidget)
        self.pageLabel.setObjectName(u"pageLabel")
        self.pageLabel.setMinimumSize(QSize(0, 25))
        self.pageLabel.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_2.addWidget(self.pageLabel)

        self.makeSelection = QPushButton(self.centralwidget)
        self.makeSelection.setObjectName(u"makeSelection")
        self.makeSelection.setMinimumSize(QSize(120, 25))
        self.makeSelection.setMaximumSize(QSize(120, 25))

        self.horizontalLayout_2.addWidget(self.makeSelection)

        self.applySelection = QPushButton(self.centralwidget)
        self.applySelection.setObjectName(u"applySelection")
        self.applySelection.setMinimumSize(QSize(120, 25))
        self.applySelection.setMaximumSize(QSize(120, 25))

        self.horizontalLayout_2.addWidget(self.applySelection)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 2, 7)

        self.fileDisplayWidget = QWidget(self.centralwidget)
        self.fileDisplayWidget.setObjectName(u"fileDisplayWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileDisplayWidget.sizePolicy().hasHeightForWidth())
        self.fileDisplayWidget.setSizePolicy(sizePolicy)
        self.fileDisplayWidget.setMinimumSize(QSize(800, 580))
        self.horizontalLayout_3 = QHBoxLayout(self.fileDisplayWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.gridLayout.addWidget(self.fileDisplayWidget, 1, 4, 1, 1)

        self.sideWidget = QWidget(self.centralwidget)
        self.sideWidget.setObjectName(u"sideWidget")
        self.sideWidget.setMinimumSize(QSize(250, 0))
        self.sideWidget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout = QVBoxLayout(self.sideWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.extractButton = QToolButton(self.sideWidget)
        self.extractButton.setObjectName(u"extractButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.extractButton.sizePolicy().hasHeightForWidth())
        self.extractButton.setSizePolicy(sizePolicy1)
        self.extractButton.setMinimumSize(QSize(140, 25))
        self.extractButton.setMaximumSize(QSize(140, 25))
        icon4 = QIcon()
        icon4.addFile(u"UI/resources/extract.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extractButton.setIcon(icon4)
        self.extractButton.setIconSize(QSize(16, 16))
        self.extractButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.extractButton.setAutoRaise(False)

        self.verticalLayout.addWidget(self.extractButton, 0, Qt.AlignHCenter)

        self.selectionsList = QListWidget(self.sideWidget)
        self.selectionsList.setObjectName(u"selectionsList")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.selectionsList.sizePolicy().hasHeightForWidth())
        self.selectionsList.setSizePolicy(sizePolicy2)
        self.selectionsList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.selectionsList.setDefaultDropAction(Qt.CopyAction)
        self.selectionsList.setSpacing(5)
        self.selectionsList.setUniformItemSizes(True)
        self.selectionsList.setSelectionRectVisible(False)
        self.selectionsList.setItemAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.selectionsList)

        self.clearAllButton = QPushButton(self.sideWidget)
        self.clearAllButton.setObjectName(u"clearAllButton")
        self.clearAllButton.setMinimumSize(QSize(140, 25))
        self.clearAllButton.setMaximumSize(QSize(140, 25))

        self.verticalLayout.addWidget(self.clearAllButton, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.sideWidget, 1, 0, 1, 1)

        ATOM.setCentralWidget(self.centralwidget)

        self.retranslateUi(ATOM)

        QMetaObject.connectSlotsByName(ATOM)
    # setupUi

    def retranslateUi(self, ATOM):
        ATOM.setWindowTitle(QCoreApplication.translate("ATOM", u"MainWindow", None))
        self.previousButton.setText("")
        self.titleLabel.setText(QCoreApplication.translate("ATOM", u"Blueprint Reader", None))
        self.exitButton.setText(QCoreApplication.translate("ATOM", u" Exit", None))
        self.pickFileButton.setText(QCoreApplication.translate("ATOM", u"Open File", None))
        self.nextButton.setText("")
        self.pageLabel.setText(QCoreApplication.translate("ATOM", u"Page 1/100", None))
        self.makeSelection.setText(QCoreApplication.translate("ATOM", u"Select Region", None))
        self.applySelection.setText(QCoreApplication.translate("ATOM", u"Apply Selection", None))
        self.extractButton.setText(QCoreApplication.translate("ATOM", u" Extract", None))
        self.clearAllButton.setText(QCoreApplication.translate("ATOM", u"Clear All", None))
    # retranslateUi

