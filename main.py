import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# Classe principal da aplicação
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha Primeira Janela")
        self.setGeometry(100, 100, 800, 600)  # Define posição e tamanho da janela

# Configuração principal da aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Instância do aplicativo
    window = MainWindow()         # Cria a janela principal
    window.show()                 # Exibe a janela
    sys.exit(app.exec_())         # Executa o loop da aplicação