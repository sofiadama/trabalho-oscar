class Categoria:
    def __init__(self, titulo: str):
        self.__titulo = titulo

    @property
    def titulo(self) -> str:
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        if not isinstance(titulo, str):
            raise TypeError("Título inválido!")
        self.__titulo = titulo