from entidade.indicado import Indicado
from entidade.categoria import Categoria
from entidade.filme import Filme

class Ator(Indicado):
    def __init__(self, nome: str, nacionalidade: str, categoria: Categoria, filme: Filme, ano_indicacao: int):
        super().__init__(nome, nacionalidade, categoria, filme, ano_indicacao)
