from DAOs.dao import DAO
from entidade.diretor import Diretor

class DiretorDAO(DAO):
    def __init__(self):
        super().__init__('diretores.pkl')

    def add(self, diretor: Diretor):
        if diretor is not None and isinstance(diretor, Diretor) and isinstance(diretor.nome, str):
            super().add(diretor.nome, diretor)

    def update(self, diretor: Diretor):
        if diretor is not None and isinstance(diretor, Diretor) and isinstance(diretor.nome, str):
            super().update(diretor.nome, diretor)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
