from tela.tela_filme import TelaFilme
from entidade.filme import Filme

class ControladorFilme():
    def __init__(self, controlador_sistema):
        self.__filmes_indicados = []
        self.__tela_filme = TelaFilme()
        self.__controlador_sistema = controlador_sistema
    
    def pegar_filme_por_titulo(self, titulo: str):
        for filme in self.__filmes_indicados:
            if filme.titulo == titulo:
                return filme
            elif self.__filmes_indicados.count(filme) > 1:
                self.__tela_filme.mostrar_mensagem("Há mais de um filme com esse título.")
        return None

    def adicionar_filme(self):
        dados_filme = self.__tela_filme.pegar_dados_filme()
        for filme in self.__filmes_indicados:
            if filme.titulo == dados_filme["titulo"] and filme.sinopse == dados_filme["sinopse"]:
                print("\nFilme já foi cadastrado.")
                return

        filme = Filme(
            dados_filme["titulo"], 
            dados_filme["sinopse"],
            dados_filme["categoria"],
            dados_filme["ano de indicacao"]
        )

        self.__filmes_indicados.append(filme)
    
    def alterar_dados(self):
        titulo_filme = self.__tela_filme.buscar_filme()
        filme = self.pegar_filme_por_titulo(titulo_filme)

        if filme is not None:
            novos_dados_filme = self.__tela_filme.pegar_dados_filme()
            filme.titulo = novos_dados_filme["titulo"]
            filme.sinopse = novos_dados_filme["sinopse"]
            filme.categoria = novos_dados_filme["categoria"]
            filme.ano_indicacao = novos_dados_filme["ano de indicacao"]
            self.listar_filmes()

        else:
            self.__tela_filme.mostrar_mensagem("\nFilme não foi cadastrado.")

    def listar_filmes(self):
        print("----- FILMES INDICADOS -----\n")
        for filme in self.__filmes_indicados:
            self.__tela_filme.mostrar_dados_filme({
                "titulo": filme.titulo, 
                "sinopse": filme.sinopse,
                "categoria": filme.categoria,
                "ano de indicacao": filme.ano_indicacao 
            })

        if self.__filmes_indicados == []:
            self.__tela_filme.mostrar_mensagem("\nNenhum filme indicado.")

    def remover_filme(self):
        titulo = self.__tela_filme.buscar_filme()
        filme = self.pegar_filme_por_titulo(titulo)

        if filme is not None:
            self.__filmes_indicados.remove(filme)
            self.__tela_filme.mostrar_mensagem("\nFilme removido com sucesso!")
        else:
            self.__tela_filme.mostrar_mensagem("\nFilme não foi indicado.")
    
    def retornar_menu(self):
        self.__controlador_sistema.abrir_tela_indicacoes()
    
    def abrir_tela_filme(self):
        opcoes = {
            1: self.adicionar_filme, 
            2: self.alterar_dados, 
            3: self.listar_filmes, 
            4: self.remover_filme, 
            0: self.retornar_menu
        }
    
        continuar = True
        while continuar:
            opcoes[self.__tela_filme.tela_opcoes()]()
