from controle.controlador_voto import ControladorVoto
from tela.tela_voto import TelaVoto
from voto_filme import VotoFilme

class ControladorVotoFilme(ControladorVoto):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__controlador_sistema = controlador_sistema
        self.__tela_voto = TelaVoto()
        self.__votos = {}  

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
                if voto.ano == ano:
                    self.__tela_voto.mostra_mensagem("Você já votou neste ano.")
                    return True
        return False

    def mostrar_filmes_indicados(self):
        filmes = self.__controlador_sistema.controlador_filme.listar_filmes()
        for i, filme in enumerate(filmes):
            print(f"{i+1}. {filme.titulo} | Diretor: {filme.diretor.nome} | Categoria: {filme.categoria.nome}")
        return filmes

    def adicionar_voto(self):
        membro = self.autentificar_membro()
        if not membro:
            return
        filmes = self.mostrar_filmes_indicados()
        escolha = self.__tela_voto.pegar_opcao("Escolha o número do filme: ")
        ano = self.__tela_voto.pegar_opcao("Informe o ano do voto: ")

        try:
            filme = filmes[int(escolha) - 1]
            ano = int(ano)
        except (IndexError, ValueError):
            self.__tela_voto.mostra_mensagem("Escolha inválida.")
            return

        if self.verificar_duplicidade_voto(membro.id, ano):
            return

        voto = VotoFilme(membro, filme, ano)
        if membro.id not in self.__votos:
            self.__votos[membro.id] = []
        self.__votos[membro.id].append(voto)
        self.__tela_voto.mostra_mensagem("Voto registrado com sucesso!")

    def alterar_voto(self):
        membro = self.autentificar_membro()
        if not membro or membro.id not in self.__votos:
            self.__tela_voto.mostra_mensagem("Nenhum voto encontrado.")
            return
        ano = int(self.__tela_voto.pegar_opcao("Digite o ano do voto que deseja alterar: "))
        for voto in self.__votos[membro.id]:
            if voto.ano == ano:
                filmes = self.mostrar_filmes_indicados()
                nova_escolha = self.__tela_voto.pegar_opcao("Escolha o novo filme: ")
                try:          #seleciona um  filme da lista a partir da entrada do usuario
                    novo_filme = filmes[int(nova_escolha) - 1]
                except (IndexError, ValueError):
                    self.__tela_voto.mostra_mensagem("Escolha inválida.")
                    return
                voto.indicado = novo_filme
                self.__tela_voto.mostra_mensagem("Voto alterado com sucesso!")
                return
        self.__tela_voto.mostra_mensagem("Voto não encontrado para o ano informado.")

    def listar_votos(self):
        for id_membro, votos in self.__votos.items():
            print(f"\nMembro ID: {id_membro}")
            for voto in votos:
                print(f"Ano: {voto.ano} | Filme: {voto.indicado.titulo}")

    def remover_voto(self):
        membro = self.autentificar_membro()
        if not membro or membro.id not in self.__votos:
            self.__tela_voto.mostra_mensagem("Nenhum voto encontrado.")
            return
        ano = int(self.__tela_voto.pegar_opcao("Digite o ano do voto que deseja remover: "))
        votos_membro = self.__votos[membro.id]
        for voto in votos_membro:
            if voto.ano == ano:
                votos_membro.remove(voto)
                self.__tela_voto.mostra_mensagem("Voto removido com sucesso!")
                return
        self.__tela_voto.mostra_mensagem("Voto não encontrado para o ano informado.")
