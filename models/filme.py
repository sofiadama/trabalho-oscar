from diretor import Diretor

class Filme:
    def __init__(self, titulo: str, diretor: Diretor, ano_de_lancamento: int):
        self.__titulo = titulo
        self.__diretor = diretor
        self.__ano_de_lancamento = ano_de_lancamento
        self.__filmes_indicados = []
        
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

    def adicionar_indicacao(self, titulo: str, diretor: Diretor, ano_de_lancamento: int):
        for filme_indicado in self.__filmes_indicados:
            if titulo == filme_indicado["titulo"]:
                print("Filme já foi indicado.")
                return

        novo_filme_indicado = {"titulo": titulo, "diretor": diretor, "ano": ano_de_lancamento}
        return

    def alterar_indicacao(self):
        pass
        
    def listar_indicacoes(self):
        return self.__filmes_indicados
        
    def remover_indicacao(self, titulo: str):
        for filme_indicado not in self.__filmes_indicados:
            print("Filme não foi indicado.")
            return

        self.__filmes_indicados = [filme_indicado for filme_indicado in self.__filmes_indicados if filme_indicado.get("titulo") != titulo]
        return
