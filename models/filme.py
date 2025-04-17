from diretor import Diretor
from categoria import Categoria

class Filme:
    def __init__(self, titulo: str, ano: int, diretor: Diretor, ator: Ator, categoria: Categoria):
        self.titulo = titulo
        self.ano_de_lancamento = ano_de_lancamento
        self.diretor = diretor
        self.ator = ator
        self.categoria = categoria
    
    @property
    def titulo(self):
      return self.titulo

    @titulo.setter
    def titulo(self, titulo):
      self.titulo = titulo

    @property
    def ano_de_lancamento(self):
      return self.ano_de_lancamento

    @ano_de_lancamento.setter
    def ano_de_lancamento(self, ano_de_lancamento):
      self.ano_de_lancamento = ano_de_lancamento
      
    @property
    def diretor(self):
      return self.diretor

    @diretor.setter
    def diretor(self, diretor):
      self.diretor = diretor

    @property
    def ator(self):
      return self.ator

    @ator.setter
    def ator(self, ator):
      self.ator = ator

    @property
    def categoria(self):
      return self.categoria

    @categoria.setter
    def categoria(self, categoria):
      self.categoria = categoria
