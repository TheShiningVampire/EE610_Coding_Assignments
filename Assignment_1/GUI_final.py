import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtGui import QPixmap
from Image_Manipulations import *

class Ui_MainWindow(object):
    # Code generated using Qt Designer
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1160, 880)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.original_image = QtWidgets.QLabel(self.centralwidget)
        self.original_image.setGeometry(QtCore.QRect(210, 80, 711, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.original_image.sizePolicy().hasHeightForWidth())
        self.original_image.setSizePolicy(sizePolicy)
        self.original_image.setAutoFillBackground(True)
        self.original_image.setText("")
        self.original_image.setObjectName("original_image")
        self.load_image = QtWidgets.QPushButton(self.centralwidget)
        self.load_image.setGeometry(QtCore.QRect(180, 690, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_image.sizePolicy().hasHeightForWidth())
        self.load_image.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.load_image.setFont(font)
        self.load_image.setObjectName("load_image")
        self.histogram_equalization = QtWidgets.QPushButton(self.centralwidget)
        self.histogram_equalization.setGeometry(QtCore.QRect(450, 630, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.histogram_equalization.setFont(font)
        self.histogram_equalization.setObjectName("histogram_equalization")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 590, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gamma_correction = QtWidgets.QPushButton(self.centralwidget)
        self.gamma_correction.setGeometry(QtCore.QRect(450, 670, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gamma_correction.setFont(font)
        self.gamma_correction.setObjectName("gamma_correction")
        self.log_transform = QtWidgets.QPushButton(self.centralwidget)
        self.log_transform.setGeometry(QtCore.QRect(450, 710, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.log_transform.setFont(font)
        self.log_transform.setObjectName("log_transform")
        self.blur_image = QtWidgets.QPushButton(self.centralwidget)
        self.blur_image.setGeometry(QtCore.QRect(450, 750, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.blur_image.setFont(font)
        self.blur_image.setObjectName("blur_image")
        self.sharpen_image = QtWidgets.QPushButton(self.centralwidget)
        self.sharpen_image.setGeometry(QtCore.QRect(450, 790, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sharpen_image.setFont(font)
        self.sharpen_image.setObjectName("sharpen_image")
        self.special_effect = QtWidgets.QPushButton(self.centralwidget)
        self.special_effect.setGeometry(QtCore.QRect(450, 830, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.special_effect.setFont(font)
        self.special_effect.setObjectName("special_effect")
        self.undo_last = QtWidgets.QPushButton(self.centralwidget)
        self.undo_last.setGeometry(QtCore.QRect(870, 620, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undo_last.sizePolicy().hasHeightForWidth())
        self.undo_last.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.undo_last.setFont(font)
        self.undo_last.setObjectName("undo_last")
        self.undo_all = QtWidgets.QPushButton(self.centralwidget)
        self.undo_all.setGeometry(QtCore.QRect(870, 700, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undo_all.sizePolicy().hasHeightForWidth())
        self.undo_all.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.undo_all.setFont(font)
        self.undo_all.setObjectName("undo_all")
        self.save_image = QtWidgets.QPushButton(self.centralwidget)
        self.save_image.setGeometry(QtCore.QRect(870, 790, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_image.sizePolicy().hasHeightForWidth())
        self.save_image.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.save_image.setFont(font)
        self.save_image.setObjectName("save_image")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 10, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        # Modifications made manually
        self.original_image.setScaledContents(True)  
        self.previous_img_path = "Previous_Image/prev_img.jpg"
        self.current_img_path = None

        # Connection specific function to the buttons clicked
        self.load_image.clicked.connect(self.Load_Image)
        self.histogram_equalization.clicked.connect(self.HISTOGRAM_EQUALIZATION)
        self.gamma_correction.clicked.connect(self.GAMMA_CORRECTION)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.load_image.setText(_translate("MainWindow", "Load Image"))
        self.histogram_equalization.setText(_translate("MainWindow", "Histogram Equalization"))
        self.label_3.setText(_translate("MainWindow", "Image Manipulation"))
        self.gamma_correction.setText(_translate("MainWindow", "Gamma Correction"))
        self.log_transform.setText(_translate("MainWindow", "Log Transform"))
        self.blur_image.setText(_translate("MainWindow", "Blur Image"))
        self.sharpen_image.setText(_translate("MainWindow", "Sharpen Image"))
        self.special_effect.setText(_translate("MainWindow", "Special Effect"))
        self.undo_last.setText(_translate("MainWindow", "Undo Last"))
        self.undo_all.setText(_translate("MainWindow", "Undo All"))
        self.save_image.setText(_translate("MainWindow", "Save Image"))
        self.label_4.setText(_translate("MainWindow", "BASIC IMAGE EDITOR"))

    def Load_Image(self):
        file = QFileDialog.getOpenFileName()
        self.original_imp_path = file[0]
        pixmap = QPixmap(self.original_imp_path)
        self.original_image.setScaledContents(True)
        self.original_image.setPixmap(pixmap) 
        self.current_img_path = self.original_imp_path  


    def HISTOGRAM_EQUALIZATION(self):
        if (self.current_img_path == None):
            print("No image loaded")

        image = cv2.imread(self.current_img_path)
        cv2.imwrite(self.previous_img_path, image)

        img_output = Histogram_Equalization(image)

        self.current_img_path = "Previous_Image/current_img.jpg"

        cv2.imwrite(self.current_img_path, img_output)
        pixmap = QPixmap(self.current_img_path)
        self.original_image.setPixmap(pixmap) 


    def GAMMA_CORRECTION(self):
        image = cv2.imread(self.current_img_path)
        cv2.imwrite(self.previous_img_path, image)
        
        img_output = Gamma_Correction(image,2)

        self.current_img_path = "Previous_Image/current_img.jpg"

        cv2.imwrite(self.current_img_path, img_output)
        pixmap = QPixmap(self.current_img_path)
        self.original_image.setPixmap(pixmap)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
