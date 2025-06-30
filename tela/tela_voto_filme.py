import PySimpleGUI as sg

class TelaVotoFilme:
    def __init__(self):
        self.__window = None
    
    def tela_votos_em_filmes(self):
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
        elif values['4']:
            opcao = 4 
        elif values['0']:
            opcao = 0
        
        self.close()
        return opcao
    
    def init_opcoes_votos(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("=========== VOTOS EM FILMES ===========", font=("Helvetica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvetica", 15))],
            [sg.Radio('Adicionar Voto', "RD1", key='1')],
            [sg.Radio('Alterar Voto', "RD1", key='2')],
            [sg.Radio('Listar Votos', "RD1", key='3')],
            [sg.Radio('Excluir Voto', "RD1", key='4')],
            [sg.Radio('Menu de Votos', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de votos', layout)

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
        elif values['0']:
            opcao = 0
            
        self.close()
        return opcao
        
    def init_opcoes_filtros(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("=============== FILTROS ===============", font=("Helvetica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvetica", 15))],
            [sg.Radio('Listar Votos Gerais', "RD1", key='1')],
            [sg.Radio('Listar Votos Por Ano', "RD1", key='2')],
            [sg.Radio('Listar Votos Por Categoria', "RD1", key='3')],
            [sg.Radio('Menu de Votos em Filmes', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de votos', layout)
        
    def mostrar_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        if self.__window:
            self.__window.close()

    def open(self):
        event, values = self.__window.read()
        return event, values