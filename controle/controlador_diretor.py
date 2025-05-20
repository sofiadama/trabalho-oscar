from tela.tela__diretor import TelaDiretor
from entidade.diretor import Diretor

class ControladorDiretor():
    def __init__(self, controlador_sistema):
        self.__diretores_indicados = []
        self.__tela_diretor = TelaDiretor()
        self.__controlador_sistema = controlador_sistema
    
    def pegar_diretor_por_nome(self, nome: str):
        for diretor in self.__diretores_indicados:
            if diretor.nome == nome:
                return diretor
            elif self.__diretores_indicados.count(diretor) > 1:
                self.__tela_diretor.mostrar_mensagem("Há mais de um diretor com esse nome.")
        return None

    def adicionar_diretor(self):
        dados_diretor = self.__tela_diretor.pegar_dados_diretor()
        for diretor in self.__diretores_indicados:
            if diretor.nome == dados_diretor["nome"] and diretor.filme == dados_diretor["filme"]:
                print("\nDiretor já foi indicado.")
                return

        diretor = Diretor(
            dados_diretor["nome"], 
            dados_diretor["nacionalidade"],
            dados_diretor["categoria"],
            dados_diretor["filme"],
            dados_diretor["ano de indicacao"]
        )

        self.__diretores_indicados.append(diretor)
    
    def alterar_dados(self):
        nome_diretor = self.__tela_diretor.buscar_diretor()
        diretor = self.pegar_diretor_por_nome(nome_diretor)

        if diretor is not None:
            novos_dados_diretor = self.__tela_diretor.pegar_dados_diretor()
            diretor.nome = novos_dados_diretor["nome"]
            diretor.nacionalidade = novos_dados_diretor["nacionalidade"]
            diretor.categoria = novos_dados_diretor["categoria"]
            diretor.filme = novos_dados_diretor["filme"]
            diretor.ano_indicacao = novos_dados_diretor["ano de indicacao"]
            self.listar_diretores()

        else:
            self.__tela_diretor.mostrar_mensagem("\nDiretor não foi indicado.")

    def listar_diretores(self):
        print("----- DIRETORES INDICADOS -----\n")
        for diretor in self.__diretores_indicados:
            self.__tela_diretor.mostrar_dados_diretor({
                "nome": diretor.nome, 
                "nacionalidade": diretor.nacionalidade,
                "categoria": diretor.categoria,
                "filme": diretor.filme,
                "ano de indicacao": diretor.ano_indicacao 
            })

        if self.__diretores_indicados == []:
            self.__tela_diretor.mostrar_mensagem("Nenhum diretor indicado.")

    def remover_diretor(self):
        nome = self.__tela_diretor.buscar_diretor()
        diretor = self.pegar_diretor_por_nome(nome)

        if diretor is not None:
            self.__diretores_indicados.remove(diretor)
            self.__tela_diretor.mostrar_mensagem("\nDiretor removido com sucesso!")
        else:
            self.__tela_diretor.mostrar_mensagem("\nDiretor não foi indicado.")
    
    def retornar_menu(self):
        self.__controlador_sistema.abrir_tela_indicacoes()
    
    def abrir_tela_diretor(self):
        opcoes = {
            1: self.adicionar_diretor, 
            2: self.alterar_dados, 
            3: self.listar_diretores, 
            4: self.remover_diretor, 
            0: self.retornar_menu
        }
    
        continuar = True
        while continuar:
            opcoes[self.__tela_diretor.tela_opcoes()]()

