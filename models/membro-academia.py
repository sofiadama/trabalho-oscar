from pessoa import Pessoa
from voto import Voto

class MembroAcademia(Pessoa):
    def __init__(self, id: int, nome: str, data_de_nascimento: int, nacionalidade: str, votos: Voto):
        super().__init__(id, nome, data_de_nascimento, nacionalidade)
        self.__votos = []

    @property
    def votos(self):
        return self.__votos

    def adicionar_voto(self, voto: Voto):
        self.__votos.append(voto)
