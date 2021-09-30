import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtGui import QPixmap
from numpy import float32
from Image_Manipulations import *


class Ui_MainWindow(object):
    """
    Code generated using Qt Designer
    Please ignore the code written from line 9 upto line 221. The code has been used to generate the GUI.
    It is generated automatically by PyQt5 Designer and is not required to be edited.
    """

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1261, 897)
        MainWindow.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.original_image = QtWidgets.QLabel(self.centralwidget)
        self.original_image.setGeometry(QtCore.QRect(220, 80, 681, 451))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.original_image.sizePolicy().hasHeightForWidth())
        self.original_image.setSizePolicy(sizePolicy)
        self.original_image.setAutoFillBackground(False)
        self.original_image.setText("")
        self.original_image.setObjectName("original_image")
        self.load_image = QtWidgets.QPushButton(self.centralwidget)
        self.load_image.setGeometry(QtCore.QRect(450, 580, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.load_image.sizePolicy().hasHeightForWidth())
        self.load_image.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.load_image.setFont(font)
        self.load_image.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                      "color: rgb(255, 255, 255);")
        self.load_image.setObjectName("load_image")
        self.histogram_equalization = QtWidgets.QPushButton(self.centralwidget)
        self.histogram_equalization.setGeometry(QtCore.QRect(80, 690, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.histogram_equalization.setFont(font)
        self.histogram_equalization.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                  "background-color: rgb(0, 170, 255);")
        self.histogram_equalization.setObjectName("histogram_equalization")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 640, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gamma_correction = QtWidgets.QPushButton(self.centralwidget)
        self.gamma_correction.setGeometry(QtCore.QRect(70, 780, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gamma_correction.setFont(font)
        self.gamma_correction.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                            "color: rgb(255, 255, 255);")
        self.gamma_correction.setObjectName("gamma_correction")
        self.log_transform = QtWidgets.QPushButton(self.centralwidget)
        self.log_transform.setGeometry(QtCore.QRect(450, 690, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.log_transform.setFont(font)
        self.log_transform.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                         "color: rgb(255, 255, 255);")
        self.log_transform.setObjectName("log_transform")
        self.blur_image = QtWidgets.QPushButton(self.centralwidget)
        self.blur_image.setGeometry(QtCore.QRect(450, 780, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.blur_image.setFont(font)
        self.blur_image.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 170, 255);")
        self.blur_image.setObjectName("blur_image")
        self.sharpen_image = QtWidgets.QPushButton(self.centralwidget)
        self.sharpen_image.setGeometry(QtCore.QRect(780, 690, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sharpen_image.setFont(font)
        self.sharpen_image.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                         "color: rgb(255, 255, 255);")
        self.sharpen_image.setObjectName("sharpen_image")
        self.special_effect = QtWidgets.QPushButton(self.centralwidget)
        self.special_effect.setGeometry(QtCore.QRect(780, 780, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.special_effect.setFont(font)
        self.special_effect.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                          "color: rgb(255, 255, 255);")
        self.special_effect.setObjectName("special_effect")
        self.undo_last = QtWidgets.QPushButton(self.centralwidget)
        self.undo_last.setGeometry(QtCore.QRect(1050, 620, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.undo_last.sizePolicy().hasHeightForWidth())
        self.undo_last.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.undo_last.setFont(font)
        self.undo_last.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                     "color: rgb(255, 255, 255);")
        self.undo_last.setObjectName("undo_last")
        self.undo_all = QtWidgets.QPushButton(self.centralwidget)
        self.undo_all.setGeometry(QtCore.QRect(1050, 690, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.undo_all.sizePolicy().hasHeightForWidth())
        self.undo_all.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.undo_all.setFont(font)
        self.undo_all.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                    "color: rgb(255, 255, 255);")
        self.undo_all.setObjectName("undo_all")
        self.save_image = QtWidgets.QPushButton(self.centralwidget)
        self.save_image.setGeometry(QtCore.QRect(1050, 780, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.save_image.sizePolicy().hasHeightForWidth())
        self.save_image.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.save_image.setFont(font)
        self.save_image.setStyleSheet("background-color: rgb(0, 0, 255);\n"
                                      "color: rgb(255, 255, 255);")
        self.save_image.setObjectName("save_image")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 0, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.msg = QtWidgets.QLabel(self.centralwidget)
        self.msg.setGeometry(QtCore.QRect(320, 540, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.msg.setFont(font)
        self.msg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msg.setStyleSheet("color: rgb(255, 255, 255);")
        self.msg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 830, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 255, 255);")
        self.label.setObjectName("label")
        self.gamma = QtWidgets.QLineEdit(self.centralwidget)
        self.gamma.setGeometry(QtCore.QRect(110, 830, 121, 31))
        self.gamma.setStyleSheet("background-color: rgb(252, 252, 252);\n"
                                 "color: rgb(0, 0, 0);")
        self.gamma.setAlignment(QtCore.Qt.AlignCenter)
        self.gamma.setObjectName("gamma")
        self.kernel = QtWidgets.QSlider(self.centralwidget)
        self.kernel.setGeometry(QtCore.QRect(500, 830, 160, 22))
        self.kernel.setMinimum(1)
        self.kernel.setMaximum(15)
        self.kernel.setSingleStep(2)
        self.kernel.setPageStep(10)
        self.kernel.setProperty("value", 5)
        self.kernel.setOrientation(QtCore.Qt.Horizontal)
        self.kernel.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.kernel.setTickInterval(2)
        self.kernel.setObjectName("kernel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 830, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(390, 860, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(170, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.sigma = QtWidgets.QLineEdit(self.centralwidget)
        self.sigma.setGeometry(QtCore.QRect(510, 860, 121, 31))
        self.sigma.setStyleSheet("background-color: rgb(252, 252, 252);\n"
                                 "color: rgb(0, 0, 0);")
        self.sigma.setAlignment(QtCore.Qt.AlignCenter)
        self.sigma.setObjectName("sigma")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(710, 730, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(170, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.sharpness = QtWidgets.QSlider(self.centralwidget)
        self.sharpness.setGeometry(QtCore.QRect(810, 740, 160, 22))
        self.sharpness.setMinimum(0)
        self.sharpness.setMaximum(5)
        self.sharpness.setOrientation(QtCore.Qt.Horizontal)
        self.sharpness.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sharpness.setTickInterval(1)
        self.sharpness.setObjectName("sharpness")
        MainWindow.setCentralWidget(self.centralwidget)

        # Modifications made manually
        self.original_image.setScaledContents(True)
        self.previous_img_path = "Previous_Image/prev_img.jpg"
        self.current_img_path = None
        # Default Kernel size for the gaussian blur
        self.kernel_size = 5

        # Connection specific function to the buttons clicked
        # Connect button to Load Image function
        self.load_image.clicked.connect(self.Load_Image)
        # Connect button to Histogram Equalization function
        self.histogram_equalization.clicked.connect(
            self.HISTOGRAM_EQUALIZATION)
        # Connect button to Gamma Correction function
        self.gamma_correction.clicked.connect(self.GAMMA_CORRECTION)
        # Connect button to Log Transformation function
        self.log_transform.clicked.connect(self.LOG_TRANSFORMATION)
        # Connect button to Blur Image function
        self.blur_image.clicked.connect(self.BLUR_IMAGE)
        # Connect button to Sharpen Image function
        self.sharpen_image.clicked.connect(self.SHARPEN_IMAGE)
        # Connect button to Undo Last function
        self.undo_last.clicked.connect(self.UNDO_LAST)
        # Connect button to Undo All function
        self.undo_all.clicked.connect(self.UNDO_ALL)
        # Connect button to Save Image function
        self.save_image.clicked.connect(self.SAVE_IMAGE)
        # Connect button to a Special Effect function
        self.special_effect.clicked.connect(self.SPECIAL_EFFECT)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Function to retranslate the UI
        This function is automatically generated by PyQt5 Designer
        Please do not manually edit this function 
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.load_image.setText(_translate("MainWindow", "Load Image"))
        self.histogram_equalization.setText(
            _translate("MainWindow", "Histogram Equalization"))
        self.label_3.setText(_translate("MainWindow", "Image Manipulation"))
        self.gamma_correction.setText(
            _translate("MainWindow", "Gamma Correction"))
        self.log_transform.setText(_translate("MainWindow", "Log Transform"))
        self.blur_image.setText(_translate("MainWindow", "Blur Image"))
        self.sharpen_image.setText(_translate("MainWindow", "Sharpen Image"))
        self.special_effect.setText(
            _translate("MainWindow", "Contrast Strech"))
        self.undo_last.setText(_translate("MainWindow", "Undo Last"))
        self.undo_all.setText(_translate("MainWindow", "Undo All"))
        self.save_image.setText(_translate("MainWindow", "Save Image"))
        self.label_4.setText(_translate("MainWindow", "BASIC IMAGE EDITOR"))
        self.msg.setText(_translate("MainWindow", "Let\'s Start"))
        self.label.setText(_translate("MainWindow", "gamma"))
        self.gamma.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "Kernel Size"))
        self.label_6.setText(_translate("MainWindow", "Sigma"))
        self.sigma.setText(_translate("MainWindow", "3"))
        self.label_7.setText(_translate("MainWindow", "Sharpness"))


########################################################################################################################
#                                    FUNCTIONS WRITTEN BY ME                                                           #
########################################################################################################################

    def Load_Image(self):
        """
        Function to load the image from the file system
        """
        file = QFileDialog.getOpenFileName()
        self.original_img_path = file[0]
        pixmap = QPixmap(self.original_img_path)
        self.original_image.setScaledContents(True)
        self.original_image.setPixmap(pixmap)
        self.current_img_path = self.original_img_path

    def HISTOGRAM_EQUALIZATION(self):
        """
        Function to perform histogram equalization on the image
        """
        if (self.current_img_path == None):
            self.msg.setText("Please load an image first")
            return

        # Read the image from the file system
        image = cv2.imread(self.current_img_path)
        # Save the image to the file system
        cv2.imwrite(self.previous_img_path, image)

        # Set the message to processing on the GUI
        self.msg.setText("Processing !")

        # Perform histogram equalization on the image
        img_output = Histogram_Equalization(image)

        # Update the current image path
        self.current_img_path = "Previous_Image/current_img.jpg"

        # Save the image to the file system
        cv2.imwrite(self.current_img_path, img_output)
        # Load the image into the GUI
        pixmap = QPixmap(self.current_img_path)
        # Update the GUI with the new image
        self.original_image.setPixmap(pixmap)

        # Set the message to "Done !" on the GUI
        self.msg.setText("Done !")

    def GAMMA_CORRECTION(self):
        """
        Function to perform gamma correction on the image
        """
        if (self.current_img_path == None):                 # If no image is loaded then set out the message
            self.msg.setText("Please load an image first")
            return

        # Get the value of gamma from the text box
        gamma = float32(self.gamma.text())
        # Read the image from the file system
        image = cv2.imread(self.current_img_path)
        # Save the image in the previous image folder
        cv2.imwrite(self.previous_img_path, image)

        # Set the message to processing on the GUI
        self.msg.setText("Processing !")

        # Perform gamma correction on the image
        img_output = Gamma_Correction(image, gamma)

        # Set the current image path to the previous image path
        self.current_img_path = "Previous_Image/current_img.jpg"

        # Save the image in the current image folder
        cv2.imwrite(self.current_img_path, img_output)
        # Load the image in the GUI
        pixmap = QPixmap(self.current_img_path)
        # Update the GUI with the new image
        self.original_image.setPixmap(pixmap)

        # Set the message to "Done !" on the GUI
        self.msg.setText("Done !")

    def LOG_TRANSFORMATION(self):
        """
        Function to perform log transformation on the image
        """
        if (self.current_img_path == None):                 # If no image is loaded then set out the message
            self.msg.setText("Please load an image first")
            return

        image = cv2.imread(self.current_img_path)           # Read the image
        # Save the image in the previous image path
        cv2.imwrite(self.previous_img_path, image)

        # Set the message to processing on the GUI
        self.msg.setText("Processing !")

        # Perform log transformation on the image
        img_output = Log_Transformation(image)

        # Set the current image path to the previous image path
        self.current_img_path = "Previous_Image/current_img.jpg"

        # Save the image in the current image path
        cv2.imwrite(self.current_img_path, img_output)
        # Load the image in the GUI
        pixmap = QPixmap(self.current_img_path)
        # Update the GUI with the new image
        self.original_image.setPixmap(pixmap)

        # Set the message to "Done !" on the GUI
        self.msg.setText("Done !")

    def BLUR_IMAGE(self):
        """
        Function to perform blurring on the image
        """
        if (self.current_img_path == None):                 # If no image is loaded then set out the message
            self.msg.setText("Please load an image first")
            return

        # Get the value of sigma from the text box
        sigma = float(self.sigma.text())

        image = cv2.imread(self.current_img_path)           # Read the image
        # Save the image in the previous image path
        cv2.imwrite(self.previous_img_path, image)

        # Set the message to processing on the GUI
        self.msg.setText("Processing !")

        # Perform blurring on the image
        img_output = GaussianBlur(image, int(self.kernel.value()), sigma)

        # Set the current image path to the previous image path
        self.current_img_path = "Previous_Image/current_img.jpg"

        # Save the image in the current image path
        cv2.imwrite(self.current_img_path, img_output)
        # Load the image in the GUI
        pixmap = QPixmap(self.current_img_path)
        # Update the GUI with the new image
        self.original_image.setPixmap(pixmap)

        # Set the message to "Done !" on the GUI
        self.msg.setText("Done !")

    def SHARPEN_IMAGE(self):
        """
        Function to perform sharpening on the image
        """
        if (self.current_img_path == None):                 # If no image is loaded then set out the message
            self.msg.setText("Please load an image first")
            return

        image = cv2.imread(self.current_img_path)           # Read the image
        # Save the image in the previous image path
        cv2.imwrite(self.previous_img_path, image)

        # Set the message to processing on the GUI
        self.msg.setText("Processing !")
        # Perform sharpening on the image
        img_output = Sharpen(image, int(self.sharpness.value()))

        # Set the current image path to the previous image path
        self.current_img_path = "Previous_Image/current_img.jpg"

        # Save the image in the current image path
        cv2.imwrite(self.current_img_path, img_output)
        # Load the image in the GUI
        pixmap = QPixmap(self.current_img_path)
        # Update the GUI with the new image
        self.original_image.setPixmap(pixmap)

        # Set the message to "Done !" on the GUI
        self.msg.setText("Done !")

    def UNDO_LAST(self):
        """
        Function to undo the last operation
        """
        if (self.current_img_path == None):                 # If no image is loaded then set out the message
            self.msg.setText("Please load an image first")
            return

        # If no image is loaded then set out the message
        if (self.previous_img_path == None):
            self.msg.setText("No previous image")
            return

        # Set the message to processing on the GUI
        self.msg.setText("Processing !")

        # Set the current image path to the previous image path
        self.current_img_path = self.previous_img_path
        # Load the image in the GUI
        pixmap = QPixmap(self.current_img_path)
        # Update the GUI with the new image
        self.original_image.setPixmap(pixmap)

        # Set the message to "Done !" on the GUI
        self.msg.setText("Done !")

    def UNDO_ALL(self):
        """
        Function to undo all the operations
        """
        if (self.current_img_path == None):                 # If no image is loaded then set out the message
            self.msg.setText("Please load an image first")
            return

        # If no image is loaded then set out the message
        if (self.previous_img_path == None):
            self.msg.setText("No previous image")
            return

        # Set the message to processing on the GUI
        self.msg.setText("Processing !")

        # Set the current image path to the original image path
        self.current_img_path = self.original_img_path
        # Load the image in the GUI
        pixmap = QPixmap(self.current_img_path)
        # Update the GUI with the new image
        self.original_image.setPixmap(pixmap)

        # Set the message to "Done !" on the GUI
        self.msg.setText("Done !")

    def SAVE_IMAGE(self):
        """
        Function to save the image
        """
        if (self.current_img_path == None):                 # If no image is loaded then set out the message
            self.msg.setText("Please load an image first")
            return

        # Set the message to processing on the GUI
        self.msg.setText("Processing !")

        self.current_img_path = "Previous_Image/current_img.jpg"
        self.saving_path = "Saved_Images/saved_img.jpg"
        img = cv2.imread(self.current_img_path)             # Read the image
        # Save the image in the saved image path
        cv2.imwrite(self.saving_path, img)

        # Set the message to "Done !" on the GUI
        self.msg.setText("Done !")

    def SPECIAL_EFFECT(self):
        """
        Function to perform a special effect on the image
        For Special effect I am using Contrast Streching which has not  been asked to be implemented in any assignment questions
        """
        if (self.current_img_path == None):                 # If no image is loaded then set out the message
            self.msg.setText("Please load an image first")
            return

        image = cv2.imread(self.current_img_path)           # Read the image
        # Save the image in the previous image path
        cv2.imwrite(self.previous_img_path, image)

        # Set the message to processing on the GUI
        self.msg.setText("Processing !")

        # Perform log transformation on the image
        img_output = Contrast_Stretching(image)

        # Set the current image path to the previous image path
        self.current_img_path = "Previous_Image/current_img.jpg"

        # Save the image in the current image path
        cv2.imwrite(self.current_img_path, img_output)
        # Load the image in the GUI
        pixmap = QPixmap(self.current_img_path)
        # Update the GUI with the new image
        self.original_image.setPixmap(pixmap)

        # Set the message to "Done !" on the GUI
        self.msg.setText("Done !")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
