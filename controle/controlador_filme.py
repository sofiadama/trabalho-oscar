from tela.tela_filme import TelaFilme
from entidade.filme import Filme

class ControladorFilme:
    def __init__(self, controlador_sistema):
        self.__filmes_indicados = []
        self.__tela_filme = TelaFilme()
        self.__controlador_sistema = controlador_sistema

    def adicionar_filme(self):
        dados_filme = self.__tela_filme.pegar_dados_filme()

        filme = Filme(
            dados_filme["titulo"], 
            dados_filme["sinopse"],
            dados_filme["categoria"],
            dados_filme["ano de indicacao"]
        )

        if self.verificar_categoria_inexistente(dados_filme):
            return
        if self.verificar_categoria_restrita(dados_filme):
            return
        if self.verificar_duplicidade_indicacao(dados_filme):
            return

        self.__filmes_indicados.append(filme)

    def alterar_dados(self):
        titulo_filme = self.__tela_filme.buscar_filme_por_titulo()
        filme = self.pegar_filme_por_titulo(titulo_filme)

        if filme is None:
            self.__tela_filme.mostrar_mensagem("\nFilme não foi cadastrado.")
            return
        
        novos_dados_filme = self.__tela_filme.pegar_dados_filme()
        filme.titulo = novos_dados_filme["titulo"]
        filme.sinopse = novos_dados_filme["sinopse"]
        filme.categoria = novos_dados_filme["categoria"]
        filme.ano_indicacao = novos_dados_filme["ano de indicacao"]
        self.listar_filmes()
        
    def listar_filmes(self):
        if not self.__filmes_indicados:
            print(f"\nNenhum filme indicado.")
            return
        
        print("----- FILMES INDICADOS -----\n")
        for filme in self.__filmes_indicados:
            self.__tela_filme.mostrar_dados_filme({
                "titulo": filme.titulo, 
                "sinopse": filme.sinopse,
                "categoria": filme.categoria,
                "ano de indicacao": filme.ano_indicacao 
            })

    def remover_filme(self):
        titulo = self.__tela_filme.buscar_filme_por_titulo()
        filme = self.pegar_filme_por_titulo(titulo)

        if filme is None:
            self.__tela_filme.mostrar_mensagem("\nFilme não foi indicado.")
            return

        self.__filmes_indicados.remove(filme)
        self.__tela_filme.mostrar_mensagem("\nFilme removido com sucesso!")

    def verificar_categoria_inexistente(self, dados_filme):
        categorias_cadastradas = self.__controlador_sistema.controlador_categoria.pegar_categorias_cadastradas()

        if dados_filme["categoria"] not in [categoria.titulo for categoria in categorias_cadastradas]:
            print("\nCategoria não cadastrada.")
            return True
        return False
    
    def verificar_categoria_restrita(self, dados_filme):
        categorias_restritas = self.__controlador_sistema.controlador_categoria.pegar_categorias_restritas()
        
        if dados_filme["categoria"] in categorias_restritas:
            print("\nCategoria restrita a atores e diretores.")
            return True
        return False
    
    def verificar_duplicidade_indicacao(self, dados_filme):
        for filme in self.__filmes_indicados:
            if filme.titulo == dados_filme["titulo"] and filme.sinopse == dados_filme["sinopse"]:
                print("\nFilme já foi indicado.")
                return True
        return False

    def pegar_filme_por_titulo(self, titulo: str):
        return [filme for filme in self.__filmes_indicados if filme.titulo == titulo]
    
    def pegar_filme_por_categoria(self, categoria: str):
        return [filme for filme in self.__filmes_indicados if filme.categoria == categoria]
    
    def pegar_filme_por_ano(self, ano_indicacao: int):
        return [filme for filme in self.__filmes_indicados if filme.ano_indicacao == ano_indicacao]
    
    def filtrar_indicados_por_categoria(self):
        categoria = self.__tela_filme.buscar_categoria()
        filmes_filtrados = self.pegar_filme_por_categoria(categoria) 
    
        if not filmes_filtrados:
            print(f"\nNenhum filme indicado na categoria '{categoria}'.")
            return

        print(f"----- FILMES INDICADOS NA CATEGORIA '{categoria}' -----\n")
        for filme in filmes_filtrados:
            print(filme.titulo)

    def filtrar_indicados_por_ano(self):
        ano_indicacao = self.__tela_filme.buscar_ano_indicacao()
        filmes_filtrados = self.pegar_filme_por_ano(ano_indicacao) 

        if not filmes_filtrados:
            print(f"\nNenhum filme indicado no ano de '{ano_indicacao}'.")
            return

        print(f"----- FILMES INDICADOS NO ANO DE '{ano_indicacao}' -----\n")
        for filme in filmes_filtrados:
            print(filme.titulo)
    
    def pegar_filmes_indicados(self):
        return self.__filmes_indicados
    
    def retornar_menu(self):
        self.__controlador_sistema.abrir_submenu_indicacoes()

    def listar_filmes_por_filtro(self):
        opcoes = {
            1: self.filtrar_indicados_por_categoria,
            2: self.filtrar_indicados_por_ano,
            3: self.listar_filmes,
            0: self.abrir_tela_filme
        }

        continuar = True
        while continuar:
            opcoes[self.__tela_filme.tela_opcoes_filtros()]()
    
    def abrir_tela_filme(self):
        opcoes = {
            1: self.adicionar_filme, 
            2: self.alterar_dados, 
            3: self.listar_filmes_por_filtro, 
            4: self.remover_filme, 
            0: self.retornar_menu
        }
    
        continuar = True
        while continuar:
            opcoes[self.__tela_filme.tela_opcoes()]()
    
    
