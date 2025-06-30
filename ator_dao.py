from DAOs.dao import DAO
from entidade.ator import Ator

class AtorDAO(DAO):
    def __init__(self):
        super().__init__('atores.pkl')

    def add(self, ator: Ator):
        if ator is not None and isinstance(ator, Ator) and isinstance(ator.nome, str):
            super().add(ator.nome, ator)

    def update(self, ator: Ator):
        if ator is not None and isinstance(ator, Ator) and isinstance(ator.nome, str):
            super().update(ator.nome, ator)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
