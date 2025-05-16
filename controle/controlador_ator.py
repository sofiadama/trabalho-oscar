from tela.tela_ator import TelaAtor

class ControladorAtor:
    def __init__(self, controlador_sistema):
        self.__atores_indicados = []
        self.__tela_ator = TelaAtor()
        self.__controlador_sistema = controlador_sistema

    def adicionar_ator(self, nome: str):
        dados_ator = self.__tela_ator.pegar_dados_ator()
        for ator in self.__atores_indicados:
            if ator.nome == dados_ator["nome"] and ator.filme == dados_ator["filme"]:
                print("Ator já foi cadastrado.")
                return

        ator = Ator(
            dados_ator["nome"], 
            dados_ator["nacionalidade"],
            dados_ator["categoria"],
            dados_ator["filme"],
            dados_ator["ano de indicacao"]
        )

        self.__atores_indicados.append(ator)
    
    def buscar_ator(self, nome: str):
        for ator in self.__atores_indicados:
            if ator.nome == nome:
                return ator
        return None
    
    def alterar_dados(self):
        self.listar_atores()
        nome_ator = self.__tela_ator.selecionar_ator()
        ator = self.buscar_ator(nome_ator)

        if ator is not None:
            novos_dados_ator = self.__tela_ator.pegar_dados_ator()
            ator.nome = novos_dados_ator["nome"]
            ator.nacionalidade = novos_dados_ator["nacionalidade"]
            ator.categoria = novos_dados_ator["categoria"]
            ator.filme = novos_dados_ator["filme"]
            ator.ano_indicacao = novos_dados_ator["ano de indicacao"]
            self.listar_atores()

        else:
            print("Ator não cadastrado.")

    def listar_atores(self):
        for ator in self.__atores_indicados:
            self.__tela_ator.mostrar_dados_ator({
                "nome": ator.nome, 
                "nacionalidade": ator.nacionalidade, 
                "ano de indicacao": ator.ano_indicacao, 
                "filme": ator.filme, 
                "categoria": ator.categoria
            })

    def remover_ator(self, nome: str):
        self.listar_atores()
        ator = self.buscar_ator(nome)
        if ator is None:
            print("Ator não foi cadastrado.")
            return

        self.__atores_indicados.remove(ator)
    
    def retornar_menu(self):
        self.__controlador_sistema.abrir_tela()
    
    def abrir_tela(self):
        opcoes = {
            1: self.adicionar_ator, 
            2: self.alterar_dados, 
            3: self.listar_atores, 
            4: self.remover_ator, 
            0: self.retornar_menu
        }
    
        continuar = True
        while continuar:
            opcoes[self.__tela_ator.tela_opcoes()]()
            
