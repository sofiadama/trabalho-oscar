import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None

    def tela_opcoes_principais(self):
        self.init_opcoes_principais()
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
    
    def init_opcoes_principais(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("========= SISTEMA DE VOTAÇÕES =========", font=("Helvetica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvetica", 15))],
            [sg.Radio('Cadastros', "RD1", key='1')],
            [sg.Radio('Indicações', "RD1", key='2')],
            [sg.Radio('Votações', "RD1", key='3')],
            [sg.Radio('Sair', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de votos', layout)

    def tela_opcoes_cadastros(self):
        self.init_opcoes_cadastros()
        event, values = self.__window.read()
        opcao = 0
        
        if event in (sg.WIN_CLOSED, 'Cancelar', None):
            opcao = 0
        elif values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['0']:
            opcao = 0
            
        self.close()
        return opcao
    
    def init_opcoes_cadastros(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("=========== CADASTROS ===========", font=("Helvetica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvetica", 15))],
            [sg.Radio('Cadastro de Membros', "RD1", key='1')],
            [sg.Radio('Cadastro de Categorias', "RD1", key='2')],
            [sg.Radio('Menu Principal', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de votos', layout)

    def tela_opcoes_indicacoes(self):
        self.init_opcoes_indicacoes()
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
    
    def init_opcoes_indicacoes(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("=========== INDICAÇÕES ===========", font=("Helvetica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvetica", 15))],
            [sg.Radio('Indicações de Atores', "RD1", key='1')],
            [sg.Radio('Indicações de Diretores', "RD1", key='2')],
            [sg.Radio('Indicações de Filmes', "RD1", key='3')],
            [sg.Radio('Menu Principal', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de votos', layout)

    def tela_opcoes_votos(self):
        self.init_opcoes_votos()
        event, values = self.__window.read()
        opcao = 0
        
        if event in (sg.WIN_CLOSED, 'Cancelar', None):
            opcao = 0
        elif values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['0']:
            opcao = 0
            
        self.close()
        return opcao
    
    def init_opcoes_votos(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("=========== VOTOS ===========", font=("Helvetica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvetica", 15))],
            [sg.Radio('Votações', "RD1", key='1')],
            [sg.Radio('Relatórios', "RD1", key='2')],
            [sg.Radio('Menu Principal', "RD1", key='0')],
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