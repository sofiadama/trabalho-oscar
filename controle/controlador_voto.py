from tela.tela_voto import TelaVoto
from controle.controlador_membro import ControladorMembro

class ControladorVoto(ControladorMembro):
    def __init__(self, controlador_sistema):
        super().__init__(self)
        self.__membro_autenticado = None
        self.__votos = []
        self.__tela_voto = TelaVoto()
        self.__controlador_sistema = controlador_sistema

    @property
    def membro_autenticado(self):
        return self.__membro_autenticado
    
    def autenticar_membro(self):
        if self.__membro_autenticado is not None: # verifica se HÁ membro autenticado (!= None)
            return True

        id_membro = self.__tela_voto.autenticacao_membro()
        for membro in super().pegar_lista_membros():
            if membro.id == id_membro:
                self.__membro_autenticado = membro
                return True
        
            self.__tela_voto.mostrar_mensagem("Membro não cadastrado.")
            return False

    def listar_votos_gerais(self):
        print("----- VOTOS GERAIS -----\n")
        for voto in self.__votos:
            self.__tela_voto.mostrar_dados_voto({
                "membro": voto.membro, 
                "indicado": voto.indicado,
                "categoria": voto.categoria,
                "ano": voto.ano
            })

        if self.__votos == []:
            self.__tela_voto.mostrar_mensagem("Nenhum voto registrado.")
    
    def pegar_lista_votos(self):
        return self.__votos

    def retornar_menu(self):
        self.__controlador_sistema.abrir_tela_votos()
