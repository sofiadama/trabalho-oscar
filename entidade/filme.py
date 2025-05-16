from entidade.diretor import Diretor
from entidade.categoria import Categoria

class Filme():
    def __init__(self, titulo: str, diretor: Diretor, categoria: Categoria):
        self.__titulo = titulo
        self.__diretor = diretor
        self.__categoria = categoria
    
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
    
    @property
    def diretor(self):
        return self.__diretor

    @diretor.setter
    def diretor(self, diretor):
        self.__diretor = diretor

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria