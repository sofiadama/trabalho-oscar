from DAOs.dao import DAO
from entidade.filme import Filme

class FilmeDAO(DAO):
    def __init__(self):
        super().__init__('filmes.pkl')

    def add(self, filme: Filme):
        if filme is not None and isinstance(filme, Filme) and isinstance(filme.titulo, str):
            super().add(filme.titulo, filme)

    def update(self, filme: Filme):
        if filme is not None and isinstance(filme, Filme) and isinstance(filme.titulo, str):
            super().update(filme.titulo, filme)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
