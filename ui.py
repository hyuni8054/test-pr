# ch 8.1.3 ui.py
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout, QLineEdit, QComboBox, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore
class View(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le1 = QLineEdit('0', self)
        self.le1.setAlignment(QtCore.Qt.AlignRight)
        self.le1.setFocus(True)
        self.le1.selectAll()

        self.le2 = QLineEdit('0', self)
        self.le2.setAlignment(QtCore.Qt.AlignRight)

        self.cb = QComboBox(self)
        # self.cb.addItems(['+', '-', '*', '/', '^', '%'])
        self.cb.addItems(['+', '-', '*', '/'])

        hbox_formula = QHBoxLayout()
        hbox_formula.addWidget(self.le1)
        hbox_formula.addWidget(self.cb)
        hbox_formula.addWidget(self.le2)

        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.lbl1 = QLabel('v2.3.0', self)
        self.lbl1.setFont(QFont('Consolas', 10))
        self.btn1 = QPushButton('calc', self)
        self.btn2 = QPushButton('clear', self)

        hbox = QHBoxLayout()
        hbox.addWidget(self.lbl1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formula)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()
    
    def setDisplay(self, text):
        self.te1.appendPlainText(text)
    
    def clearMessage(self):
        self.te1.clear()