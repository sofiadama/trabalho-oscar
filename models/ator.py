from pessoa import Pessoa

class Ator(Pessoa):
    def __init__(self, id: int, nome: str, data_de_nascimento: int, nacionalidade: str):
        super().__init__(id, nome, data_de_nascimento, nacionalidade)
        self.__atores_indicados = []

    def indicar_ator():
        for ator_indicado in self.__atores_indicados:
            if novo_ator_indicado == ator_indicado:
                return "Ator já foi indicado."

        novo_ator_indicado = {"id": id, "nome": nome, "data_de_nascimento": data_de_nascimento, "nacionalidade": nacionalidade}
        self.__atores_indicados.append(novo_ator_indicado)
