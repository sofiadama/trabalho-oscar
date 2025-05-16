from tela.tela_sistema import TelaSistema
from controle.controlador_membro import ControladorMembro
from controle.controlador_ator import ControladorAtor
# filme
# diretor
from controle.controlador_categoria import ControladorCategoria
from controle.controlador_voto import ControladorVoto


class ControladorSistema:

    def __init__(self):
        self.__controlador_membro = ControladorMembro(self)
        self.__controlador_ator = ControladorAtor(self)
        # filme
        # diretor
        self.__controlador_categoria = ControladorCategoria(self)
        self.__controlador_voto = ControladorVoto(self)
    
    @property
    def controlador_membro(self):
        return self.__controlador_membro
    
    @property
    def controlador_ator(self):
        return self.__controlador_ator
    
    @property
    def controlador_categoria(self):
        return self.__controlador_categoria
    
    @property
    def controlador_voto(self):
        return self.__controlador_voto
    
    def iniciar_sistema(self):
        self.__abrir_tela_principal()
    
    def cadastros(self):
        self.__abrir_tela_cadastros()
    
    def indicacoes(self):
        self.__abrir_tela_indicacoes()

    def votos(self):
        self.__abrir_tela_votos()    
    
    def cadastro_membro(self):
        self.__controlador_membro.abrir_tela_cadastros()

    def cadastro_categoria(self):
        self.__controlador_categoria.abrir_tela_cadastros()

    def indicacao_ator(self):
        self.__controlador_ator.abrir_tela_indicacoes()
    
    def indicacao_diretor(self):
        self.__controlador_diretor.abrir_tela_indicacoes()

    def indicacao_filme(self):
        self.__controlador_filme.abrir_tela_indicacoes()

    def voto_ator(self):
        self.__controlador_voto.abrir_tela_votos()

    def voto_diretor(self):
        self.__controlador_voto.abrir_tela_votos()

    def voto_filme(self):
        self.__controlador_voto.abrir_tela_votos()
    
    def retornar_menu(self):
        self.__abrir_tela_principal()
    
    def encerrar_sistema(self):
        exit(0)

    def abrir_tela_principal(self):
        lista_opcoes = {1: self.cadastros, 2: self.indicacoes, 3: self.votos,
                        0: self.retornar_menu}
    
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_principais()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def abrir_tela_cadastros(self):
        lista_opcoes = {1: self.cadastro_membro, 2: self.cadastro_categoria,
                        0: self.retornar_menu}
        
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_cadastros()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
    
    def abrir_tela_indicacoes(self):
        lista_opcoes = {1: self.indicacao_ator, 2: self.indicacao_diretor, 3: self.indicacao_filme,
                        0: self.retornar_menu}
        
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_indicacoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
        
    def abrir_tela_votos(self):
        lista_opcoes = {1: self.voto_ator, 2: self.voto_diretor, 3: self.voto_filme,
                        0: self.retornar_menu}
        
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_votos()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
    
    
    
    
