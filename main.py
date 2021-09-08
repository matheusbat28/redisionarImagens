import sys
from PyQt5.QtWidgets import QApplication
from telaFuncoes.app import RedimencionarImagem
    
qt = QApplication(sys.argv)
ig = RedimencionarImagem()
ig.show()
qt.exec_()