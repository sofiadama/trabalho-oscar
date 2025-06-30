from tela.tela_diretor import TelaDiretor
from entidade.diretor import Diretor
from DAOs.diretor_dao import DiretorDAO

class ControladorDiretor():
    def __init__(self, controlador_sistema):
        self.__diretor_DAO = DiretorDAO()
        self.__tela_diretor = TelaDiretor()
        self.__controlador_sistema = controlador_sistema

    def pegar_diretor_por_nome(self, nome: str):
        try:
            nome = nome.strip().title()
        except AttributeError:
            self.__tela_diretor.mostra_mensagem("Nome inválido.")
            return None

        diretor = self.__diretor_DAO.get(nome)
        if diretor is not None:
            return diretor
        else:
            self.__tela_diretor.mostra_mensagem("Diretor não foi indicado.")
            return None

    def pegar_diretores_indicados(self):
        return self.__diretor_DAO.get_all()

    def adicionar_diretor(self):
        try:
            dados_diretor = self.__tela_diretor.pegar_dados_diretor()
            if not dados_diretor:
                return
        except Exception as e:
            self.__tela_diretor.mostra_mensagem(f"Erro ao obter dados do diretor: {e}")
            return

        nome = dados_diretor["nome"].strip().title()
        if self.__diretor_DAO.get(nome) is not None:
            self.__tela_diretor.mostra_mensagem("Diretor já foi indicado.")
            return

        categoria_obj = self.__controlador_sistema.controlador_categoria.pegar_categoria_por_titulo("Melhor Diretor")
        if not categoria_obj:
            self.__tela_diretor.mostra_mensagem("Categoria 'Melhor Diretor' não cadastrada.")
            return

        filme_obj = self.__controlador_sistema.controlador_filme.pegar_filme_por_titulo(dados_diretor["titulo_filme"])
        if not filme_obj:
            self.__tela_diretor.mostra_mensagem("Filme não cadastrado.")
            return

        diretor = Diretor(
            nome,
            dados_diretor["nacionalidade"],
            categoria_obj,
            filme_obj,  
            dados_diretor["ano_indicacao"]
        )
        self.__diretor_DAO.add(diretor)
        self.__tela_diretor.mostra_mensagem("Diretor adicionado com sucesso!")

    def alterar_dados(self):
        try:
            nome_diretor = self.__tela_diretor.buscar_diretor()
            if not nome_diretor:
                return
        except Exception as e:
            self.__tela_diretor.mostra_mensagem(f"Erro ao buscar diretor: {e}")
            return

        diretor = self.pegar_diretor_por_nome(nome_diretor)
        if diretor is None:
            self.__tela_diretor.mostra_mensagem("Diretor não foi indicado.")
            return

        try:
            novos_dados_diretor = self.__tela_diretor.pegar_dados_diretor()
            if not novos_dados_diretor:
                return

            categoria_obj = self.__controlador_sistema.controlador_categoria.pegar_categoria_por_titulo("Melhor Diretor")
            if not categoria_obj:
                self.__tela_diretor.mostra_mensagem("Categoria 'Melhor Diretor' não cadastrada.")
                return

            filme_obj = self.__controlador_sistema.controlador_filme.pegar_filme_por_titulo(novos_dados_diretor["titulo_filme"])
            if not filme_obj:
                self.__tela_diretor.mostra_mensagem("Filme não cadastrado.")
                return

            self.__diretor_DAO.remove(diretor.nome)
            novo_nome = novos_dados_diretor["nome"].strip().title()
            diretor.nome = novo_nome
            diretor.nacionalidade = novos_dados_diretor["nacionalidade"]
            diretor.categoria = categoria_obj
            diretor.filme = filme_obj
            diretor.ano_indicacao = novos_dados_diretor["ano_indicacao"]
            self.__diretor_DAO.add(diretor)
            self.__tela_diretor.mostra_mensagem("Dados do diretor alterados com sucesso!")
        except (KeyError, ValueError) as e:
            self.__tela_diretor.mostra_mensagem(f"Erro ao alterar dados: {e}")

    def listar_diretores(self):
        diretores = self.__diretor_DAO.get_all()
        if not diretores:
            self.__tela_diretor.mostra_mensagem("Nenhum diretor indicado.")
            return

        dados_diretor = []
        for diretor in diretores:
            dados_diretor.append({
                "nome": diretor.nome,
                "nacionalidade": diretor.nacionalidade,
                "categoria": diretor.categoria.titulo,
                "titulo_filme": diretor.filme.titulo,
                "ano_indicacao": diretor.ano_indicacao
            })
        self.__tela_diretor.mostrar_diretor(dados_diretor)

    def remover_diretor(self):
        try:
            nome = self.__tela_diretor.buscar_diretor()
            if not nome:
                return
        except Exception as e:
            self.__tela_diretor.mostra_mensagem(f"Erro ao buscar diretor: {e}")
            return

        diretor = self.pegar_diretor_por_nome(nome)
        if diretor is not None:
            self.__diretor_DAO.remove(diretor.nome)
            self.__tela_diretor.mostra_mensagem("\nDiretor removido com sucesso!")
        else:
            self.__tela_diretor.mostra_mensagem("Diretor não foi indicado.")

    def gerar_relatorio_por_ano(self):
        ano = self.__tela_diretor.buscar_indicados_por_ano()
        try:
            ano = int(ano)
        except (TypeError, ValueError):
            self.__tela_diretor.mostra_mensagem("Ano inválido.")
            return

        diretores_filtrados = [diretor for diretor in self.__diretor_DAO.get_all() if diretor.ano_indicacao == ano]

        if not diretores_filtrados:
            self.__tela_diretor.mostra_mensagem(f"Nenhum diretor indicado no ano de '{ano}'.")
            return

        mensagem = f"............... INDICADOS NO ANO DE '{ano}' ...............\n"
        for i, diretor_filtrado in enumerate(diretores_filtrados, 1):
            mensagem += f"{i}. Nome: {diretor_filtrado.nome}, Nacionalidade: {diretor_filtrado.nacionalidade}, Categoria: {diretor_filtrado.categoria.titulo}, Filme: {diretor_filtrado.filme.titulo}, Ano de Indicação: {diretor_filtrado.ano_indicacao}\n"

        self.__tela_diretor.mostra_mensagem(mensagem)

    def retornar_menu(self):
        try:
            self.__controlador_sistema.abrir_submenu_indicacoes()
        except Exception as e:
            self.__tela_diretor.mostra_mensagem(f"Erro ao retornar ao menu: {e}")

    def abrir_tela_diretor(self):
        opcoes = {
            1: self.adicionar_diretor,
            2: self.alterar_dados,
            3: self.abrir_filtro,
            4: self.remover_diretor,
            0: self.retornar_menu
        }

        while True:
            try:
                opcao = self.__tela_diretor.tela_opcoes()
                if opcao in opcoes:
                    opcoes[opcao]()
                else:
                    self.__tela_diretor.mostra_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela_diretor.mostra_mensagem(f"Erro: {e}")

    def abrir_filtro(self):
        opcoes = {
            1: self.listar_diretores,
            2: self.gerar_relatorio_por_ano,
            0: self.abrir_tela_diretor
        }

        while True:
            try:
                op = self.__tela_diretor.tela_filtros_de_relatorios()
                if op in opcoes:
                    opcoes[op]()
                else:
                    self.__tela_diretor.mostra_mensagem("Opção inválida!")
            except KeyError:
                self.__tela_diretor.mostra_mensagem("Opção inválida!")