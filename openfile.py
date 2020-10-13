# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpenFile.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import tempfile
import os
import sys
try:
    ressources = sys._MEIPASS
except:
    ressources = "."

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(320, 330)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(ressources,"nticon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setPixmap(QtGui.QPixmap(os.path.join(ressources,'nt_no_1bg.png')).scaled(80,80,QtCore.Qt.KeepAspectRatio))
        self.label.move(110,260)
        self.openfile = QtWidgets.QPushButton(self.centralwidget)
        self.openfile.setGeometry(QtCore.QRect(30, 20, 261, 31))
        self.openfile.setObjectName("openfile")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 80, 261, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(30, 150, 261, 31))
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 130, 261, 16))
        self.label.setObjectName("label")
        self.bouton_valider = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_valider.setGeometry(QtCore.QRect(30, 210, 261, 31))
        self.bouton_valider.setObjectName("bouton_valider")
        self.bouton_valider.setEnabled(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 321, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "P&L - Mc4U"))
        MainWindow.setStatusTip(_translate("MainWindow", "Version 0.2"))
        self.openfile.setText(_translate("MainWindow", "Sélectionnez le fichier .txt à analyser"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Nom de l\'entitée (optionnel)"))
        self.label.setText(_translate("MainWindow", "Sélectionner votre mois pour le format Mc4U"))
        self.bouton_valider.setText(_translate("MainWindow", "Go"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
