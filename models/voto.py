from membroAcademia import MembroAcademia

class Voto:
  def __init__(self, id: int, membro: MembroAcademia, indicado: Indicacao, ano_de_indicacao: int):
    self.__id = id
    self.__membro = membro
    self.__indicado = indicado
    self.__ano_de_indicacao = ano_de_indicacao

  @property
  def id(self):
    return self.__id

  @id.setter
  def id(self, id):
    self.__id = id

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
  def ano_de_indicacao(self):
    return self.__ano_de_indicacao

  @indicacao.setter
  def ano_de_indicacao(self, ano_de_indicacao):
    self.__ano_de_indicacao = ano_de_indicacao
