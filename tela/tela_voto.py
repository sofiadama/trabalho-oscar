import PySimpleGUI as sg

class TelaVoto:
    def __init__(self):
        self.__window = None
        
    def tela_filtros_de_relatorios(self):
        self.init_opcoes_filtros()
        event, values = self.__window.read()
        opcao = 0
        
        if event in (sg.WIN_CLOSED, 'Cancelar', None):
            opcao = 0
        elif values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        elif values['0']:
            opcao = 0
            
        self.close()
        return opcao
    
    def init_opcoes_filtros(self):
        sg.theme('DarkTeal4') 
        layout = [
            [sg.Text("=============== FILTROS ===============", font=("Helvetica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvetica", 15))],
            [sg.Radio('Listar Votos', "RD1", key='1')],
            [sg.Radio('Listar Vencedores Por Ano', "RD1", key='2')],
            [sg.Radio('Listar Vencedores Por Categoria', "RD1", key='3')],
            [sg.Radio('Listar Filmes Mais Premiados', "RD1", key='4')],
            [sg.Radio('Menu de Votos', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]  
        ]
        self.__window = sg.Window('Sistema de votos', layout) 
    
    def tela_tipos_de_votos(self):
        self.init_opcoes_votos()
        event, values = self.__window.read()
        opcao = 0
        
        if event in (sg.WIN_CLOSED, 'Cancelar', None):
            opcao = 0
        elif values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['0']:
            opcao = 0
            
        self.close()
        return opcao
    
    def init_opcoes_votos(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("=============== VOTOS ===============", font=("Helvetica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvetica", 15))],
            [sg.Radio('Votos em Atores', "RD1", key='1')],
            [sg.Radio('Votos em Diretores', "RD1", key='2')],
            [sg.Radio('Votos em Filmes', "RD1", key='3')],
            [sg.Radio('Menu de Votos', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de votos', layout)
    
    def autenticacao_membro(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("=============== AUTENTICAÇÃO ===============", font=("Helvetica", 25))],
            [sg.Text('Digite o ID para autenticar: ', font=("Helvetica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='membro')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de votos', layout)

        event, values = self.__window.read()
        membro = values['membro'] if event == 'Confirmar' else None
        self.close()
        return membro
    
    def pegar_dados_voto(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("=============== DADOS VOTO ===============", font=("Helvetica", 25))],
            [sg.Text('Indicado:', size=(15, 1)), sg.InputText('', key='indicado')],
            [sg.Text('Categoria:', size=(15, 1)), sg.InputText('', key='categoria')],
            [sg.Text('Ano:', size=(15, 1)), sg.InputText('', key='ano')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de votos', layout)

        event, values = self.__window.read()
        
        if event == 'Confirmar':
            indicado = values['indicado']
            categoria = values['categoria']
            ano = values['ano']
            resultado = {"indicado": indicado, "categoria": categoria, "ano": ano}
        else:
            resultado = None

        self.close()
        return resultado
    
    def mostrar_dados_voto(self, dados_voto):
        string_todos_votos = ""
        for dado in dados_voto:
            string_todos_votos += "MEMBRO: " + str(dado["membro"]) + '\n'
            string_todos_votos += "INDICADO: " + str(dado["indicado"]) + '\n'
            string_todos_votos += "CATEGORIA: " + str(dado["categoria"]) + '\n'
            string_todos_votos += "ANO DE INDICAÇÃO: " + str(dado["ano"]) + '\n\n'

        sg.popup("=============== LISTA DE VOTOS ===============", string_todos_votos)

    def buscar_voto_por_ano(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("=============== SELECIONAR VOTO ===============", font=("Helvetica", 25))],
            [sg.Text('Digite o ano que deseja selecionar: ', font=("Helvetica", 15))],
            [sg.Text('ANO:', size=(15, 1)), sg.InputText('', key='ano')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona ano', layout)

        event, values = self.__window.read()
        ano = values['ano'] if event == 'Confirmar' else None
        self.close()
        return ano

    def buscar_voto_por_categoria(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("=============== SELECIONAR VOTO ===============", font=("Helvetica", 25))],
            [sg.Text('Digite a categoria que deseja selecionar: ', font=("Helvetica", 15))],
            [sg.Text('CATEGORIA:', size=(15, 1)), sg.InputText('', key='categoria')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona categoria', layout)

        event, values = self.__window.read()
        categoria = values['categoria'] if event == 'Confirmar' else None
        self.close()
        return categoria
    
    def buscar_vencedor_por_ano(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("=============== SELECIONAR VENCEDOR ===============", font=("Helvetica", 25))],
            [sg.Text('Digite o ano que deseja selecionar: ', font=("Helvetica", 15))],
            [sg.Text('ANO:', size=(15, 1)), sg.InputText('', key='ano')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona ano', layout)

        event, values = self.__window.read()
        ano = values['ano'] if event == 'Confirmar' else None
        self.close()
        return ano
    
    def buscar_vencedor_por_categoria(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("=============== SELECIONAR VENCEDOR ===============", font=("Helvetica", 25))],
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
        if self.__window:
            self.__window.close()

    def open(self):
        event, values = self.__window.read()
        return event, values