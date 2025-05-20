from tela.tela_sistema import TelaSistema
from tela.tela_voto import TelaVoto
from controle.controlador_ator import ControladorAtor
from controle.controlador_diretor import ControladorDiretor
from controle.controlador_filme import ControladorFilme
from controle.controlador_membro import ControladorMembro
from controle.controlador_categoria import ControladorCategoria
from controle.controlador_voto import ControladorVoto
from controle.controlador_voto_ator import ControladorVotoAtor
from controle.controlador_voto_diretor import ControladorVotoDiretor
from controle.controlador_voto_filme import ControladorVotoFilme

class ControladorSistema:

    def __init__(self):
        self.__controlador_ator = ControladorAtor(self)
        self.__controlador_diretor = ControladorDiretor(self)
        self.__controlador_filme = ControladorFilme(self)
        self.__controlador_membro = ControladorMembro(self)
        self.__controlador_categoria = ControladorCategoria(self)
        self.__controlador_voto = ControladorVoto(self)
        self.__controlador_voto_ator = ControladorVotoAtor(self)
        self.__controlador_voto_diretor = ControladorVotoDiretor(self)
        self.__controlador_voto_filme = ControladorVotoFilme(self)
        self.__tela_voto = TelaVoto()
        self.__tela_sistema = TelaSistema()
    
    @property
    def controlador_ator(self):
        return self.__controlador_ator
    
    @property
    def controlador_diretor(self):
        return self.__controlador_diretor
    
    @property
    def controlador_filme(self):
        return self.__controlador_filme
    
    @property
    def controlador_membro(self):
        return self.__controlador_membro
    
    @property
    def controlador_categoria(self):
        return self.__controlador_categoria
    
    @property
    def controlador_voto(self):
        return self.__controlador_voto
    
    @property
    def controlador_voto_ator(self):
        return self.__controlador_voto_ator
    
    @property
    def controlador_voto_diretor(self):
        return self.__controlador_voto_diretor
    
    @property
    def controlador_voto_filme(self):
        return self.__controlador_voto_filme
    
    def iniciar_sistema(self):
        self.abrir_tela_principal()
    
    def cadastros(self):
        self.abrir_tela_cadastros()
    
    def indicacoes(self):
        self.abrir_tela_indicacoes()
    
    def votos(self):
        self.abrir_tela_votos()

    def cadastro_membro(self):
        self.controlador_membro.abrir_tela_membro()
    
    def cadastro_categoria(self):
        self.controlador_categoria.abrir_tela_categoria()

    def cadastro_voto(self):
        self.escolher_tipo_indicado()

    def indicacao_ator(self):
        self.__controlador_ator.abrir_tela_ator()

    def indicacao_diretor(self):
        self.__controlador_diretor.abrir_tela_diretor()
    
    def indicacao_filme(self):
        self.__controlador_filme.abrir_tela_filme()
    
    def encerrar_sistema(self):
        exit(0)

    def abrir_tela_principal(self):
        lista_opcoes = {
            1: self.cadastros,
            2: self.indicacoes,
            3: self.votos,
            0: self.encerrar_sistema
        }
    
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_principais()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
    
    def abrir_tela_cadastros(self):
        lista_opcoes = {
            1: self.cadastro_membro,
            2: self.cadastro_categoria,
            0: self.abrir_tela_principal
        }
        
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_cadastros()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
    
    def abrir_tela_indicacoes(self):
        lista_opcoes = {
            1: self.indicacao_ator,
            2: self.indicacao_diretor,
            3: self.indicacao_filme,
            0: self.abrir_tela_principal
        }
        
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_indicacoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            if funcao_escolhida is None:
                break
            funcao_escolhida()
    
    def abrir_tela_votos(self):
        lista_opcoes = {
            1: self.escolher_tipo_indicado, 
            2: self.controlador_voto.listar_votos_gerais,
            0: self.abrir_tela_principal
        }
    
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_votos()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            if funcao_escolhida is None:
                break
            funcao_escolhida()

    def escolher_tipo_indicado(self):
        if self.__controlador_voto.membro_autenticado is None:
            if not self.controlador_voto.autenticar_membro():
                return

        lista_opcoes = {
            1: self.__controlador_voto_ator.abrir_tela_voto_ator, 
            2: self.__controlador_voto_diretor.abrir_tela_voto_diretor, 
            3: self.__controlador_voto_filme.abrir_tela_voto_filme,
            0: None
        }
    
        while True:
            opcao_escolhida = self.__tela_voto.tela_tipo_indicados()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            if funcao_escolhida is None:
                break
            funcao_escolhida()
    
