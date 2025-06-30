class Membro:
    def __init__(self, id: int, nome: str, nascimento: str, nacionalidade: str):
        self.__id = id
        self.__nome = nome
        self.__nascimento = nascimento
        self.__nacionalidade = nacionalidade

    @property 
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id: int):
        if not isinstance(id, int):
            raise TypeError("ID inválido.")
        self.__id = id
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str):
            raise TypeError("Nome inválido.")
        self.__nome = nome
    
    @property
    def nascimento(self) -> str:
        return self.__nascimento
    
    @nascimento.setter
    def nascimento(self, nascimento: str):
        if not isinstance(nascimento, str):
            raise TypeError("Data de nascimento inválida.")
        self.__nascimento = nascimento

    @property
    def nacionalidade(self) -> str:
        return self.__nacionalidade
    
    @nacionalidade.setter
    def nacionalidade(self, nacionalidade: str):
        if not isinstance(nacionalidade, str):
            raise TypeError("Nacionalidade inválida.")
        self.__nacionalidade = nacionalidade
    
    def __eq__(self, other):
        if isinstance(other, Membro):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)