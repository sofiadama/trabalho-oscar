from abc import ABC, abstractmethod
from entidade.filme import Filme
from entidade.categoria import Categoria

class Indicado(ABC):
    @abstractmethod
    def __init__(self, nome: str, nacionalidade: str, categoria: Categoria, filme: Filme, ano_indicacao: int):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__categoria = categoria
        self.__filme = filme
        self.__ano_indicacao = ano_indicacao

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nacionalidade(self):
        return self.__nacionalidade
    
    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade
    
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @property
    def filme(self):
        return self.__filme
    
    @filme.setter
    def filme(self, filme):
        self.__filme = filme
    
    @property
    def ano_indicacao(self):
        return self.__ano_indicacao
    
    @ano_indicacao.setter
    def ano_indicacao(self, ano_indicacao):
        self.__ano_indicacao = ano_indicacao