from entidade.voto import Voto
from entidade.membro import Membro
from entidade.ator import Ator
from entidade.categoria import Categoria

class VotoAtor(Voto):
  def __init__(self, membro: Membro, indicado: Ator, categoria: Categoria, ano: int):
    super().__init__(membro, indicado, categoria, ano)