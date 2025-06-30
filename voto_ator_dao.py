from DAOs.dao import DAO
from entidade.voto_ator import VotoAtor
from entidade.membro import Membro
from entidade.ator import Ator

class VotoAtorDAO(DAO):
    def __init__(self):
        super().__init__('voto_ator.pkl')

    def add(self, voto_ator: VotoAtor):
        if((voto_ator is not None) and isinstance(voto_ator, VotoAtor) and isinstance(voto_ator.membro, Membro) and isinstance(voto_ator.indicado, Ator)):
            key = (voto_ator.membro, voto_ator.indicado)
            super().add(key, voto_ator)

    def update(self, voto_ator: VotoAtor):
        if((voto_ator is not None) and isinstance(voto_ator, VotoAtor) and isinstance(voto_ator.membro, Membro) and isinstance(voto_ator.indicado, Ator)):
            key = (voto_ator.membro, voto_ator.indicado)
            super().update(key, voto_ator)

    def get(self, membro, indicado):
        if membro is not None and indicado is not None:
            key = (membro, indicado)
            return super().get(key)

    def remove(self, membro, indicado):
        if membro is not None and indicado is not None:
            key = (membro, indicado)
            return super().remove(key)
