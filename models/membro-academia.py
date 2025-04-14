from pessoa import Pessoa

class MembroAcademia(Pessoa):
    def __init__(self, id, nome, data_de_nascimento, nacionalidade):
        super().__init__(id, nome, data_de_nascimento, nacionalidade)
