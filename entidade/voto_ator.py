from voto import Voto
from ator import Ator
from membro import Membro


class VotoAtor(Voto):
  def __init__(self, membro: Membro, indicado: Ator, ano: int):
    super().__init__(membro, indicado, ano)
