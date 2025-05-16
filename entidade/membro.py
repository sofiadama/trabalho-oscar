class Membro:
    def __init__(self, id: int, nome: str, nascimento: str, nacionalidade: str):
        self.__votos = []

    @property 
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def nascimento(self):
        return self.__nascimento
    
    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento

    @property
    def nacionalidade(self):
        return self.__nacionalidade
    
    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade