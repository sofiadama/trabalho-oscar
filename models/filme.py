from diretor import Diretor
from ator import Ator
from categoria import Categoria

class Filme:
    def __init__(self, titulo: str, ano: int, diretor: Diretor, ator: Ator, categoria: Categoria):
        self.__titulo = titulo
        self.__ano_de_lancamento = ano_de_lancamento
        self.__diretor = diretor
        self.__ator = ator
        self.__categoria = categoria
    
    @property
    def titulo(self):
      return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
      self.__titulo = titulo

    @property
    def ano_de_lancamento(self):
      return self.__ano_de_lancamento

    @ano_de_lancamento.setter
    def ano_de_lancamento(self, ano_de_lancamento):
      self.__ano_de_lancamento = ano_de_lancamento
      
    @property
    def diretor(self):
      return self.__diretor

    @diretor.setter
    def diretor(self, diretor):
      self.__diretor = diretor

    @property
    def ator(self):
      return self.__ator

    @ator.setter
    def ator(self, ator):
      self.__ator = ator

    @property
    def categoria(self):
      return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
      self.__categoria = categoria
