from entidade.voto import Voto
from entidade.membro import Membro
from entidade.diretor import Diretor
from entidade.categoria import Categoria

class VotoDiretor(Voto):  
  def __init__(self, membro: Membro, indicado: Diretor, categoria: Categoria, ano: int):
    super().__init__(membro, indicado, categoria, ano)