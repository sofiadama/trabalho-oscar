from tela.tela_diretor import TelaDiretor
from entidade.diretor import Diretor

class ControladorDiretor():
    def __init__(self, controlador_sistema):
        self.__diretores_indicados = []
        self.__tela_diretor = TelaDiretor(controlador_sistema)
        self.__controlador_sistema = controlador_sistema
    
    def pegar_diretor_por_nome(self, nome: str):
        try: #se nao for uma string
            nome = nome.strip().title()
        except AttributeError:
            self.__tela_diretor.mostrar_mensagem("Nome inválido.")
            return None
        
        for diretor in self.__diretores_indicados:
            if diretor.nome.strip().title() == nome:
                return diretor
        
        return None
    
    def pegar_diretores_indicados(self):
        return self.__diretores_indicados

    def adicionar_diretor(self):
        try:
            dados_diretor = self.__tela_diretor.pegar_dados_diretor()
        except Exception as e:
            self.__tela_diretor.mostrar_mensagem(f"Erro ao obter dados do diretor: {e}")
            return

        try:
            for diretor in self.__diretores_indicados:
                if (diretor.nome == dados_diretor["nome"] and 
                    diretor.filme == dados_diretor["filme"]):
                    self.__tela_diretor.mostrar_mensagem("Diretor já foi indicado.")
                    return

            diretor = Diretor(
                dados_diretor["nome"], 
                dados_diretor["nacionalidade"],
                dados_diretor["categoria"],
                dados_diretor["filme"],
                dados_diretor["ano_indicacao"]
            )
            self.__diretores_indicados.append(diretor)
            self.__tela_diretor.mostrar_mensagem("Diretor adicionado com sucesso!")

        except KeyError as e:
            self.__tela_diretor.mostrar_mensagem(f"Dado faltando: {e}")

    def alterar_dados(self):
        try: #pepga qualquer erro de entrada ex se for texto em vez de um int
            nome_diretor = self.__tela_diretor.buscar_diretor_por_nome()
        except Exception as e:
            self.__tela_diretor.mostrar_mensagem(f"Erro ao buscar diretor: {e}")
            return

        diretor = self.pegar_diretor_por_nome(nome_diretor)

        if diretor is None:
            self.__tela_diretor.mostrar_mensagem("Diretor não foi indicado.")
            return

        try:
            novos_dados_diretor = self.__tela_diretor.pegar_dados_diretor()
            diretor.nome = novos_dados_diretor["nome"]
            diretor.nacionalidade = novos_dados_diretor["nacionalidade"]
            diretor.categoria = novos_dados_diretor["categoria"]
            diretor.filme = novos_dados_diretor["filme"]
            diretor.ano_indicacao = novos_dados_diretor["ano_indicacao"]
            self.__tela_diretor.mostrar_mensagem("Dados do diretor alterados com sucesso!")
        except (KeyError, ValueError) as e:
            self.__tela_diretor.mostrar_mensagem(f"Erro ao alterar dados: {e}")

    def listar_diretores(self):
        print("----- DIRETORES INDICADOS -----\n")
        if not self.__diretores_indicados:
            self.__tela_diretor.mostrar_mensagem("Nenhum diretor indicado.")
            return

        for diretor in self.__diretores_indicados:
            try:
                self.__tela_diretor.mostrar_dados_diretor({
                    "nome": diretor.nome, 
                    "nacionalidade": diretor.nacionalidade,
                    "categoria": diretor.categoria,
                    "filme": diretor.filme,
                    "ano_indicacao": diretor.ano_indicacao 
                })
            except Exception as e:
                self.__tela_diretor.mostrar_mensagem(f"Erro ao exibir diretor: {e}")

    def remover_diretor(self):
        try: #se tentar remover quem nao esta na lista 
            nome = self.__tela_diretor.buscar_diretor_por_nome()
        except Exception as e:
            self.__tela_diretor.mostrar_mensagem(f"Erro ao buscar diretor: {e}")
            return

        diretor = self.pegar_diretor_por_nome(nome)

        if diretor is not None:
            try:
                self.__diretores_indicados.remove(diretor)
                self.__tela_diretor.mostrar_mensagem("\nDiretor removido com sucesso!")
            except ValueError:
                self.__tela_diretor.mostrar_mensagem("Erro ao remover diretor.")
        else:
            self.__tela_diretor.mostrar_mensagem("Diretor não foi indicado.")

    def gerar_relatorio_por_ano(self):
        ano = self.__tela_diretor.buscar_indicados_por_ano()
        diretores_filtrados = [diretor for diretor in self.__diretores_indicados if diretor.ano_indicacao == ano]
        
        if not diretores_filtrados:
            self.__tela_diretor.mostrar_mensagem(f"Nenhum diretor indicado no ano de '{ano}'.")
            return
        
        print("." * 15,f"INDICADOS NO ANO DE '{ano}'", "." * 15)
        for diretor_filtrado in diretores_filtrados:
            self.__tela_diretor.mostrar_dados_diretor({
                "nome": diretor_filtrado.nome, 
                "nacionalidade": diretor_filtrado.nacionalidade,
                "categoria": diretor_filtrado.categoria,
                "filme": diretor_filtrado.filme,
                "ano_indicacao": diretor_filtrado.ano_indicacao 
            })

    def retornar_menu(self):
        try:
            self.__controlador_sistema.abrir_submenu_indicacoes()
        except Exception as e:
            self.__tela_diretor.mostrar_mensagem(f"Erro ao retornar ao menu: {e}")
    
    def abrir_tela_diretor(self):
        opcoes = {
            1: self.adicionar_diretor, 
            2: self.alterar_dados, 
            3: self.abrir_filtro, 
            4: self.remover_diretor, 
            0: self.retornar_menu
        }
    
        while True:
            try: #pega qualqer erro de entrada pra opcoes 
                opcao = self.__tela_diretor.tela_opcoes()
                if opcao in opcoes:
                    opcoes[opcao]()
                else:
                    self.__tela_diretor.mostrar_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela_diretor.mostrar_mensagem(f"Erro: {e}")

    def abrir_filtro(self):
        opcoes = {
            1: self.listar_diretores, 
            2: self.gerar_relatorio_por_ano, 
            0: self.abrir_tela_diretor
        }

        while True:
            try:
                opcoes[self.__tela_diretor.tela_filtros_de_relatorios()]()
            except KeyError:
                self.__tela_diretor.mostrar_mensagem("Opção inválida!")

