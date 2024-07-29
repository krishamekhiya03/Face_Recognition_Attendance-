# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 818)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #D6FB90;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutCentral = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayoutCentral.setObjectName("verticalLayoutCentral")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutCentral.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(200, -1, 200, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(200, 0))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/register.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(200, 0))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/Attendance.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(200, 0))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/report.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 65))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: #4CAF50;\n"
"border: 1px solid #555;\n"
"border-radius: 30px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 65))
        self.pushButton.setMaximumSize(QtCore.QSize(16777, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: #4CAF50;\n"
"border: 1px solid #555;\n"
"border-radius: 30px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 65))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: #4CAF50;\n"
"border: 1px solid #555;\n"
"border-radius: 30px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_7.addWidget(self.pushButton_2)
        self.gridLayout_6.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem5 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setMinimumSize(QtCore.QSize(80, 40))
        self.exitButton.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("background-color: #FF6347;\n"
"border: 1px solid #555;\n"
"border-radius: 10px;")
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout_8.addWidget(self.exitButton)
        spacerItem6 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayoutCentral.addLayout(self.verticalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutCentral.addItem(spacerItem7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome to the Facial Recognition Attendance System!"))
        self.pushButton_3.setText(_translate("MainWindow", "Add Student Information"))
        self.pushButton.setText(_translate("MainWindow", "Attendance"))
        self.pushButton_2.setText(_translate("MainWindow", "Attendance Report"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())