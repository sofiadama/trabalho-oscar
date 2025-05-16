from abc import ABC, abstractmethod

class ControladorVoto(ABC):
    @abstractmethod
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__votos = {} # dicionario que armazena os votos por membro
    
    @abstractmethod
    def verificar_duplicidade_voto():
        # criar uma lista de votos para cada membro
        # para ator e diretor: o voto nao pode conter o "ano" duplicado
        # para filme: o voto nao pode conter a "categoria" duplicada
        pass

    @abstractmethod
    def adicionar_voto():
        pass

    @abstractmethod
    def alterar_voto():
        pass

    @abstractmethod
    def listar_votos():
        pass

    @abstractmethod
    def remover_voto():
        pass

