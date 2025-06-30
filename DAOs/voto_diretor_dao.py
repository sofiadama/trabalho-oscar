from DAOs.dao import DAO
from entidade.voto_diretor import VotoDiretor
from entidade.membro import Membro
from entidade.diretor import Diretor

class VotoDiretorDAO(DAO):
    def __init__(self):
        super().__init__('voto_diretor.pkl')

    def add(self, voto_diretor: VotoDiretor):
        if((voto_diretor is not None) and isinstance(voto_diretor, VotoDiretor) and isinstance(voto_diretor.membro, Membro) and isinstance(voto_diretor.indicado, Diretor)):
            key = (voto_diretor.membro, voto_diretor.indicado)
            super().add(key, voto_diretor)

    def update(self, voto_diretor: VotoDiretor):
        if((voto_diretor is not None) and isinstance(voto_diretor, VotoDiretor) and isinstance(voto_diretor.membro, Membro) and isinstance(voto_diretor.indicado, Diretor)):
            key = (voto_diretor.membro, voto_diretor.indicado)
            super().update(key, voto_diretor)

    def get(self, membro, indicado):
        if membro is not None and indicado is not None:
            key = (membro, indicado)
            return super().get(key)

    def remove(self, membro, indicado):
        if membro is not None and indicado is not None:
            key = (membro, indicado)
            return super().remove(key)
