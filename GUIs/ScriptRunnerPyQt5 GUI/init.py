import sys
from main import Ui_MainWindow
from aboutcreator import *
#from button_logic import *
#from PyQt5 import QtCore, QtGui, QtWidgets
#from Auto import Ui_MainWindow
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from scripFunc.scripEXEC import *



#this is where all of the python logic will be.

class MainWstart(QMainWindow, Ui_MainWindow):
    def __init__(self):
        print('Script Runner has started')
        QMainWindow.__init__(self)
        self.setupUi(self)
        #self.actionAbout_Creator.clicked.connect(self.Ui_AboutCreator)
        self.actionAbout_Creator.triggered.connect(self.aboutCre)
        #self.quit_button.clicked.connect(self.quitButon)

    def aboutCre(Ui_AboutCreator):
        #QMainWindow.__init__(self)
        #self.setupUi(self)
        print('Showing about creator window')

    def funcassign():
        print('Assigning functions')

        buttonNames = []

    #def quitButon(self):
    #    print('Closing program')
    #    sys.exit()








if __name__ == "__main__":

    app = QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    main = MainWstart()
    main.show()
    sys.exit(app.exec_())
