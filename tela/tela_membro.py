import PySimpleGUI as sg

class TelaMembro():
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        self.init_opcoes()
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

    def init_opcoes(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('=========== MEMBROS ===========', font=("Helvetica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvetica", 15))],
            [sg.Radio('Incluir Membro', "RD1", key='1')],
            [sg.Radio('Alterar Membro', "RD1", key='2')],
            [sg.Radio('Listar Membro', "RD1", key='3')],
            [sg.Radio('Excluir Membro', "RD1", key='4')],
            [sg.Radio('Menu de Cadastros', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Sistema do Oscar', layout)

    def pegar_dados_membro(self):
        sg.theme('DarkTeal4')        
        layout = [
            [sg.Text('-------- DADOS MEMBRO ----------', font=("Helvetica", 25))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Text('NOME:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('NASCIMENTO:', size=(15, 1)), sg.InputText('', key='nascimento')],
            [sg.Text('NACIONALIDADE:', size=(15, 1)), sg.InputText('', key='nacionalidade')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de votos', layout)

        event, values = self.__window.read()
        
        if event == 'Confirmar':
            id = values['id']
            nome = values['nome']
            nascimento = values['nascimento']
            nacionalidade = values['nacionalidade']
            resultado = {"id": id, "nome": nome, "nascimento": nascimento, "nacionalidade": nacionalidade}
        else:
            resultado = None

        self.close()
        return resultado
        
    def mostrar_dados_membro(self, dados_membro):
        string_todos_membros = ""
        for dado in dados_membro:
            string_todos_membros += "ID: " + str(dado['id']) + '\n'
            string_todos_membros += "NOME: " + str(dado["nome"]) + '\n'
            string_todos_membros += "NASCIMENTO: " + str(dado["nascimento"]) + '\n'
            string_todos_membros += "NACIONALIDADE: " + str(dado["nacionalidade"]) + '\n\n'
            
        sg.popup("=============== LISTA DE MEMBROS ===============", string_todos_membros)

    def selecionar_membro(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text("=============== SELECIONAR MEMBRO ===============", font=("Helvetica", 25))],
            [sg.Text('Digite o ID do membro que deseja selecionar:', font=("Helvetica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar membro', layout)

        event, values = self.__window.read()
        
        # CORRIGIDO: Melhor validação e conversão
        if event == 'Confirmar':
            id_val = values.get('id', '').strip()
            if not id_val:
                self.close()
                sg.popup("Erro", "O ID não pode ficar vazio!")
                return None
            self.close()
            return id_val
        else:
            self.close()
            return None
        
    def mostrar_mensagem(self, msg):
        sg.popup("", msg)
    
    def close(self):
        if self.__window:
            self.__window.close()

    def open(self):
        event, values = self.__window.read()
        return event, values
