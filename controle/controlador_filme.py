from tela.tela_filme import TelaFilme
from entidade.filme import Filme
from DAOs.filme_dao import FilmeDAO

class ControladorFilme():
    def __init__(self, controlador_sistema):
        self.__filme_DAO = FilmeDAO()
        self.__tela_filme = TelaFilme()
        self.__controlador_sistema = controlador_sistema

    def pegar_filme_por_titulo(self, titulo: str):
        try:
            titulo = titulo.strip().title()
        except AttributeError:
            self.__tela_filme.mostrar_mensagem("Título inválido.")
            return None
        
        filme = self.__filme_DAO.get(titulo)
        if filme is not None:
            return filme
        else:
            self.__tela_filme.mostrar_mensagem("Filme não foi cadastrado.")
            return None

    def pegar_filmes_indicados(self):
        return self.__filme_DAO.get_all()

    def adicionar_filme(self):
        try:
            dados_filme = self.__tela_filme.pegar_dados_filme()
            if not dados_filme:
                return

            titulo = dados_filme["titulo"].strip().title()
            if self.__filme_DAO.get(titulo) is not None:
                self.__tela_filme.mostrar_mensagem("\nFilme já foi cadastrado.")
                return

            categoria_obj = self.__controlador_sistema.controlador_categoria.pegar_categoria_por_titulo(dados_filme["categoria"])
            if not categoria_obj:
                self.__tela_filme.mostrar_mensagem(f"Categoria '{dados_filme['categoria']}' não cadastrada.")
                return

            ano = int(dados_filme["ano_indicacao"])

            novo_filme = Filme(
                titulo,
                dados_filme["sinopse"],
                categoria_obj,
                ano
            )
            self.__filme_DAO.add(novo_filme)
            self.__tela_filme.mostrar_mensagem("\nFilme cadastrado com sucesso!")

        except (AttributeError, KeyError, ValueError) as e:
            self.__tela_filme.mostrar_mensagem(f"Erro ao cadastrar filme: {e}")

    def alterar_dados(self):
        try:
            titulo_filme = self.__tela_filme.buscar_filme_por_titulo()
            filme = self.pegar_filme_por_titulo(titulo_filme)
            
            if filme is None:
                self.__tela_filme.mostrar_mensagem("\nFilme não foi cadastrado.")
                return
                
            novos_dados_filme = self.__tela_filme.pegar_dados_filme()
            if not novos_dados_filme:
                return

            categoria_obj = self.__controlador_sistema.controlador_categoria.pegar_categoria_por_titulo(novos_dados_filme["categoria"])
            if not categoria_obj:
                self.__tela_filme.mostrar_mensagem(f"Categoria '{novos_dados_filme['categoria']}' não cadastrada.")
                return

            ano = int(novos_dados_filme["ano_indicacao"])

            self.__filme_DAO.remove(filme.titulo)
            filme.titulo = novos_dados_filme["titulo"].strip().title()
            filme.sinopse = novos_dados_filme["sinopse"]
            filme.categoria = categoria_obj
            filme.ano_indicacao = ano
            self.__filme_DAO.add(filme)
            self.__tela_filme.mostrar_mensagem("\nDados do filme alterados com sucesso!")

        except (AttributeError, KeyError, ValueError) as e:
            self.__tela_filme.mostrar_mensagem(f"Erro ao alterar filme: {e}")

    def listar_filmes(self):
        filmes = self.__filme_DAO.get_all()
        if not filmes:
            self.__tela_filme.mostrar_mensagem("\nNenhum filme indicado.")
            return
        
        dados_filmes = []
        for filme in filmes:
            dados_filmes.append({
                "titulo": filme.titulo, 
                "sinopse": filme.sinopse,
                "categoria": filme.categoria.titulo if hasattr(filme.categoria, 'titulo') else str(filme.categoria),
                "ano_indicacao": filme.ano_indicacao 
            })
        
        self.__tela_filme.mostrar_dados_filme(dados_filmes)
        
    def remover_filme(self):
        titulo = self.__tela_filme.buscar_filme_por_titulo()
        filme = self.pegar_filme_por_titulo(titulo)
    
        try:
            if filme is not None:
                self.__filme_DAO.remove(filme.titulo)
                self.__tela_filme.mostrar_mensagem("\nFilme removido com sucesso!")
            else:
                raise LookupError("Filme não foi indicado.")
        except LookupError as e:
            self.__tela_filme.mostrar_mensagem(str(e))
    
    def gerar_relatorio_por_ano(self):
        ano = self.__tela_filme.buscar_indicados_por_ano()
        try:
            ano = int(ano)
        except (TypeError, ValueError):
            self.__tela_filme.mostrar_mensagem("Ano inválido.")
            return

        filmes_filtrados = [filme for filme in self.__filme_DAO.get_all() if filme.ano_indicacao == ano]
        
        if not filmes_filtrados:
            self.__tela_filme.mostrar_mensagem(f"Nenhum filme indicado no ano de '{ano}'.")
            return
        
        mensagem = f"............... INDICADOS NO ANO DE '{ano}' ...............\n"
        for i, filme_filtrado in enumerate(filmes_filtrados, 1):
            categoria = filme_filtrado.categoria.titulo if hasattr(filme_filtrado.categoria, 'titulo') else str(filme_filtrado.categoria)
            mensagem += f"{i}. Filme: {filme_filtrado.titulo}, Sinopse: {filme_filtrado.sinopse}, Categoria: {categoria}, Ano de Indicação: {filme_filtrado.ano_indicacao}\n"

        self.__tela_filme.mostrar_mensagem(mensagem)
    
    def gerar_relatorio_por_categoria(self):
        categoria = self.__tela_filme.buscar_indicados_por_categoria().strip().title()
        filmes_filtrados = [
            filme for filme in self.__filme_DAO.get_all()
            if (hasattr(filme.categoria, 'titulo') and filme.categoria.titulo.strip().title() == categoria)
            or (isinstance(filme.categoria, str) and filme.categoria.strip().title() == categoria)
        ]
        
        if not filmes_filtrados:
            self.__tela_filme.mostrar_mensagem(f"Nenhum filme indicado na categoria '{categoria}'.")
            return
        
        mensagem = f"............... INDICADOS NA CATEGORIA '{categoria}' ...............\n"
        for i, filme_filtrado in enumerate(filmes_filtrados, 1):
            categoria_nome = filme_filtrado.categoria.titulo if hasattr(filme_filtrado.categoria, 'titulo') else str(filme_filtrado.categoria)
            mensagem += f"{i}. Filme: {filme_filtrado.titulo}, Sinopse: {filme_filtrado.sinopse}, Categoria: {categoria_nome}, Ano de Indicação: {filme_filtrado.ano_indicacao}\n"

        self.__tela_filme.mostrar_mensagem(mensagem)
        
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
            0: self.abrir_tela_filme
        }

        while True:
            try:
                op = self.__tela_filme.tela_filtros_de_relatorios()
                if op in opcoes:
                    opcoes[op]()
                else:
                    self.__tela_filme.mostrar_mensagem("Opção inválida!")
            except KeyError:
                self.__tela_filme.mostrar_mensagem("Opção inválida!")