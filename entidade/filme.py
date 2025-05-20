from entidade.categoria import Categoria

class Filme:
    def __init__(self, titulo: str, sinopse: str, categoria: Categoria, ano_indicacao: int):
        self.__titulo = titulo
        self.__sinopse = sinopse
        self.__categoria = categoria
        self.__ano_indicacao = ano_indicacao
    
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo
    
    @property
    def sinopse(self):
        return self.__sinopse

    @sinopse.setter
    def sinopse(self, sinopse: str):
        self.__sinopse = sinopse

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria: Categoria):
        self.__categoria = categoria

    @property
    def ano_indicacao(self):
        return self.__ano_indicacao
    
    @ano_indicacao.setter
    def ano_indicacao(self, ano_indicacao: int):
        self.__ano_indicacao = ano_indicacao