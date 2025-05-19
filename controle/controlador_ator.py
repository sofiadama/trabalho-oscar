from tela.tela_ator import TelaAtor
from entidade.ator import Ator

class ControladorAtor():
    def __init__(self, controlador_sistema):
        self.__atores_indicados = []
        self.__tela_ator = TelaAtor()
        self.__controlador_sistema = controlador_sistema
    
    def pegar_ator_por_nome(self, nome: str):
        for ator in self.__atores_indicados:
            if ator.nome == nome:
                return ator
            elif self.__atores_indicados.count(ator) > 1:
                self.__tela_ator.mostrar_mensagem("Há mais de um ator com esse nome.")
        return None

    # adicionar funçao de comparar/buscar atores por filme 

    def adicionar_ator(self):
        dados_ator = self.__tela_ator.pegar_dados_ator()
        for ator in self.__atores_indicados:
            if ator.nome == dados_ator["nome"] and ator.filme == dados_ator["filme"]:
                print("\nAtor já foi indicado.")
                return

        ator = Ator(
            dados_ator["nome"], 
            dados_ator["nacionalidade"],
            dados_ator["categoria"],
            dados_ator["filme"],
            dados_ator["ano de indicacao"]
        )

        self.__atores_indicados.append(ator)
    
    # limitar indicados para 5 por ANO
    
    def alterar_dados(self):
        nome_ator = self.__tela_ator.buscar_ator()
        ator = self.pegar_ator_por_nome(nome_ator)

        if ator is not None:
            novos_dados_ator = self.__tela_ator.pegar_dados_ator()
            ator.nome = novos_dados_ator["nome"]
            ator.nacionalidade = novos_dados_ator["nacionalidade"]
            ator.categoria = novos_dados_ator["categoria"]
            ator.filme = novos_dados_ator["filme"]
            ator.ano_indicacao = novos_dados_ator["ano de indicacao"]
            self.listar_atores()

        else:
            self.__tela_ator.mostrar_mensagem("\nAtor não foi indicado.")

    def listar_atores(self):
        print("----- ATORES INDICADOS -----\n")
        for ator in self.__atores_indicados:
            self.__tela_ator.mostrar_dados_ator({
                "nome": ator.nome, 
                "nacionalidade": ator.nacionalidade,
                "categoria": ator.categoria,
                "filme": ator.filme,
                "ano de indicacao": ator.ano_indicacao 
            })

        if self.__atores_indicados == []:
            self.__tela_ator.mostrar_mensagem("Nenhum ator indicado.")

    def remover_ator(self):
        nome = self.__tela_ator.buscar_ator()
        ator = self.pegar_ator_por_nome(nome)

        if ator is not None:
            self.__atores_indicados.remove(ator)
            self.__tela_ator.mostrar_mensagem("\nAtor removido com sucesso!")
        else:
            self.__tela_ator.mostrar_mensagem("\nAtor não foi indicado.")
    
    def retornar_menu(self):
        self.__controlador_sistema.abrir_tela_indicacoes()
    
    def abrir_tela_ator(self):
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
