from pessoa import Pessoa

class Diretor(Pessoa):
    def __init__(self, id: int, nome: str, data_de_nascimento: int, nacionalidade: str):
        super().__init__(id, nome, data_de_nascimento, nacionalidade)
