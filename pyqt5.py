import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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
        self.sample1 = QLabel("This is comment", self)
        self.sample2 = QLineEdit(self)
        self.button_pass = QPushButton("パスを選択...", self)
        self.button_pass.clicked.connect(self.ShowDialog)
        layout = QGridLayout()
        layout.setSpacing(10)
        layout.addWidget(self.sample1,0,0)
        layout.addWidget(self.sample2,1,0)
        layout.addWidget(self.button_pass,1,2)
        self.setLayout(layout)
        self.show()

    @pyqtSlot()
    # epubからメタデータを取得
    def ShowDialog(self):
        text = text_dir
        fname = QFileDialog.getOpenFileName(self, 'Open file',text,"テキストファイル(*.txt)")
        path = fname[0]
        if path != "":
            QMessageBox.question(self, "Message", "the file dir is " + path, QMessageBox.Ok, QMessageBox.Ok)
            self.sample2.setText(path)


def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    
    main()
