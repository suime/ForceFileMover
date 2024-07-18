# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(300, 300))
        MainWindow.setMaximumSize(QSize(300, 300))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(300, 300))
        self.centralwidget.setMaximumSize(QSize(300, 300))
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setAcceptDrops(True)
        self.frame.setStyleSheet(u"gridline-color: rgb(92, 191, 191);\n"
"border-color: rgb(109, 109, 109);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.status = QLabel(self.centralwidget)
        self.status.setObjectName(u"status")
        self.status.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.status)

        self.openFile = QPushButton(self.centralwidget)
        self.openFile.setObjectName(u"openFile")

        self.verticalLayout_3.addWidget(self.openFile)

        self.verticalLayout_3.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>ForceFileMover 1.0</p><p>1. \ud30c\uc77c\uc744 \uc5f4\uac70\ub098 \ub5a8\uad70\ub2e4. </p><p>2. \ud30c\uc77c \uc704\uce58\uc5d0 \ud574\ub2f9 \ud30c\uc77c\uba85.csv\ub85c \uc0c8\ub85c\uc6b4 \ud30c\uc77c\uc774 \uc0dd\uc131\ub41c\ub2e4.</p><p>3. csv \ud30c\uc77c\uc744 \ud30c\uc77c\ubb34\ubc84\ub85c \ub118\uae34\ub2e4.</p><p>4. \ub2e4\ub978 \ub9dd\uc5d0\uc11c \ub2e4\uc2dc \ud30c\uc77c\uc744 \uc774\uac78\ub85c \uc5f0\ub2e4. </p><p>5. \uadf8\ub7fc \uc6d0\ubcf8 \ud30c\uc77c\ub85c \ubcf5\uad6c\ub41c\ub2e4.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Drag and Drop", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.openFile.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc5f4\uae30", None))
    # retranslateUi

