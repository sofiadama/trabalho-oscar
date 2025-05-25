from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from entidade.membro import Membro
from entidade.categoria import Categoria

Tipo = TypeVar("Tipo")

class Voto(ABC, Generic[Tipo]):
    @abstractmethod
    def __init__(self, membro: Membro, indicado: Tipo, categoria: Categoria, ano: int):
      self.__membro = membro
      self.__indicado = indicado
      self.__categoria = categoria
      self.__ano = ano

    @property
    def membro(self) -> Membro:
      return self.__membro

    @membro.setter
    def membro(self, membro: Membro):
      if not isinstance(membro, Membro):
        raise TypeError("Membro inválido.")
      self.__membro = membro

    @property
    def indicado(self): 
      return self.__indicado

    @indicado.setter
    def indicado(self, indicado: Tipo):
      self.__indicado = indicado

    @property
    def categoria(self) -> Categoria: 
      return self.__categoria

    @categoria.setter
    def categoria(self, categoria: Categoria):
      if not isinstance(categoria, Categoria):
        raise TypeError("Categoria inválida.")
      self.__categoria = categoria

    @property
    def ano(self) -> int:
      return self.__ano

    @ano.setter
    def ano(self, ano: int):
      if not isinstance(ano, int):
        raise TypeError("Ano de votação inválido.")
      self.__ano = ano
