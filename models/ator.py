from pessoa import Pessoa

class Ator(Pessoa):
    def __init__(self, id, nome, data_de_nascimento, nacionalidade):
        super().__init__(id, nome, data_de_nascimento, nacionalidade)
