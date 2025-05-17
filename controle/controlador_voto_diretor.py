from controle.controlador_voto import ControladorVoto
from controle.controlador_diretor import ControladorDiretor
from controle.controlador_membro import ControladorMembro
from tela.tela_voto import TelaVoto

class ControladorVotoDiretor(ControladorVoto):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__controlador_sistema = controlador_sistema
        self.__tela_voto = TelaVoto()
        self.__votos = {}  # chave: id_membro, valor: lista de votos

    def autentificar_membro(self):
        id_membro = self.__tela_voto.autentificacao_membro()
        membros = self.__controlador_sistema.controlador_membro.lista_membros()
        for membro in membros:
            if membro.id == id_membro:
                return membro
        self.__tela_voto.mostra_mensagem("Membro não encontrado.")
        return None

    def verificar_duplicidade_voto(self, id_membro, ano):
        if id_membro in self.__votos:
            for voto in self.__votos[id_membro]:
                if voto["ano"] == ano:
                    self.__tela_voto.mostra_mensagem("Você já votou neste ano.")
                    return True
        return False

    def mostrar_diretores_indicados(self):
        diretores = self.__controlador_sistema.controlador_diretor.listar_diretores()
        for diretor in diretores:
            print(f"ID: {diretor.id} | Nome: {diretor.nome}")

    def adicionar_voto(self):
        membro = self.autentificar_membro()
        if not membro:
            return
        dados_voto = self.__tela_voto.pegar_dados_voto()
        if self.verificar_duplicidade_voto(membro.id, dados_voto["ano"]):
            return
        if membro.id not in self.__votos:
            self.__votos[membro.id] = []
        self.__votos[membro.id].append(dados_voto)
        self.__tela_voto.mostra_mensagem("Voto registrado com sucesso!")

    def alterar_voto(self):
        membro = self.autentificar_membro()
        if not membro or membro.id not in self.__votos:
            self.__tela_voto.mostra_mensagem("Nenhum voto encontrado.")
            return
        ano = input("Digite o ano do voto que deseja alterar: ")
        for voto in self.__votos[membro.id]:
            if voto["ano"] == ano:
                novo_voto = self.__tela_voto.pegar_dados_voto()
                voto.update(novo_voto)
                self.__tela_voto.mostra_mensagem("Voto alterado com sucesso!")
                return
        self.__tela_voto.mostra_mensagem("Voto não encontrado para o ano informado.")

    def listar_votos(self):
        for id_membro, votos in self.__votos.items():
            print(f"Membro ID: {id_membro}")
            for voto in votos:
                self.__tela_voto.mostrar_voto(voto)

    def remover_voto(self):
        membro = self.autentificar_membro()
        if not membro or membro.id not in self.__votos:
            self.__tela_voto.mostra_mensagem("Nenhum voto encontrado.")
            return
        ano = input("Digite o ano do voto que deseja remover: ")
        votos_membro = self.__votos[membro.id]
        for voto in votos_membro:
            if voto["ano"] == ano:
                votos_membro.remove(voto)
                self.__tela_voto.mostra_mensagem("Voto removido com sucesso!")
                return
        self.__tela_voto.mostra_mensagem("Voto não encontrado para o ano informado.")
