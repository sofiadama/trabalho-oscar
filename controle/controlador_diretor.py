from tela_diretor import TelaDiretor
from diretor import Diretor

class ControladorDiretor:
   def __init__(self, controlador_sistema):
        self.__diretores = []
        self.__tela_diretor = TelaDiretor()
        self.__controlador_sistema = controlador_sistema

    def buscar_diretor(self, nome: str):
        for diretor in self.__diretores:
            if diretor.nome == nome:
                return diretor
        return None

    def adicionar_diretor(self):
        dados_diretor = self.__tela_diretor.pegar_dados_diretor()
        diretor = Diretor(dados_diretor["nome"], dados_diretor["nacionalidade"], dados_diretor["filme"], dados_diretor["nacionalidade"]), dados_diretor["ano_indicacao"]
        self.__diretores.append(diretor)

    def alterar_diretor(self):
        self.lista_diretores()
        nome_diretor = self.__tela_diretor.buscar_diretor()
        diretor = self.pega_diretor_por_nome(nome_diretor)

        if diretor is not None:
            novos_dados = self.__tela_diretor.pega_dados_diretor()
            diretor.nome = novos_dados["nome"]
            diretor.filme = novos_dados["filme"]
            diretor.nacionalidade = novos_dados["nacionalidade"]
            diretor.ano_indicacao = novos_dados["ano_indicacao"]
            diretor.categoria = novos_dados["categoria"]
            self.lista_diretores()
        else:
            self.__tela_diretor.mostra_mensagem("ATENÇÃO: Diretor não encontrado.")

    def listar_diretores(self):
        if not self.__diretores:
            self.__tela_diretor.mostrar_mensagem("Nenhum diretor cadastrado.")
        for diretor in self.__diretores:
            self.__tela_diretor.mostrar_diretor({
                "nome": diretor.nome,
                "categoria": diretor.categoria
                "filme": diretor.filme
                "ano_indicação": diretor.ano_indicação
                "nacionalidade": diretor.nacionalidade
            })

    def remover_diretor(self):
        self.lista_diretores()
        id_diretor = self.__tela_diretor.seleciona_diretor()
        diretor = self.pega_diretor_por_id(id_diretor)

        if diretor is not None:
            self.__diretores.remover(diretor)
            self.listar_diretores()
        else:
            self.__tela_diretor.mostrar_mensagem("ATENÇÃO: Diretor não encontrado.")

    def retornar_menu(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        opcoes = {
            1: self.incluir_diretor,
            2: self.alterar_diretor,
            3: self.lista_diretores,
            4: self.excluir_diretor,
            0: self.retornar_menu
        }

        while True:
            opcao = self.__tela_diretor.tela_opcoes()
            funcao_escolhida = opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_diretor.mostra_mensagem("Opção inválida.")

