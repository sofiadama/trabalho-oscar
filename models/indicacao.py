from ator import Ator
from diretor import Diretor
from filme import Filme
from categoria import Categoria

class Indicacao:
  def __init__(self, ator: Ator, diretor: Diretor, filme: Filme, categoria: Categoria):
    self.__ator = ator
    self.__diretor = diretor
    self.__filme = filme
    self.__categoria = categoria

  @property
  def ator(self):
    return self.__ator

  @ator.setter
  def ator(self, ator):
    self.__ator = ator

  @property 
  def diretor(self):
    return self.__diretor

  @diretor.setter
  def diretor(self, diretor):
    self.__diretor = diretor

  @property
  def filme(self):
    return self.__filme

  @filme.setter
  def filme(self, filme):
    self.__filme = filme

  @property
  def categoria(self):
    return self.__categoria

  @categoria.setter
  def categoria(self, categoria):
    self.__categoria = categoria
    


  
