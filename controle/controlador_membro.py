from tela.tela_membro import TelaMembro
from entidade.membro import Membro

class ControladorMembro():
    def __init__(self, controlador_sistema):
        self.__membros = []
        self.__tela_membro = TelaMembro()
        self.__controlador_sistema = controlador_sistema
    
    def pegar_membro_por_id(self, id: int):
        for membro in self.__membros:
            if membro.id == id:
                return membro
            elif self.__membros.count(membro) > 1:
                self.__tela_membro.mostrar_mensagem("Há mais de um membro com esse id.")
        return None

    def adicionar_membro(self):
        dados_membro = self.__tela_membro.pegar_dados_membro()
        for membro in self.__membros:
            if membro.id == dados_membro["id"] and membro.nome == dados_membro["nome"]:
                print("\nMembro já foi cadastrado.")
                return

        membro = Membro(
            dados_membro["id"], 
            dados_membro["nome"],
            dados_membro["nascimento"],
            dados_membro["nacionalidade"]
        )

        self.__membros.append(membro)
    
    def alterar_dados(self):
        id_membro = self.__tela_membro.buscar_membro()
        membro = self.pegar_membro_por_id(id_membro)

        if membro is not None:
            novos_dados_membro = self.__tela_membro.pegar_dados_membro()
            membro.id = novos_dados_membro["id"]
            membro.nome = novos_dados_membro["nome"]
            membro.nascimento = novos_dados_membro["nascimento"]
            membro.nacionalidade = novos_dados_membro["nacionalidade"]
            self.listar_membros()

        else:
            self.__tela_membro.mostrar_mensagem("\nMembro não foi cadastrado.")

    def listar_membros(self):
        print("----- MEMBROS DA ACADEMIA -----\n")
        for membro in self.__membros:
            self.__tela_membro.mostrar_dados_membro({
                "id": membro.id, 
                "nome": membro.nome,
                "nascimento": membro.nascimento,
                "nacionalidade": membro.nacionalidade
            })

        if self.__membros == []:
            self.__tela_membro.mostrar_mensagem("Nenhum membro cadastrado.")

    def remover_membro(self):
        id = self.__tela_membro.buscar_membro()
        membro = self.pegar_membro_por_id(id)

        if membro is not None:
            self.__membros.remove(membro)
            self.__tela_membro.mostrar_mensagem("\nMembro removido com sucesso!")
        else:
            self.__tela_membro.mostrar_mensagem("\nMembro não foi cadastrado.")
    
    def pegar_lista_membros(self):
        return self.__membros

    def retornar_menu(self):
        self.__controlador_sistema.abrir_tela_cadastros()
    
    def abrir_tela_membro(self):
        opcoes = {
            1: self.adicionar_membro, 
            2: self.alterar_dados, 
            3: self.listar_membros, 
            4: self.remover_membro, 
            0: self.retornar_menu
        }
    
        continuar = True
        while continuar:
            opcoes[self.__tela_membro.tela_opcoes()]()
