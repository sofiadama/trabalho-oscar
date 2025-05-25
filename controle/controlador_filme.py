from tela.tela_filme import TelaFilme
from entidade.filme import Filme

class ControladorFilme():
    def __init__(self, controlador_sistema):
        self.__filmes_indicados = []
        self.__tela_filme = TelaFilme(controlador_sistema)
        self.__controlador_sistema = controlador_sistema

    def adicionar_filme(self):
        try: 
            dados_filme = self.__tela_filme.pegar_dados_filme()

            for filme in self.__filmes_indicados:
                if filme.titulo == dados_filme["titulo"] and filme.sinopse == dados_filme["sinopse"]:
                    self.__tela_filme.mostrar_mensagem("\nFilme já foi cadastrado.")
                    return

            novo_filme = Filme(
                dados_filme["titulo"],
                dados_filme["sinopse"],
                dados_filme["categoria"],
                dados_filme["ano_indicacao"]
            )
            self.__filmes_indicados.append(novo_filme)
            self.__tela_filme.mostrar_mensagem("\nFilme cadastrado com sucesso!")

        except AttributeError as e: # pega erro no dicionario 
            self.__tela_filme.mostrar_mensagem(str(e))
        except KeyError as e:
            self.__tela_filme.mostrar_mensagem(f"Campo faltando: {e}")

    def alterar_dados(self):
        try:
            titulo_filme = self.__tela_filme.buscar_filme_por_titulo()
            filme = self.pegar_filme_por_titulo(titulo_filme)
            
            if filme is None:
                self.__tela_filme.mostrar_mensagem("\nFilme não foi cadastrado.")
                return
                
            novos_dados_filme = self.__tela_filme.pegar_dados_filme()
            filme.titulo = novos_dados_filme["titulo"]
            filme.sinopse = novos_dados_filme["sinopse"]
            filme.categoria = novos_dados_filme["categoria"]
            filme.ano_indicacao = novos_dados_filme["ano_indicacao"]
            self.__tela_filme.mostrar_mensagem("\nDados do filme alterados com sucesso!")

        except AttributeError as e:
            self.__tela_filme.mostrar_mensagem(str(e))   

    def listar_filmes(self):
        print("----- FILMES INDICADOS -----\n")
        if not self.__filmes_indicados:
            self.__tela_filme.mostrar_mensagem("\nNenhum filme indicado.")
            return
        
        for filme in self.__filmes_indicados:
            self.__tela_filme.mostrar_dados_filme({
                "titulo": filme.titulo, 
                "sinopse": filme.sinopse,
                "categoria": filme.categoria,
                "ano_indicacao": filme.ano_indicacao 
            })

    def remover_filme(self):
        titulo = self.__tela_filme.buscar_filme_por_titulo()
        filme = self.pegar_filme_por_titulo(titulo)
    
        try:
            if filme is not None:
                self.__filmes_indicados.remove(filme)
                self.__tela_filme.mostrar_mensagem("\nFilme removido com sucesso!")
            else: #se tentar remover filme que nao está na lista 
                raise LookupError("Filme não foi indicado.")
        except LookupError as e:
            self.__tela_filme.mostrar_mensagem(str(e))
    
    def gerar_relatorio_por_ano(self):
        ano = self.__tela_filme.buscar_indicados_por_ano()
        filmes_filtrados = [filme for filme in self.__filmes_indicados if filme.ano_indicacao == ano]
        
        if not filmes_filtrados:
            self.__tela_filme.mostrar_mensagem(f"Nenhum filme indicado no ano de '{ano}'.")
            return
        
        print("." * 15,f"INDICADOS NO ANO DE '{ano}'", "." * 15)
        for filme_filtrado in filmes_filtrados:
            self.__tela_filme.mostrar_dados_filme({
                "titulo": filme_filtrado.titulo, 
                "sinopse": filme_filtrado.sinopse,
                "categoria": filme_filtrado.categoria,
                "ano_indicacao": filme_filtrado.ano_indicacao 
            })
    
    def gerar_relatorio_por_categoria(self):
        categoria = self.__tela_filme.buscar_indicados_por_categoria().strip().title()
        filmes_filtrados = [filme for filme in self.__filmes_indicados if filme.categoria == categoria]
        
        if not filmes_filtrados:
            self.__tela_filme.mostrar_mensagem(f"Nenhum filme indicado na categoria '{categoria}'.")
            return
        
        print("." * 15,f"INDICADOS NA CATEGORIA '{categoria}'", "." * 15)
        for filme_filtrado in filmes_filtrados:
            self.__tela_filme.mostrar_dados_filme({
                "titulo": filme_filtrado.titulo, 
                "sinopse": filme_filtrado.sinopse,
                "categoria": filme_filtrado.categoria,
                "ano_indicacao": filme_filtrado.ano_indicacao 
            })
        
    def pegar_filme_por_titulo(self, titulo: str):
        try: # se digitar titulo que nao está na lista 
            titulo = titulo.strip().title()
        except AttributeError:
            self.__tela_filme.mostrar_mensagem("Título inválido.")
            return None
        
        filmes_encontrados = [filme for filme in self.__filmes_indicados if filme.titulo == titulo]

        try:
            if len(filmes_encontrados) == 1:
                return filmes_encontrados[0]
            elif len(filmes_encontrados) > 1:
                raise LookupError("Há mais de um filme com esse título.")
            else:
                raise LookupError("Filme não foi cadastrado.")
        except LookupError as e:
            self.__tela_filme.mostrar_mensagem(str(e))
            return None
    
    def pegar_filmes_indicados(self):
        return self.__filmes_indicados
    
    def retornar_menu(self):
        self.__controlador_sistema.abrir_submenu_indicacoes()
    
    def abrir_tela_filme(self):
        opcoes = {
            1: self.adicionar_filme, 
            2: self.alterar_dados, 
            3: self.abrir_filtro, 
            4: self.remover_filme, 
            0: self.retornar_menu
        }
    
        continuar = True
        while continuar:
            try:
                opcao = self.__tela_filme.tela_opcoes()
                if opcao in opcoes:
                    opcoes[opcao]()
                else:
                    self.__tela_filme.mostrar_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela_filme.mostrar_mensagem(f"Erro inesperado: {e}")

    def abrir_filtro(self):
        opcoes = {
            1: self.listar_filmes, 
            2: self.gerar_relatorio_por_ano,
            3: self.gerar_relatorio_por_categoria, 
            0: self.retornar_menu
        }

        while True:
            try:
                opcoes[self.__tela_filme.tela_filtros_de_relatorios()]()
            except KeyError:
                self.__tela_filme.mostrar_mensagem("Opção inválida!")


