import sys
from PyQt4 import QtGui

class Wendow(QtGui.QtMainWindow):
    super(Wendow,self).__init__()
    self.setGeometry(120,100,500,200)
    self.setWindowTitle("Temps")
    self.show()

tt = QtGui.QApplication(sys.argv)
GUI = Wendow()
