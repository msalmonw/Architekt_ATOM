# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectionDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_selectionDialog(object):
    def setupUi(self, selectionDialog):
        if not selectionDialog.objectName():
            selectionDialog.setObjectName(u"selectionDialog")
        selectionDialog.setWindowModality(Qt.WindowModal)
        selectionDialog.resize(400, 500)
        selectionDialog.setMinimumSize(QSize(400, 500))
        selectionDialog.setStyleSheet(u"QWidget#selectionDialog{\n"
"background:rgba(30, 33, 36, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QWidget{\n"
"background: rgba(51, 57, 73, 255);\n"
"border-radius: 10px;\n"
"font-family: Poppins;\n"
"font-size: 16px;\n"
"font-weight: 400;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"border: 0px;\n"
"background: rgba(0, 128, 255, 255);\n"
"color: rgba(255, 255, 255, 255);\n"
"font-weight: 600;\n"
"border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"border: 2px solid transparent;\n"
"}\n"
"QPushButton#cancelButton{\n"
"background: transparent;\n"
"color: rgba(0, 128, 255, 255);\n"
"}\n"
"QLabel#titleLabel{\n"
"background: transparent;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QCheckBox{\n"
"background: transparent;\n"
"padding-left: 10px;\n"
"}")
        selectionDialog.setSizeGripEnabled(False)
        selectionDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(selectionDialog)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.titleLabel = QLabel(selectionDialog)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMinimumSize(QSize(0, 30))
        self.titleLabel.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.titleLabel)

        self.selectionBox = QComboBox(selectionDialog)
        self.selectionBox.setObjectName(u"selectionBox")
        self.selectionBox.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.selectionBox)

        self.tableSelected = QCheckBox(selectionDialog)
        self.tableSelected.setObjectName(u"tableSelected")

        self.verticalLayout.addWidget(self.tableSelected)

        self.verticalSpacer = QSpacerItem(20, 258, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 5, 10, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(selectionDialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setMinimumSize(QSize(80, 30))
        self.cancelButton.setMaximumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.cancelButton)

        self.saveButton = QPushButton(selectionDialog)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(80, 30))
        self.saveButton.setMaximumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.saveButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(selectionDialog)

        QMetaObject.connectSlotsByName(selectionDialog)
    # setupUi

    def retranslateUi(self, selectionDialog):
        selectionDialog.setWindowTitle(QCoreApplication.translate("selectionDialog", u"Dialog", None))
        self.titleLabel.setText(QCoreApplication.translate("selectionDialog", u"Edit Selection", None))
        self.tableSelected.setText(QCoreApplication.translate("selectionDialog", u"  Table Selected", None))
        self.cancelButton.setText(QCoreApplication.translate("selectionDialog", u"Cancel", None))
        self.saveButton.setText(QCoreApplication.translate("selectionDialog", u"Save", None))
    # retranslateUi

