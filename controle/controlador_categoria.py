from tela.tela_categoria import TelaCategoria
from entidade.categoria import Categoria
from DAOs.categoria_dao import CategoriaDAO

class ControladorCategoria():
    def __init__(self, controlador_sistema):
        self.__categoria_DAO = CategoriaDAO()
        self.__tela_categoria = TelaCategoria()
        self.__controlador_sistema = controlador_sistema

    def pegar_categoria_por_titulo(self, titulo: str):
        try:
            titulo = titulo.strip().title()
        except AttributeError:
            self.__tela_categoria.mostrar_mensagem("Título inválido.")
            return None

        categoria = self.__categoria_DAO.get(titulo)
        if categoria is not None:
            return categoria
        return None

    def pegar_categorias(self):
        return self.__categoria_DAO.get_all()

    def adicionar_categoria(self):
        try:
            dados_categoria = self.__tela_categoria.pegar_dados_categoria()
            if not dados_categoria or not dados_categoria.get("titulo"):
                self.__tela_categoria.mostrar_mensagem("Título da categoria não pode ser vazio.")
                return
            titulo = dados_categoria.get("titulo", "").strip().title()
            if self.pegar_categoria_por_titulo(titulo) is not None:
                self.__tela_categoria.mostrar_mensagem("\nCategoria já foi cadastrada.")
                return

            categoria = Categoria(titulo)
            self.__categoria_DAO.add(categoria)
            self.__tela_categoria.mostrar_mensagem("Categoria adicionada com sucesso!")
        except Exception as e:
            self.__tela_categoria.mostrar_mensagem(f"Erro ao adicionar categoria: {e}")

    def alterar_dados(self):
        titulo_categoria = self.__tela_categoria.selecionar_categoria()
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

        self.__categoria_DAO.remove(categoria.titulo)
        categoria.titulo = novo_titulo
        self.__categoria_DAO.add(categoria)
        self.__tela_categoria.mostrar_mensagem("Categoria alterada com sucesso!")

    def listar_categorias(self):
        categorias = self.__categoria_DAO.get_all()
        if not categorias:
            self.__tela_categoria.mostrar_mensagem("Nenhuma categoria cadastrada.")
            return

        dados_categorias = []
        for categoria in categorias:
            dados_categorias.append({"titulo": categoria.titulo})
        self.__tela_categoria.mostrar_dados_categoria(dados_categorias)

    def remover_categoria(self):
        titulo = self.__tela_categoria.selecionar_categoria()
        categoria = self.pegar_categoria_por_titulo(titulo)

        try:
            if categoria is None:
                raise LookupError("Categoria não foi cadastrada.")
        except LookupError as e:
            self.__tela_categoria.mostrar_mensagem(str(e))
            return

        self.__categoria_DAO.remove(categoria.titulo)
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
                self.__tela_categoria.mostrar_mensagem(f"Erro inesperado: {e}")