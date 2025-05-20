from entidade.voto import Voto
from entidade.membro import Membro
from entidade.filme import Filme
from entidade.categoria import Categoria

class VotoFilme(Voto):
  def __init__(self, membro: Membro, indicado: Filme, categoria: Categoria, ano: int):
    super().__init__(membro, indicado, categoria, ano)