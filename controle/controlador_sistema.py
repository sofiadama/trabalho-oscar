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
        self.abrir_menu_principal()
    
    def acessar_cadastros(self):
        self.abrir_submenu_cadastros()
    
    def acessar_indicacoes(self):
        self.abrir_submenu_indicacoes()
    
    def acessar_votos(self):
        self.abrir_submenu_votos()

    def cadastro_membro(self):
        self.controlador_membro.abrir_tela_membro()
    
    def cadastro_categoria(self):
        self.controlador_categoria.abrir_tela_categoria()

    def indicacao_ator(self):
        self.__controlador_ator.abrir_tela_ator()

    def indicacao_diretor(self):
        self.__controlador_diretor.abrir_tela_diretor()
    
    def indicacao_filme(self):
        self.__controlador_filme.abrir_tela_filme()
    
    def registro_voto(self):
        self.__controlador_voto.autenticar_membro()

    def encerrar_sistema(self):
        exit(0)

    def excecao_opcao_errada(self, lista_opcoes, funcao_tela, opcoes_validas = None):
        while True:
            try:
                opcao_escolhida = funcao_tela()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
                return
            except KeyError:
                print("Opção inválida!")
                if opcoes_validas:
                    print("Opções válidas: ", opcoes_validas)
    
    def abrir_menu_principal(self):
        lista_opcoes = {
            1: self.acessar_cadastros,
            2: self.acessar_indicacoes,
            3: self.acessar_votos,
            0: self.encerrar_sistema
        }
        
        self.excecao_opcao_errada(
            lista_opcoes,
            self.__tela_sistema.tela_opcoes_principais,
            [0,1,2,3]
        )
                     
    def abrir_submenu_cadastros(self):
        lista_opcoes = {
            1: self.cadastro_membro,
            2: self.cadastro_categoria,
            0: self.abrir_menu_principal
        }
        
        self.excecao_opcao_errada(
            lista_opcoes,
            self.__tela_sistema.tela_opcoes_cadastros,
            [0,1,2]
        )
    
    def abrir_submenu_indicacoes(self):
        lista_opcoes = {
            1: self.indicacao_ator,
            2: self.indicacao_diretor,
            3: self.indicacao_filme,
            0: self.abrir_menu_principal
        }
        
        self.excecao_opcao_errada(
            lista_opcoes,
            self.__tela_sistema.tela_opcoes_indicacoes,
            [0,1,2,3]
        )
    
    def abrir_submenu_votos(self):
        lista_opcoes = {
            1: self.controlador_voto.autenticar_membro, 
            2: self.controlador_voto.abrir_filtro_vencedores,
            0: self.abrir_menu_principal
        }
    
        self.excecao_opcao_errada(
            lista_opcoes,
            self.__tela_sistema.tela_opcoes_votos,
            [0,1,2]
        )

    def escolher_tipo_de_voto(self):
        lista_opcoes = {
            1: self.__controlador_voto_ator.abrir_tela_voto_ator, 
            2: self.__controlador_voto_diretor.abrir_tela_voto_diretor, 
            3: self.__controlador_voto_filme.abrir_tela_voto_filme,
            0: self.abrir_submenu_votos
        }

        self.excecao_opcao_errada(
            lista_opcoes,
            self.__tela_voto.tela_tipos_de_votos,
            [0,1,2,3]
        )