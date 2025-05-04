from tela_diretor import TelaDiretor
from diretor import Diretor


class ControladorDiretor:
    def __init__(self):
        self.__tela_diretor = TelaDiretor(self)
        self.__diretores = []

    def inicia(self):
        self.abre_tela_inicial()

    def inclui_diretor(self):
        dados = self.__tela_diretor.pega_dados_diretor()
        diretor = Diretor(id, nome, data_de_nascimento, nacionalidade)
        self.__diretores.append(diretor)
        self.__tela_diretor.mostra_mensagem("Diretor incluído com sucesso!")

    def altera_diretor(self):
        cpf = self.__tela_diretor.pega_cpf()
        for diretor in self.__diretores:
            if diretor["cpf"] == cpf:
                novos_dados = self.__tela_diretor.pega_dados_diretor()
                diretor["nome"] = novos_dados["nome"]
                diretor["cpf"] = novos_dados["cpf"]
                self.__tela_diretor.mostra_mensagem("Diretor alterado com sucesso!")
                return
        self.__tela_diretor.mostra_mensagem("Diretor não encontrado.")

    def exclui_diretor(self):
        cpf = self.__tela_diretor.pega_cpf()
        for diretor in self.__diretores:
            if diretor["cpf"] == cpf:
                self.__diretores.remove(diretor)
                self.__tela_diretor.mostra_mensagem("Diretor excluído com sucesso!")
                return
        self.__tela_diretor.mostra_mensagem("Diretor não encontrado.")

    def lista_diretor(self):
        self.__tela_diretor.mostra_diretores(self.__diretores)

    def finalizar(self):
        self.__tela_diretor.mostra_mensagem("Encerrando...")
        exit()

    def abre_tela_inicial(self):
        switcher = {
            0: self.finalizar,
            1: self.inclui_diretor,
            2: self.altera_diretor,
            3: self.exclui_diretor,
            4: self.lista_diretor
        }
        
        while True:
            opcao = self.__tela_diretor.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_diretor.mostra_mensagem("Opção inválida.")

