# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'custom_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_Custom_Widget(object):
    def setupUi(self, Custom_Widget):
        if not Custom_Widget.objectName():
            Custom_Widget.setObjectName(u"Custom_Widget")
        Custom_Widget.resize(467, 42)
        self.horizontalLayout = QHBoxLayout(Custom_Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.minus_btn = QPushButton(Custom_Widget)
        self.minus_btn.setObjectName(u"minus_btn")

        self.horizontalLayout.addWidget(self.minus_btn)

        self.spin_Box = QSpinBox(Custom_Widget)
        self.spin_Box.setObjectName(u"spin_Box")

        self.horizontalLayout.addWidget(self.spin_Box)

        self.plus_btn = QPushButton(Custom_Widget)
        self.plus_btn.setObjectName(u"plus_btn")

        self.horizontalLayout.addWidget(self.plus_btn)


        self.retranslateUi(Custom_Widget)

        QMetaObject.connectSlotsByName(Custom_Widget)
    # setupUi

    def retranslateUi(self, Custom_Widget):
        Custom_Widget.setWindowTitle(QCoreApplication.translate("Custom_Widget", u"Form", None))
        self.minus_btn.setText(QCoreApplication.translate("Custom_Widget", u"Minus", None))
        self.plus_btn.setText(QCoreApplication.translate("Custom_Widget", u"Plus", None))
    # retranslateUi

