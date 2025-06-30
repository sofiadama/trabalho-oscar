import PySimpleGUI as sg

class TelaFilme():      
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
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- FILMES ----------', font=("Helvetica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvetica", 15))],
            [sg.Radio('Incluir Filme', "RD1", key='1')],
            [sg.Radio('Alterar Filme', "RD1", key='2')],
            [sg.Radio('Listar Filme', "RD1", key='3')],
            [sg.Radio('Excluir Filme', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema do Oscar', layout)

    def tela_filtros_de_relatorios(self):
        while True:
            layout = [
                [sg.Text('-------- RELATÓRIO DE INDICAÇÕES ----------', font=('Helvetica', 20))],
                [sg.Text('Escolha uma opção:', font=('Helvetica', 14))],
                [sg.Radio('Listar todos os filmes indicados', "RD1", key='1')],
                [sg.Radio('Listar filmes indicados por ano', "RD1", key='2')],
                [sg.Radio('Listar filmes indicados por categoria', "RD1", key='3')],
                [sg.Radio('Menu de indicação de filmes', "RD1", key='0')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]

            window = sg.Window('Relatório de Indicações', layout)
            button, values = window.read()
            window.close()

            if button in (None, 'Cancelar'):
                return None

            if values.get('1'):
                return 1
            elif values.get('2'):
                return 2
            elif values.get('3'):
                return 3
            elif values.get('0'):
                return 0
            else:
                sg.popup('Erro! Selecione uma das opções válidas: 0, 1 ou 2.')

    def pegar_dados_filme(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("=============== DADOS FILME ===============", font=("Helvetica", 25))],
            [sg.Text('Título:', size=(15, 1)), sg.InputText('', key='titulo')],
            [sg.Text('Sinopse:', size=(15, 1)), sg.InputText('', key='sinopse')],
            [sg.Text('Categoria:', size=(15, 1)), sg.InputText('', key='categoria')],
            [sg.Text('Ano de indicação:', size=(15, 1)), sg.InputText('', key='ano_indicacao')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Sistema do Oscar', layout)
        
        event, values = self.open()
        self.close()

        if event == 'Confirmar':
            titulo = values['titulo']
            sinopse = values['sinopse']
            categoria = values['categoria']
            ano = values['ano_indicacao']
            resultado = {"titulo": titulo, "sinopse": sinopse, "categoria": categoria, "ano_indicacao": ano}
        else:
            resultado = None
        
        self.close()
        return resultado

    def mostrar_dados_filme(self, dados_filme):
        string_todos_filmes = ""
        for dado in dados_filme:
            string_todos_filmes += "FILME: " + str(dado["titulo"]) + '\n'
            string_todos_filmes += "SINOPSE: " + str(dado["sinopse"]) + '\n'
            string_todos_filmes += "CATEGORIA: " + str(dado["categoria"]) + '\n'
            string_todos_filmes += "ANO DE INDICAÇÃO: " + str(dado["ano_indicacao"]) + '\n\n'

        sg.popup("=============== LISTA DE FILMES ===============", string_todos_filmes)

    def buscar_filme_por_titulo(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- BUSCAR FILME ----------', font=("Helvetica", 25))],
            [sg.Text('Titulo do Filme:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Buscar Filme', layout)
        button, values = self.open()
        self.close()

        if button == 'Confirmar':
            nome = values.get('nome', '').strip().title()
            if nome == '':
                sg.popup('Erro! O nome não pode ficar vazio.')
                return None
            return nome
        return None

    def buscar_indicados_por_ano(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("=============== SELECIONAR INDICADOS ===============", font=("Helvetica", 25))],
            [sg.Text('Digite o ano que deseja selecionar: ', font=("Helvetica", 15))],
            [sg.Text('ANO:', size=(15, 1)), sg.InputText('', key='ano')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona ano', layout)

        event, values = self.__window.read()
        ano = values['ano'] if event == 'Confirmar' else None
        self.close()
        return ano
    
    def buscar_indicados_por_categoria(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("=============== SELECIONAR INDICADOS ===============", font=("Helvetica", 25))],
            [sg.Text('Digite a categoria que deseja selecionar: ', font=("Helvetica", 15))],
            [sg.Text('CATEGORIA:', size=(15, 1)), sg.InputText('', key='categoria')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona categoria', layout)

        event, values = self.__window.read()
        categoria = values['categoria'] if event == 'Confirmar' else None
        self.close()
        return categoria
    
    def mostrar_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.close()

    def open(self):
        return self.__window.read()
