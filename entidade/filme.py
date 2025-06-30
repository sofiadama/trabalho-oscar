from entidade.categoria import Categoria

class Filme:
    def __init__(self, titulo: str, sinopse: str, categoria: Categoria, ano_indicacao: int):
        self.__titulo = titulo 
        self.__sinopse = sinopse
        self.__categoria = categoria
        self.__ano_indicacao = ano_indicacao
    
    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if not isinstance(titulo, str):
            raise TypeError("Título inválido.")
        self.__titulo = titulo
    
    @property
    def sinopse(self) -> str:
        return self.__sinopse

    @sinopse.setter
    def sinopse(self, sinopse: str):
        if not isinstance(sinopse, str):
            raise TypeError("Sinopse inválida.")
        self.__sinopse = sinopse

    @property
    def categoria(self) -> Categoria:
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria: Categoria):
        if not isinstance(categoria, Categoria):
            raise TypeError("Categoria inválida.")
        self.__categoria = categoria

    @property
    def ano_indicacao(self) -> int:
        return self.__ano_indicacao
    
    @ano_indicacao.setter
    def ano_indicacao(self, ano_indicacao: int):
        if not isinstance(ano_indicacao, int):
            raise TypeError("Ano de indicação inválido.")
        self.__ano_indicacao = ano_indicacao
        
    def __eq__(self, other):
        if isinstance(other, Filme):
            return self.titulo.strip().lower() == other.titulo.strip().lower()
        return False

    def __hash__(self):
        return hash(self.titulo.strip().lower())