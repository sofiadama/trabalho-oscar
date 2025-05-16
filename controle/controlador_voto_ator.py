from controle.controlador_voto import ControladorVoto
from controle.controlador_ator import ControladorAtor
from controle.controlador_membro import ControladorMembro
from tela.tela_voto import TelaVoto

class ControladorVotoAtor(ControladorVoto):
    def __init__(self, controlador_sistema):
        super().__init__()
        self.__controlador_sistema = controlador_sistema

    def autentificar_membro(self, membro):
        membro = tela_voto.autentificacao_membro()
        for membro in self.__membros_cadastrados:
            if(membro.id != id):
                print("Membro não cadastrado.")
                return
            else:
                return
        
    def verificar_duplicidade_voto(self, id_membro, categoria):
        dados_voto = self.__tela_voto.pega_dados_voto()
        # membro_id acessa os votos do membro com id especifico
        for voto in self.__votos[id_membro]:
            if voto.categoria == dados_voto["categoria"]:
                print("O membro/você já votou nesta categoria.")
                return
    
    def mostrar_atores_indicados():
        indicados = ControladorAtor.listar_atores()

    def adicionar_voto():
        pass

    def alterar_voto():
        pass
    
    def listar_votos():
        pass

    def remover_voto():
        pass