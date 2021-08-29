from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200 , 200 , 300, 300)
        self.setWindowTitle("My Window")
        self.initUI()
        self.counter = 0

    def click(self):
        self.counter += 1
        self.label.setText("you clicked the button {0} times".format(self.counter))
        self.update()


    def initUI(self):
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Press Me")
        self.button.clicked.connect(self.click)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("First Label")
        self.label.move(50,50) 
    
    def update(self):
        self.label.adjustSize()
        
    
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    


    win.show()
    sys.exit(app.exec_())

window()
