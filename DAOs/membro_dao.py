from DAOs.dao import DAO
from entidade.membro import Membro

class MembroDAO(DAO):
    def __init__(self):
        super().__init__('membros.pkl')

    def add(self, membro: Membro):
        if membro is not None and isinstance(membro, Membro) and isinstance(membro.id, int):
            super().add(membro.id, membro)

    def update(self, membro: Membro):
        if membro is not None and isinstance(membro, Membro) and isinstance(membro.id, int):
            super().update(membro.id, membro)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
