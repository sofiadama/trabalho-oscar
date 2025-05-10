from diretor import Diretor

class Filme:
    def __init__(self, titulo: str, diretor: Diretor, ano_de_lancamento: int):
        self.__titulo = titulo
        self.__diretor = diretor
        self.__ano_de_lancamento = ano_de_lancamento
        
    @property
    def titulo(self):
      return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
      self.__titulo = titulo

    @property
    def diretor(self):
      return self.__diretor

    @diretor.setter
    def diretor(self, diretor):
      self.__diretor = diretor

    @property
    def ano_de_lancamento(self):
      return self.__ano_de_lancamento

    @ano_de_lancamento.setter
    def ano_de_lancamento(self, ano_de_lancamento):
      self.__ano_de_lancamento = ano_de_lancamento
