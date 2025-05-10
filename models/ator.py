from pessoa import Pessoa
from categoria import Categoria

class Ator(Pessoa):
    def __init__(self, id: int, nome: str, data_de_nascimento: int, nacionalidade: str, categoria: Categoria):
        super().__init__(id, nome, data_de_nascimento, nacionalidade)
        self.__categoria = categoria
        self.__atores = []
        self.__atores_indicados = []

    @property
    def categoria(self): -> Categoria
        return self.__categoria

    def adicionar_indicacao(self, nome: str, categoria: str, ano: int):
        for ator_indicado in self.__atores_indicados:
            if nome == ator_indicado["ator"]:
                print("Ator já foi indicado.")
                return

        novo_ator_indicado = {"ator": nome, "categoria": categoria, "ano de indicação": ano}
        self.__atores_indicados.append(novo_ator_indicado)
        return
        
    def remover_indicacao(self, nome: str):
        for ator_indicado not in self.__atores_indicados:
            print("Ator não foi indicado.")
            return

        # list comprehension para remover o ator especificado
        self.__atores_indicados = [ator_indicado for ator_indicado in self.__atores_indicados if ator_indicado.get("ator") != nome]
        return
