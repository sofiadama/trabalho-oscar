from DAOs.dao import DAO
from entidade.categoria import Categoria

class CategoriaDAO(DAO):
    def __init__(self):
        super().__init__('categorias.pkl')

    def add(self, categoria: Categoria):
        if categoria is not None and isinstance(categoria, Categoria) and isinstance(categoria.titulo, str):
            super().add(categoria.titulo, categoria)

    def update(self, categoria: Categoria):
        if categoria is not None and isinstance(categoria, Categoria) and isinstance(categoria.titulo, str):
            super().update(categoria.titulo, categoria)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
