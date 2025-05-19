from entidade.filme import Filme
from entidade.diretor import Diretor
from entidade.categoria import Categoria

class ControladorFilme:
    def __init__(self):
        self.__filmes = []

    def cadastrar_filme(self, titulo: str, diretor: Diretor, categoria: Categoria):
        filme = Filme(titulo, diretor, categoria)
        self.__filmes.append(filme)
        return filme

    def listar_filmes(self):
        return self.__filmes

    def buscar_filme_por_titulo(self, titulo: str):
        for filme in self.__filmes:
            if filme.titulo == titulo:
                return filme
        return None

    def remover_filme(self, titulo: str):
        filme = self.buscar_filme_por_titulo(titulo)
        if filme:
            self.__filmes.remove(filme)
            return True
        return False

    def alterar_filme(self, titulo_atual: str, novo_titulo: str = None, novo_diretor: Diretor = None, nova_categoria: Categoria = None):
        filme = self.buscar_filme_por_titulo(titulo_atual)
        if filme:
            if novo_titulo:
                filme.titulo = novo_titulo
            if novo_diretor:
                filme.diretor = novo_diretor
            if nova_categoria:
                filme.categoria = nova_categoria
            return filme
        return None
