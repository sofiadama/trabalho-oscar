from DAOs.dao import DAO
from entidade.voto_filme import VotoFilme
from entidade.membro import Membro
from entidade.filme import Filme

class VotoFilmeDAO(DAO):
    def __init__(self):
        super().__init__('voto_filme.pkl')

    def add(self, voto_filme: VotoFilme):
        if((voto_filme is not None) and isinstance(voto_filme, VotoFilme) and isinstance(voto_filme.membro, Membro) and isinstance(voto_filme.indicado, Filme)):
            key = (voto_filme.membro, voto_filme.indicado)
            super().add(key, voto_filme)

    def update(self, voto_filme: VotoFilme):
        if((voto_filme is not None) and isinstance(voto_filme, VotoFilme) and isinstance(voto_filme.membro, Membro) and isinstance(voto_filme.indicado, Filme)):            
            key = (voto_filme.membro, voto_filme.indicado)
            super().update(key, voto_filme)

    def get(self, membro, indicado):
        if membro is not None and indicado is not None:
            key = (membro, indicado)
            return super().get(key)

    def remove(self, membro, indicado):
        if membro is not None and indicado is not None:
            key = (membro, indicado)
            return super().remove(key)