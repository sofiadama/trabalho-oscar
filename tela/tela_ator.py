import PySimpleGUI as sg

class TelaAtor():      
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
            [sg.Text('-------- ATORES ----------', font=("Helvetica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvetica", 15))],
            [sg.Radio('Incluir Ator', "RD1", key='1')],
            [sg.Radio('Alterar Ator', "RD1", key='2')],
            [sg.Radio('Listar Ator', "RD1", key='3')],
            [sg.Radio('Excluir Ator', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema do Oscar', layout)

    def tela_filtros_de_relatorios(self):
        while True:
            layout = [
                [sg.Text('-------- RELATÓRIO DE INDICAÇÕES ----------', font=('Helvetica', 20))],
                [sg.Text('Escolha uma opção:', font=('Helvetica', 14))],
                [sg.Radio('Listar todos os atores indicados', "RD1", key='1')],
                [sg.Radio('Listar atores indicados por ano', "RD1", key='2')],
                [sg.Radio('Menu de indicação de atores', "RD1", key='0')],
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
            elif values.get('0'):
                return 0
            else:
                sg.popup('Erro! Selecione uma das opções válidas: 0, 1 ou 2.')

    def pegar_dados_ator(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS ATOR ----------', font=("Helvetica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Nacionalidade:', size=(15, 1)), sg.InputText('', key='nacionalidade')],
            [sg.Text('Categoria:', size=(15, 1)), sg.InputText('Melhor Ator', key='categoria')],
            [sg.Text('Título do Filme:', size=(15, 1)), sg.InputText('', key='titulo_filme')],
            [sg.Text('Ano de Indicação (2020-2025):', size=(25, 1)), sg.InputText('', key='ano')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema do Oscar', layout)
        button, values = self.open()
        self.close()

        if button == 'Confirmar':
            nome = values.get('nome', '').strip().title()
            nacionalidade = values.get('nacionalidade', '').strip().capitalize()
            categoria = values.get('categoria', '').strip().title()
            titulo_filme = values.get('titulo_filme', '').strip().title()
            try:
                ano = int(values.get('ano', ''))
                if ano not in range(2020, 2026):
                    raise ValueError
            except ValueError:
                sg.popup("Erro! Ano inválido. Deve estar entre 2020 e 2025.")
                return None

            if not nome or not nacionalidade or not titulo_filme:
                sg.popup("Erro: Todos os campos devem ser preenchidos.")
                return None

            return {
                "nome": nome,
                "nacionalidade": nacionalidade,
                "categoria": categoria,
                "titulo_filme": titulo_filme,
                "ano_indicacao": ano
            }
        else:
            return None

    def mostrar_ator(self, dados_ator):
        string_todos_atores = ""
        for dado in dados_ator:
            string_todos_atores += f"NOME DO ATOR: {dado['nome']}\n"
            string_todos_atores += f"NACIONALIDADE: {dado['nacionalidade']}\n"
            string_todos_atores += f"CATEGORIA: {dado['categoria']}\n"
            string_todos_atores += f"TÍTULO DO FILME: {dado['titulo_filme']}\n"
            string_todos_atores += f"ANO DE INDICAÇÃO: {dado['ano_indicacao']}\n\n"

        sg.popup('-------- LISTA DE ATORES ----------', string_todos_atores)

    def buscar_ator_por_nome(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- BUSCAR ATOR ----------', font=("Helvetica", 25))],
            [sg.Text('Nome do Ator:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Buscar Ator', layout)
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

    def mostrar_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.close()

    def open(self):
        return self.__window.read()