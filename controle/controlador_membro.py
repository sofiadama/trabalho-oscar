from tela.tela_membro import TelaMembro
from entidade.membro import Membro

class ControladorMembro():
    def __init__(self, controlador_sistema):
        self.__membros_cadastrados = []
        self.__tela_membro = TelaMembro()
        self.__controlador_sistema = controlador_sistema

    def adicionar_membro(self, nome: str):
        for membro in self.__membros_cadastrados:
            if membro.id == membro["id"]:
                print("Membro já foi cadastrado.")
                return

        dados_membro = self.__tela_membro.pegar_dados_membro()
        membro = Membro(dados_membro["nome"], dados_membro["id"], dados_membro["nascimento"], dados_membro["nacionalidade"])
        self.__membros_cadastrados.append(membro)
    
    def buscar_membro(self, id: int):
        for membro in self.__membros_cadastrados:
            if(membro.id == id):
                return membro
        return None
    
    def alterar_dados(self):
        self.listar_membros()
        nome_membro = self.__tela_membro.selecionar_membro()
        membro = self.buscar_membro(nome_membro)

        if(membro is not None):
            novos_dados_membro = self.__tela_membro.pegar_dados_membro()
            membro.nome = novos_dados_membro["nome"]
            membro.id = novos_dados_membro["id"]
            membro.nascimento = novos_dados_membro["nascimento"]
            membro.nacionalidade = novos_dados_membro["nacionalidade"]
            self.listar_membros()

        else:
            return "Membro não cadastrado."

    def listar_membros(self):
        for membro in self.__membros_cadastrados:
            self.__tela_membro.mostrar_dados_membro({"nome": membro.nome, "id": membro.id, "nascimento": membro.nascimento, "nacionalidade": membro.nacionalidade})

    def remover_membro(self, nome: str):
        self.listar_membros()
        if nome.membro not in self.__membros_cadastrados:
            print("Membro não foi cadastrado.")
            return

        self.__membros_cadastrados = [membro for membro in self.__membros_cadastrados if membro.get("membro") != nome]
    
    def retornar_menu(self):
        self.__controlador_sistema.abrir_tela_principal()
    
    def abrir_tela(self):
        opcoes = {1: self.adicionar_membro, 2: self.alterar_dados, 3: self.listar_membros, 4: self.remover_membro, 0: self.retornar_menu}
    
        continuar = True
        while continuar:
            opcoes[self.__tela_membro.tela_opcoes()]()