# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(820, 720)
        self.lblCamara = QtWidgets.QLabel(Form)
        self.lblCamara.setGeometry(QtCore.QRect(90, 70, 600, 400))
        self.lblCamara.setObjectName("lblCamara")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 10, 731, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(90, 500, 311, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.rbAprender = QtWidgets.QRadioButton(self.groupBox)
        self.rbAprender.setGeometry(QtCore.QRect(20, 30, 141, 16))
        self.rbAprender.setChecked(True)
        self.rbAprender.setObjectName("rbAprender")
        self.rbAdivinar = QtWidgets.QRadioButton(self.groupBox)
        self.rbAdivinar.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.rbAdivinar.setObjectName("rbAdivinar")
        self.btnIniciar = QtWidgets.QPushButton(self.groupBox)
        self.btnIniciar.setGeometry(QtCore.QRect(0, 100, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnIniciar.setFont(font)
        self.btnIniciar.setObjectName("btnIniciar")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(410, 500, 281, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lblResultado = QtWidgets.QLabel(self.groupBox_2)
        self.lblResultado.setGeometry(QtCore.QRect(50, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblResultado.setFont(font)
        self.lblResultado.setObjectName("lblResultado")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DetectorFiguras v1.0"))
        self.lblCamara.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#00557f;\">Aprender Figuras Geométricas Basicas</span></p></body></html>"))
        self.groupBox.setTitle(_translate("Form", "Eligir que quieres hacer"))
        self.rbAprender.setText(_translate("Form", "Aprender"))
        self.rbAdivinar.setText(_translate("Form", "Adivinar"))
        self.btnIniciar.setText(_translate("Form", "INICIAR"))
        self.groupBox_2.setTitle(_translate("Form", "Resultado"))
        self.lblResultado.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">**********</span></p></body></html>"))

#import dir_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

