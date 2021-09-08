from interface.design import *
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap

class RedimencionarImagem(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrirImagem)
        self.btnRedimencionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)

    def abrirImagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralWidget(),
            'abrir imagem',
            r'C:/Users/mathe_2led893/Downloads/Imagens/',
        )
        self.imputAbrirArquivo.setText(imagem)
        self.imagemOriginal = QPixmap(imagem)
        self.areaImagem.setPixmap(self.imagemOriginal)
        self.inputLagura.setText(str(self.imagemOriginal.width()))
        self.inputAltura.setText(str(self.imagemOriginal.height()))

    def redimensionar(self):
        lagura = int(self.inputLagura.text())
        self.novaImagem = self.imagemOriginal.scaledToWidth(lagura)
        self.areaImagem.setPixmap(self.novaImagem)
        self.inputLagura.setText(str(self.novaImagem.width()))
        self.inputAltura.setText(str(self.novaImagem.height()))  

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralWidget(),
            'salvar imagem',
            r'C:/Users/mathe_2led893/Downloads/Área de Trabalho/',
        )  
        self.novaImagem.save(imagem, 'PNG')         

