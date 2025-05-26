from tela.tela_ator import TelaAtor
from entidade.ator import Ator
from entidade.filme import Filme

class ControladorAtor():
    def __init__(self, controlador_sistema):
        self.__atores_indicados = []
        self.__tela_ator = TelaAtor(controlador_sistema)
        self.__controlador_sistema = controlador_sistema
    
    def pegar_ator_por_nome(self, nome: str):
        try:   # se nao for uma string
            nome = nome.strip().title()
        except AttributeError:
            self.__tela_ator.mostrar_mensagem("Nome inválido.")
            return None
        
        atores_encontrados = [ator for ator in self.__atores_indicados if ator.nome == nome]
        
        try:
            if len(atores_encontrados) == 1:
                return atores_encontrados[0]
            elif len(atores_encontrados) > 1:
                raise LookupError("Há mais de um ator com esse nome.")
            else:
                raise LookupError("Ator não foi indicado.")
        except LookupError as e:
            self.__tela_ator.mostrar_mensagem(str(e))
            return None

    def pegar_atores_indicados(self):
        return self.__atores_indicados
    
    def adicionar_ator(self):
        dados_ator = self.__tela_ator.pegar_dados_ator()

        # Checa se já existe o ator indicado com mesmo nome e filme
        for ator in self.__atores_indicados:
            if ator.nome == dados_ator["nome"] and ator.filme == dados_ator["filme"]:
                self.__tela_ator.mostrar_mensagem("\nAtor já foi indicado.")
                return
        
        #Limita  indicados para so 5 por ano
        ano = dados_ator["ano_indicacao"]
        indicados_no_ano = [ator for ator in self.__atores_indicados if ator.ano_indicacao == ano]
        if len(indicados_no_ano) >= 5:
            self.__tela_ator.mostrar_mensagem(f"Limite de 5 indicações por ano já atingido para {ano}.")
            return

        ator = Ator(
            dados_ator["nome"], 
            dados_ator["nacionalidade"],
            dados_ator["categoria"],
            dados_ator["filme"],
            dados_ator["ano_indicacao"]
        )

        self.__atores_indicados.append(ator)
        self.__tela_ator.mostrar_mensagem("Ator adicionado com sucesso!")
    
    def alterar_dados(self):
        nome_ator = self.__tela_ator.buscar_ator_por_nome()
        ator = self.pegar_ator_por_nome(nome_ator)

        if ator is not None:
            novos_dados_ator = self.__tela_ator.pegar_dados_ator()
            ator.nome = novos_dados_ator["nome"]
            ator.nacionalidade = novos_dados_ator["nacionalidade"]
            ator.categoria = novos_dados_ator["categoria"]
            ator.filme = novos_dados_ator["filme"]
            ator.ano_indicacao = novos_dados_ator["ano_indicacao"]
            self.__tela_ator.mostrar_mensagem("\nDados do ator alterados com sucesso!")

        else:
            self.__tela_ator.mostrar_mensagem("\nAtor não foi indicado.")

    def listar_atores(self):
        print("----- ATORES INDICADOS -----\n")
        if not self.__atores_indicados:
            self.__tela_ator.mostrar_mensagem("Nenhum ator indicado.")
            return

        for ator in self.__atores_indicados:
            self.__tela_ator.mostrar_dados_ator({
                "nome": ator.nome, 
                "nacionalidade": ator.nacionalidade,
                "categoria": ator.categoria,
                "filme": ator.filme,
                "ano_indicacao": ator.ano_indicacao 
            })

    def remover_ator(self):
        nome = self.__tela_ator.buscar_ator_por_nome()
        ator = self.pegar_ator_por_nome(nome)

        if ator is not None:
            self.__atores_indicados.remove(ator)
            self.__tela_ator.mostrar_mensagem("\nAtor removido com sucesso!")
        else:
            self.__tela_ator.mostrar_mensagem("\nAtor não foi indicado.")

    def gerar_relatorio_por_ano(self):
        ano = self.__tela_ator.buscar_indicados_por_ano()
        atores_filtrados = [ator for ator in self.__atores_indicados if ator.ano_indicacao == ano]
        
        if not atores_filtrados:
            self.__tela_ator.mostrar_mensagem(f"Nenhum ator indicado no ano de '{ano}'.")
            return
        
        print("." * 15,f"INDICADOS NO ANO DE '{ano}'", "." * 15)
        for ator_filtrado in atores_filtrados:
            self.__tela_ator.mostrar_dados_ator({
                "nome": ator_filtrado.nome, 
                "nacionalidade": ator_filtrado.nacionalidade,
                "categoria": ator_filtrado.categoria,
                "filme": ator_filtrado.filme,
                "ano_indicacao": ator_filtrado.ano_indicacao 
            })
    
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
            try: #pega qualquer erro durante a execucao da tela de opcoes 
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
                opcoes[self.__tela_ator.tela_filtros_de_relatorios()]()
            except KeyError:
                self.__tela_ator.mostrar_mensagem("Opção inválida!")
