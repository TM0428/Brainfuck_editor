import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import main as ma
import logic
import bf_interpreter

text_dir = os.getcwd()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.title = "Brainfuck Compiler"
        self.title_text = ""
        self.initUI()
        
        
    def initUI(self):               
        #設定
        self.setWindowTitle(self.title)
        self.resize(600, 600)
        self.center()
        self.statusBar().showMessage("Made by TM,idaten")
        mainMenu = self.menuBar() 
        fileMenu = mainMenu.addMenu("File")
        helpMenu = mainMenu.addMenu("Help")
        exitButton = QAction(QIcon("exit24.png"), "Exit", self)
        exitButton.setShortcut("Ctrl+Q")
        exitButton.setStatusTip("Exit application")
        exitButton.triggered.connect(self.close)
        versionbutton = QAction(QIcon("hoge.png"), "バージョン", self)
        versionbutton.triggered.connect(self.versiontab)
        fileMenu.addAction(exitButton)
        helpMenu.addAction(versionbutton)
        tmp = UI(self)

        self.setCentralWidget(tmp)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def versiontab(self):
        QMessageBox.question(self, "Version", "0.0.1 beta", QMessageBox.Ok, QMessageBox.Ok)

#UIを作成しているウィンドウ
class UI(QWidget):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.path_label = QLabel("path", self)
        self.bf_label = QLabel("bf code", self)
        self.input_label = QLabel("input", self)
        self.output_label = QLabel("output", self)
        
        self.path_text = QLineEdit(self)
        self.txt_box = QTextEdit(self)
        self.bf_box = QTextEdit(self)
        self.input_box = QTextEdit(self)
        self.output_box = QTextEdit(self)
        self.button_pass = QPushButton("パスを選択...", self)
        self.button_pass.clicked.connect(self.ShowDialog)
        self.compile_button = QPushButton("compile→", self)
        self.compile_button.clicked.connect(self.compile)
        self.bf_run_button = QPushButton("run↓", self)
        self.bf_run_button.clicked.connect(self.run)


        layoutA = QGridLayout()
        layoutA.setSpacing(10)
        layoutA.addWidget(self.path_label,0,0)
        layoutA.addWidget(self.path_text,1,0)
        layoutA.addWidget(self.txt_box,2,0)
        layoutA.addWidget(self.button_pass,1,2)
        layoutA.addWidget(self.compile_button,2,2)
        layoutA.addWidget(self.bf_run_button,3,2)


        layoutB = QGridLayout()
        layoutB.addWidget(self.bf_label,0,0)
        layoutB.addWidget(self.bf_box,1,0)

        layoutC = QGridLayout()
        layoutC.addWidget(self.input_label,0,0)
        layoutC.addWidget(self.input_box,1,0)
        layoutC.addWidget(self.output_label,2,0)
        layoutC.addWidget(self.output_box,3,0)

        layout = QGridLayout()
        layout.addLayout(layoutA,0,0)
        layout.addLayout(layoutB,0,1)
        layout.addLayout(layoutC,1,0,1,2)
        self.setLayout(layout)
        self.show()

    @pyqtSlot()
    # epubからメタデータを取得
    def ShowDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',text_dir,"テキストファイル(*.txt)")
        path = fname[0]
        if path != "":
            #QMessageBox.question(self, "Message", "the file dir is " + path, QMessageBox.Ok, QMessageBox.Ok)
            with open(path) as f:
                text = f.read()
            self.path_text.setText(path)
            self.txt_box.setText(text)
    def compile(self):
        txt = self.txt_box.toPlainText()
        bf = ma.Brainfuck()
        #txt_list = txt.split("\n")
        """
        line = 1
        for v in txt_list:
            ma.judge(bf,v,line,None,True)
        """
        ma.call_from_pyqt(txt,bf)
        self.bf_box.setText(bf.output)

    def run(self):
        bfi = bf_interpreter.Bf_interpreter(self.input_box.toPlainText())
        bfi.set_source(self.bf_box.toPlainText())
        bfi.parsing()
        bfi.interperter()
        if bfi.err == 1:
            QMessageBox.warning(self,"Warning","Input is not defined.", QMessageBox.Ok)
        self.output_box.setText(bfi.outputs)
        
def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    
    main()
