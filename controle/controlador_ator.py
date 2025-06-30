from tela.tela_ator import TelaAtor
from entidade.ator import Ator
from DAOs.ator_dao import AtorDAO

class ControladorAtor():
    def __init__(self, controlador_sistema):
        self.__ator_DAO = AtorDAO()
        self.__tela_ator = TelaAtor()
        self.__controlador_sistema = controlador_sistema

    def pegar_ator_por_nome(self, nome: str):
        try:
            nome = nome.strip().title()
        except AttributeError:
            self.__tela_ator.mostrar_mensagem("Nome inválido.")
            return None

        ator = self.__ator_DAO.get(nome)
        if ator is not None:
            return ator
        else:
            self.__tela_ator.mostrar_mensagem("Ator não foi indicado.")
            return None

    def pegar_atores_indicados(self):
        return self.__ator_DAO.get_all()

    def adicionar_ator(self):
        dados_ator = self.__tela_ator.pegar_dados_ator()
        if not dados_ator:
            return

        nome = dados_ator["nome"].strip().title()
        if self.__ator_DAO.get(nome) is not None:
            self.__tela_ator.mostrar_mensagem("\nAtor já foi indicado.")
            return

        categoria_obj = self.__controlador_sistema.controlador_categoria.pegar_categoria_por_titulo(dados_ator["categoria"])
        if not categoria_obj:
            self.__tela_ator.mostrar_mensagem(f"Categoria '{dados_ator['categoria']}' não cadastrada.")
            return

        filme_obj = self.__controlador_sistema.controlador_filme.pegar_filme_por_titulo(dados_ator["titulo_filme"])
        if not filme_obj:
            self.__tela_ator.mostrar_mensagem("Filme não cadastrado.")
            return

        ano = dados_ator["ano_indicacao"]
        indicados_no_ano = [ator for ator in self.__ator_DAO.get_all() if ator.ano_indicacao == ano]
        if len(indicados_no_ano) >= 5:
            self.__tela_ator.mostrar_mensagem(f"Limite de 5 indicações por ano já atingido para {ano}.")
            return

        ator = Ator(
            nome,
            dados_ator["nacionalidade"],
            categoria_obj,
            filme_obj,
            ano
        )

        self.__ator_DAO.add(ator)
        self.__tela_ator.mostrar_mensagem("Ator adicionado com sucesso!")

    def alterar_dados(self):
        nome_ator = self.__tela_ator.buscar_ator_por_nome()
        ator = self.pegar_ator_por_nome(nome_ator)

        if ator is not None:
            novos_dados_ator = self.__tela_ator.pegar_dados_ator()
            if not novos_dados_ator:
                return

            categoria_obj = self.__controlador_sistema.controlador_categoria.pegar_categoria_por_titulo(novos_dados_ator["categoria"])
            if not categoria_obj:
                self.__tela_ator.mostrar_mensagem(f"Categoria '{novos_dados_ator['categoria']}' não cadastrada.")
                return

            filme_obj = self.__controlador_sistema.controlador_filme.pegar_filme_por_titulo(novos_dados_ator["titulo_filme"])
            if not filme_obj:
                self.__tela_ator.mostrar_mensagem("Filme não cadastrado.")
                return

            self.__ator_DAO.remove(ator.nome)
            novo_nome = novos_dados_ator["nome"].strip().title()
            ator.nome = novo_nome
            ator.nacionalidade = novos_dados_ator["nacionalidade"]
            ator.categoria = categoria_obj
            ator.filme = filme_obj
            ator.ano_indicacao = novos_dados_ator["ano_indicacao"]
            self.__ator_DAO.add(ator)
            self.__tela_ator.mostrar_mensagem("\nDados do ator alterados com sucesso!")
        else:
            self.__tela_ator.mostrar_mensagem("\nAtor não foi indicado.")

    def listar_atores(self):
        atores = self.__ator_DAO.get_all()
        if not atores:
            self.__tela_ator.mostrar_mensagem("Nenhum ator indicado.")
            return

        dados_ator = []
        for ator in atores:
            dados_ator.append({
                "nome": ator.nome,
                "nacionalidade": ator.nacionalidade,
                "categoria": ator.categoria.titulo if hasattr(ator.categoria, 'titulo') else str(ator.categoria),
                "titulo_filme": ator.filme.titulo if hasattr(ator.filme, 'titulo') else str(ator.filme),
                "ano_indicacao": ator.ano_indicacao
            })
        self.__tela_ator.mostrar_ator(dados_ator)

    def remover_ator(self):
        nome = self.__tela_ator.buscar_ator_por_nome()
        ator = self.pegar_ator_por_nome(nome)
        if ator is not None:
            self.__ator_DAO.remove(ator.nome)
            self.__tela_ator.mostrar_mensagem("\nAtor removido com sucesso!")
        else:
            self.__tela_ator.mostrar_mensagem("\nAtor não foi indicado.")

    def gerar_relatorio_por_ano(self):
        ano = self.__tela_ator.buscar_indicados_por_ano()
        try:
            ano = int(ano)
        except (TypeError, ValueError):
            self.__tela_ator.mostrar_mensagem("Ano inválido.")
            return

        atores_filtrados = [ator for ator in self.__ator_DAO.get_all() if ator.ano_indicacao == ano]

        if not atores_filtrados:
            self.__tela_ator.mostrar_mensagem(f"Nenhum ator indicado no ano de '{ano}'.")
            return

        mensagem = f"============= INDICADOS NO ANO DE '{ano}' =============\n"
        for i, ator_filtrado in enumerate(atores_filtrados, 1):
            categoria = ator_filtrado.categoria.titulo if hasattr(ator_filtrado.categoria, 'titulo') else str(ator_filtrado.categoria)
            filme = ator_filtrado.filme.titulo if hasattr(ator_filtrado.filme, 'titulo') else str(ator_filtrado.filme)
            mensagem += f"{i}. Nome: {ator_filtrado.nome}, Nacionalidade: {ator_filtrado.nacionalidade}, Categoria: {categoria}, Filme: {filme}, Ano de Indicação: {ator_filtrado.ano_indicacao}\n"

        self.__tela_ator.mostrar_mensagem(mensagem)

    def retornar_menu(self):
        self.__controlador_sistema.abrir_submenu_indicacoes()

    def abrir_tela_ator(self):
        opcoes = {
            1: self.adicionar_ator,
            2: self.alterar_dados,
            3: self.abrir_filtro,
            4: self.remover_ator,
            0: self.retornar_menu
        }

        continuar = True

        while continuar:
            try:
                opcao = self.__tela_ator.tela_opcoes()
                if opcao in opcoes:
                    opcoes[opcao]()
                else:
                    self.__tela_ator.mostrar_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela_ator.mostrar_mensagem(f"Erro inesperado: {e}")

    def abrir_filtro(self):
        opcoes = {
            1: self.listar_atores,
            2: self.gerar_relatorio_por_ano,
            0: self.abrir_tela_ator
        }

        while True:
            try:
                op = self.__tela_ator.tela_filtros_de_relatorios()
                if op in opcoes:
                    opcoes[op]()
                else:
                    self.__tela_ator.mostrar_mensagem("Opção inválida!")
            except KeyError:
                self.__tela_ator.mostrar_mensagem("Opção inválida!")