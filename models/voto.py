from abc import ABC, abstractmethod
from membroAcademia import MembroAcademia

class Voto(ABC):
  @abstractmethod
  def __init__(self, membro: MembroAcademia):
    self.__membro = membro

  @property
  @abstractmethod
  def membro(self):
    return self.__membro

  @abstractmethod
  def inclui_voto():
    pass

  @abstractmethod
  def exclui_voto():
    pass

  @abstractmethod
  def altera_voto():
    pass

  @abstractmethod
  def lista_voto():
    pass
