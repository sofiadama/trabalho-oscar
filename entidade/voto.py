from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from membro import Membro

Tipo = TypeVar("Tipo")

class Voto(Generic[Tipo]):
  @abstractmethod
  def __init__(self, membro: Membro, indicado: Tipo, ano: int):
      self.__membro = membro
      self.__indicado = indicado
      self.__ano = ano

  @property
  def membro(self):
    return self.__membro

  @membro.setter
  def membro(self, membro):
    self.__membro = membro

  @property
  def indicado(self): 
    return self.__indicado

  @indicado.setter
  def indicado(self, indicado):
    self.__indicado = indicado

  @property
  def ano(self):
    return self.__ano

  @ano.setter
  def ano(self, ano):
    self.__ano = ano
