from entidade.indicado import Indicado

class Ator(Indicado):
    def __init__(self, nome: str, nacionalidade: str, categoria, filme, ano_indicacao: int):
        super().__init__(nome, nacionalidade, categoria, filme, ano_indicacao)