from voto import Voto
from filme import Filme
from membro import Membro


class VotoAtor(Voto):
  def __init__(self, membro: Membro, indicado: Filme, ano: int):
    super().__init__(membro, indicado, ano)

# escolher categoria