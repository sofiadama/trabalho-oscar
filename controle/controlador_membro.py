from tela.tela_membro import TelaMembro
from entidade.membro import Membro

class ControladorMembro():
    def __init__(self, controlador_sistema):
        self.__membros = []
        self.__tela_membro = TelaMembro()
        self.__controlador_sistema = controlador_sistema
    
    def pegar_membro_por_id(self, id: int):
        try:
            membros_encontrados = [m for m in self.__membros if m.id == id]

            if not membros_encontrados:
                raise (f"Membro com ID {id} não encontrado.")
            if len(membros_encontrados) > 1:
                self.__tela_membro.mostrar_mensagem("Há mais de um membro com esse id.")
        except AttributeError as e:
            self.__tela_membro.mostrar_mensagem(str(e))
                    
        return membros_encontrados[0]

    def adicionar_membro(self):
        try:
            dados_membro = self.__tela_membro.pegar_dados_membro()
            for membro in self.__membros:
                if membro.id == dados_membro["id"] and membro.nome == dados_membro["nome"]:
                    raise Exception("Membro já foi cadastrado.")

            membro = Membro(
                dados_membro["id"], 
                dados_membro["nome"],
                dados_membro["nascimento"],
                dados_membro["nacionalidade"]
            )
            self.__membros.append(membro)
            self.__tela_membro.mostrar_mensagem("\nMembro cadastrado com sucesso!")
        except AttributeError as e:
            self.__tela_membro.mostrar_mensagem(str(e))

    def alterar_dados(self):
        try:
            id_membro = self.__tela_membro.buscar_membro()
            membro = self.pegar_membro_por_id(id_membro)

            novos_dados_membro = self.__tela_membro.pegar_dados_membro()
            membro.id = novos_dados_membro["id"]
            membro.nome = novos_dados_membro["nome"]
            membro.nascimento = novos_dados_membro["nascimento"]
            membro.nacionalidade = novos_dados_membro["nacionalidade"]
            self.__tela_membro.mostrar_mensagem("\nDados alterados com sucesso!")
            
        except AttributeError as e:
            self.__tela_membro.mostrar_mensagem(str(e))

    def listar_membros(self):
        if not self.__membros:
            self.__tela_membro.mostrar_mensagem("Nenhum membro cadastrado.")
            return

        print("----- MEMBROS DA ACADEMIA -----\n")
        for membro in self.__membros:
            self.__tela_membro.mostrar_dados_membro({
                "id": membro.id, 
                "nome": membro.nome,
                "nascimento": membro.nascimento,
                "nacionalidade": membro.nacionalidade
            })

    def remover_membro(self):
        try:
            id = self.__tela_membro.buscar_membro()
            membro = self.pegar_membro_por_id(id)
            self.__membros.remove(membro)
            self.__tela_membro.mostrar_mensagem("\nMembro removido com sucesso!")
        except AttributeError as e:
            self.__tela_membro.mostrar_mensagem(str(e))
    
    def pegar_lista_membros(self):
        return self.__membros

    def retornar_menu(self):
        self.__controlador_sistema.abrir_submenu_cadastros()
    
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
            try:
                opcao = self.__tela_membro.tela_opcoes()
                if opcao in opcoes:
                    opcoes[opcao]()
                else:
                    self.__tela_membro.mostrar_mensagem("Opção inválida.")
            except Exception as e:
                self.__tela_membro.mostrar_mensagem(f"Erro inesperado: {e}")


