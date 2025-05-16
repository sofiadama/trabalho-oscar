from tela.tela_categoria import TelaCategoria
from entidade.categoria import Categoria
from entidade.filme import Filme

class ControladorCategoria():
    def __init__(self, controlador_sistema):
        self.__categorias = {}
        self.__tela_categoria = TelaCategoria()
        self.__controlador_sistema = controlador_sistema
    
    def pegar_categoria_por_titulo(self, titulo: str):
        for categoria in self.__categorias:
            if(categoria.titulo == titulo):
                return categoria
        return None
    
    def adicionar_categoria(self, titulo):
        dados_categoria = self.__tela_categoria.pegar_dados_categoria()
        titulo = dados_categoria["titulo"]
        
        if titulo in self.__categorias:
            print("Categoria já foi cadastrada.")
            return

        categoria = Categoria(titulo)
        self.__categorias[titulo] = []  
        # Cria a chave com lista vazia para filmes    

    def alterar_categoria(self, titulo):
        self.listar_categorias()
        titulo_categoria = self.__tela_categoria.buscar_categoria()
        categoria = self.pegar_categoria_por_titulo(titulo_categoria)

        if(categoria is not None):
            novo_titulo_categoria = self.__tela_categoria.pegar_dados_categoria()
            categoria.titulo = novo_titulo_categoria["titulo"]
            self.listar_categorias()
        else:
            self.__tela_categoria.mostrar_mensagem("Categoria não cadastrada.")  
        
    def listar_categorias(self, titulo):
        titulos_categorias = self.__categorias.keys()
        print("\nLista de categorias:\n")

        for titulos in titulos_categorias:
            print(titulos)
        
   