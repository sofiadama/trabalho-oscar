from tela.tela_categoria import TelaCategoria
from entidade.categoria import Categoria

class ControladorCategoria():
    def __init__(self, controlador_sistema):
        self.__categorias = []
        self.__tela_categoria = TelaCategoria()
        self.__controlador_sistema = controlador_sistema
    
    def pegar_categoria_por_titulo(self, titulo: str):
        try:
          titulo = titulo.strip().title()
        except AttributeError:
          self.__tela_categoria.mostrar_mensagem("Título inválido.")
          return None
        
        for categoria in self.__categorias:
            if categoria.titulo.strip().title() == titulo:
                return categoria
        return None

    def adicionar_categoria(self):
        try: #entrada invalida
            dados_categoria = self.__tela_categoria.pegar_dados_categoria()
        except ValueError as e:
            self.__tela_categoria.mostrar_mensagem(str(e))
            return
        titulo = dados_categoria.get("titulo", "").strip().title()
        if not titulo:
            self.__tela_categoria.mostrar_mensagem("Título da categoria não pode ser vazio.")
            return

        if self.pegar_categoria_por_titulo(titulo) is not None:
            self.__tela_categoria.mostrar_mensagem("\nCategoria já foi cadastrada.")
            return

        categoria = Categoria(titulo)
        self.__categorias.append(categoria)
        self.__tela_categoria.mostrar_mensagem("Categoria adicionada com sucesso!")
        
        
    def alterar_dados(self):
        titulo_categoria = self.__tela_categoria.buscar_categoria()
        categoria = self.pegar_categoria_por_titulo(titulo_categoria)

        if categoria is None:
            self.__tela_categoria.mostrar_mensagem("Categoria não foi cadastrada.")
            return

        novos_dados = self.__tela_categoria.pegar_dados_categoria()
        novo_titulo = novos_dados.get("titulo", "").strip().title()

        if not novo_titulo:
            self.__tela_categoria.mostrar_mensagem("Título inválido.")
            return

        if self.pegar_categoria_por_titulo(novo_titulo) and novo_titulo != categoria.titulo:
            self.__tela_categoria.mostrar_mensagem("Já existe uma categoria com esse título.")
            return
        
        categoria.titulo = novo_titulo
        self.__tela_categoria.mostrar_mensagem("Categoria alterada com sucesso!")

    def listar_categorias(self):
        print("----- CATEGORIAS -----\n")
        if not self.__categorias:
            self.__tela_categoria.mostrar_mensagem("Nenhuma categoria cadastrada.")
            return
        
        for categoria in self.__categorias:
            self.__tela_categoria.mostrar_dados_categoria({"titulo": categoria.titulo})

    def remover_categoria(self):
        titulo = self.__tela_categoria.buscar_categoria()
        categoria = self.pegar_categoria_por_titulo(titulo)

        try:
            if categoria is None:
                raise LookupError("Categoria não foi cadastrada.")
            
        except LookupError as e:
            self.__tela_categoria.mostrar_mensagem(str(e))
            return
        
        self.__categorias.remove(categoria)
        self.__tela_categoria.mostrar_mensagem("\nCategoria removida com sucesso!")
      
    def retornar_menu(self):
        self.__controlador_sistema.abrir_submenu_cadastros()
    
    def abrir_tela_categoria(self):
        opcoes = {
            1: self.adicionar_categoria, 
            2: self.alterar_dados, 
            3: self.listar_categorias, 
            4: self.remover_categoria, 
            0: self.retornar_menu
        }

        while True:
            try:
                opcao = self.__tela_categoria.tela_opcoes()
                if opcao in opcoes:
                    opcoes[opcao]()
                else:
                    self.__tela_categoria.mostrar_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela_categoria.mostrar_mensagem(f"Erro inesperado")