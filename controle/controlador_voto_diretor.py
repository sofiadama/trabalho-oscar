from tela.tela_voto import TelaVoto
from entidade.voto_diretor import VotoDiretor
from controle.controlador_voto import ControladorVoto

class ControladorVotoDiretor(ControladorVoto):
    def __init__(self, controlador_sistema):
        super().__init__(self)
        self.__votos_em_diretores = []
        self.__tela_voto = TelaVoto()
        self.__controlador_sistema = controlador_sistema

    def pegar_voto_por_categoria(self, categoria):
        for voto in self.__votos_em_diretores:
            if voto.categoria == categoria:
                return voto
        return None

    def adicionar_voto(self):
        self.autenticar_membro(self.__controlador_membro.__membros)
        dados_voto = self.__tela_voto.pegar_dados_voto()
        for voto in self.__votos_em_diretores:
            if voto.membro == dados_voto["membro"] and voto.categoria == dados_voto["categoria"]:
                print("Você já votou nesta categoria.")
                return

        voto = VotoDiretor(
            self.__membro_autenticado, 
            dados_voto["indicado"],
            dados_voto["categoria"],
            dados_voto["ano"]
        )

        self.__votos_em_diretores.append(voto)
        super().pegar_lista_votos().append(voto)
    
    def alterar_voto(self):
        categoria_voto = self.__tela_voto.buscar_voto()
        voto = self.pegar_voto_por_categoria(categoria_voto)

        if voto is not None:
            novos_dados_voto = self.__tela_voto.pegar_dados_voto()
            voto.membro = novos_dados_voto["membro"]
            voto.indicado = novos_dados_voto["indicado"]
            voto.categoria = novos_dados_voto["categoria"]
            voto.ano = novos_dados_voto["ano"]
    
            self.listar_votos_em_atores()

        else:
            self.__tela_voto.mostrar_mensagem("\nVoto não foi registrado.")

    def listar_votos_em_diretores(self):
        print("----- VOTOS EM DIRETORES -----\n")
        for voto in self.__votos_em_diretores:
            self.__tela_voto.mostrar_dados_voto({
                "membro": voto.membro, 
                "indicado": voto.indicado,
                "categoria": voto.categoria,
                "ano": voto.ano
            })

        if self.__votos_em_diretores == []:
            self.__tela_voto.mostrar_mensagem("Nenhum voto em diretor registrado.")

    def remover_voto(self):
        self.__tela_voto.buscar_voto()
        voto = self.pegar_voto_por_categoria(voto)

        if voto is not None:
            self.__votos_em_diretores.remove(voto)
            self.__tela_voto.mostrar_mensagem("\nVoto removido com sucesso!")
        else:
            self.__tela_voto.mostrar_mensagem("\nVoto não foi registrado.")
    
    def retornar_menu(self):
        self.__controlador_sistema.abrir_tela_votos()
    
    def abrir_tela_voto_diretor(self):
        opcoes = {
            1: self.adicionar_voto, 
            2: self.alterar_voto, 
            3: self.listar_votos_em_diretores, 
            4: self.remover_voto, 
            0: self.retornar_menu
        }
    
        continuar = True
        while continuar:
            opcoes[self.__tela_voto.tela_votos_em_diretores()]()
