from abc import ABC, abstractmethod
from entidade.categoria import Categoria
from entidade.filme import Filme

class Indicado(ABC):
    @abstractmethod
    def __init__(self, nome: str, nacionalidade: str, categoria: Categoria, filme: Filme, ano_indicacao: int):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__categoria = categoria
        self.__filme = filme
        self.__ano_indicacao = ano_indicacao

    @property
    def nome(self) -> str: 
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str):
            raise TypeError("Nome inválido.")
        self.__nome = nome

    @property
    def nacionalidade(self) -> str:
        return self.__nacionalidade
    
    @nacionalidade.setter
    def nacionalidade(self, nacionalidade: str):
        if not isinstance(nacionalidade, str):
            raise TypeError("Nacionalidade inválida.")
        self.__nacionalidade = nacionalidade
    
    @property
    def categoria(self) -> Categoria:
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria: Categoria):
        if not isinstance(categoria, Categoria):
            raise TypeError("Categoria inválida.")
        self.__categoria = categoria

    @property
    def filme(self) -> Filme:
        return self.__filme
    
    @filme.setter
    def filme(self, filme: Filme):
        if not isinstance(filme, Filme):
            raise TypeError("Filme inválido.")
        self.__filme = filme
    
    @property
    def ano_indicacao(self) -> int:
        return self.__ano_indicacao
    
    @ano_indicacao.setter
    def ano_indicacao(self, ano_indicacao: int):
        if not isinstance(ano_indicacao, int):
            raise TypeError("Ano de indicação inválido.")
        self.__ano_indicacao = ano_indicacao