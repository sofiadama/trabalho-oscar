import PySimpleGUI as sg

class TelaCategoria():
    def __init__(self):
        sg.theme('DarkTeal4')
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        opcao = -1
        if values.get('1'):
            opcao = 1
        elif values.get('2'):
            opcao = 2
        elif values.get('3'):
            opcao = 3
        elif values.get('4'):
            opcao = 4
        elif values.get('0') or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        layout = [
            [sg.Text('-------- CATEGORIAS ----------', font=("Helvetica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvetica", 15))],
            [sg.Radio('Incluir Categoria', "RD1", key='1')],
            [sg.Radio('Alterar Categoria', "RD1", key='2')],
            [sg.Radio('Listar Categoria', "RD1", key='3')],
            [sg.Radio('Excluir Categoria', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema do Oscar', layout)

    def pegar_dados_categoria(self):
        layout = [
            [sg.Text('-------- DADOS CATEGORIA ----------', font=("Helvetica", 25))],
            [sg.Text('Título:', size=(15, 1)), sg.InputText('', key='titulo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema do Oscar', layout)
        button, values = self.open()
        self.close()

        if button in (None, 'Cancelar'):
            return None

        titulo = values.get('titulo')
        if not titulo or titulo.strip() == '':
            sg.popup_error("O título da categoria não pode ser vazio.")
            return {"titulo": None}  

        return {"titulo": titulo.strip()}


    def mostrar_dados_categoria(self, dados_categoria):
        string_todas_categorias = ""
        for dado in dados_categoria:
            string_todas_categorias += f"TÍTULO: {dado['titulo']}\n\n"
        sg.Popup('-------- LISTA DE CATEGORIAS ----------', string_todas_categorias)


    def selecionar_categoria(self):
        while True:
            layout = [
                [sg.Text('-------- SELECIONAR CATEGORIA ----------', font=("Helvetica", 25))],
                [sg.Text('Digite a categoria que deseja selecionar:', font=("Helvetica", 15))],
                [sg.Text('TÍTULO:', size=(15, 1)), sg.InputText('', key='titulo')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Seleciona categoria', layout)

            button, values = self.open()
            self.close()

            if button in (None, 'Cancelar'):
                return None

            titulo = values.get('titulo', '').strip()
            if titulo == '':
                sg.popup('Erro! O título não pode ficar vazio')
            else:
                return titulo

    def mostrar_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.close()

    def open(self):
        return self.__window.read()