import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout

class App(QWidget):
    def __init__(self):
        super().__init__()

        # Configuração da janela principal
        self.setWindowTitle('Anexar Arquivo XLSX')
        self.setFixedSize(700, 400)
        self.setGeometry(100, 100, 400, 200)

        # Criando botão para anexar o arquivo
        button = QPushButton('Anexar Arquivo .xlsx', self)
        button.clicked.connect(self.attach_file)
        
        # Criando botão para salvar o arquivo
        save_button = QPushButton('Salvar Arquivo Excel', self)
        save_button.clicked.connect(self.save_file)

        # Layout para o botão
        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(save_button)
        self.setLayout(layout)

    def attach_file(self):
        # Abrir diálogo para selecionar um arquivo Excel (.xlsx)
        file_name, _ = QFileDialog.getOpenFileName(self, 'Abrir Arquivo Excel', '', 'Arquivos Excel (*.xlsx);;Todos os Arquivos (*)')

        if file_name:
            print(f'Arquivo selecionado: {file_name}')
            self.read_excel(file_name)  # Ler e processar o arquivo

    def read_excel(self, file_path):
        try:
            # Lendo o arquivo Excel com pandas
            df1 = pd.read_excel(file_path)

            # Exibindo o conteúdo do DataFrame no console
            print("Conteúdo do arquivo Excel:")
            print(df1)

            # Você pode processar o DataFrame conforme sua necessidade
            # Exemplo: Mostrar os nomes das colunas
            
        except Exception as e:
            print(f'Ocorreu um erro ao ler o arquivo Excel: {e}')
            
    def save_file(self):
        # Criar um DataFrame com dados de exemplo
        dados = {
            'Nome': ['Ana', 'João', 'Maria'],
            'Idade': [25, 30, 22],
            'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
        }
        df2 = pd.DataFrame(dados)

        # Abrir um diálogo de "Salvar Como"
        file_path, _ = QFileDialog.getSaveFileName(self, 'Salvar Arquivo Excel', '', 'Arquivos Excel (*.xlsx)')

        if file_path:
            try:
                # Certificar-se de que o arquivo termina com .xlsx
                if not file_path.endswith('.xlsx'):
                    file_path += '.xlsx'

                # Salvar o DataFrame como um arquivo Excel
                df2.to_excel(file_path, index=False)
                print(f"Arquivo Excel salvo em: {file_path}")
            except Exception as e:
                print(f"Erro ao salvar o arquivo: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
