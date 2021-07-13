import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from smth import Ui_MainWindow


class Tree(QtWidgets.QMainWindow):
    def __init__(self):
        super(Tree, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_Ui()
        
    def init_Ui(self):
        self.setWindowIcon(QtGui.QIcon('Images/window_icon.ico'))
        self.ui.input.setPlaceholderText('Enter the country')
        self.setFixedSize(QtCore.QSize(623, 915))
        self.move(900, 40)
        
        
app = QtWidgets.QApplication([])
application = Tree()
application.show()

sys.exit(app.exec())
