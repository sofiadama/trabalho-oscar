from tela.tela_membro import TelaMembro
from entidade.membro import Membro
from DAOs.membro_dao import MembroDAO

class ControladorMembro():
    def __init__(self, controlador_sistema):
        self.__membro_DAO = MembroDAO()
        self.__tela_membro = TelaMembro()
        self.__controlador_sistema = controlador_sistema

    def pegar_membro_por_id(self, id: int):
        try:
            id = int(id)
        except (TypeError, ValueError):
            self.__tela_membro.mostrar_mensagem("ID inválido.")
            return None

        membro = self.__membro_DAO.get(id)
        if membro is not None:
            return membro
        else:
            self.__tela_membro.mostrar_mensagem(f"Membro com ID {id} não encontrado.")
            return None

    def adicionar_membro(self):
        try:
            dados_membro = self.__tela_membro.pegar_dados_membro()
            if not dados_membro:
                return

            id_membro = int(dados_membro["id"])
            # Checa se já existe membro com mesmo ID
            if self.__membro_DAO.get(id_membro) is not None:
                self.__tela_membro.mostrar_mensagem("Membro já foi cadastrado.")
                return

            membro = Membro(
                id_membro,
                dados_membro["nome"],
                dados_membro["nascimento"],
                dados_membro["nacionalidade"]
            )
            self.__membro_DAO.add(membro)
            self.__tela_membro.mostrar_mensagem("\nMembro cadastrado com sucesso!")
        except (AttributeError, KeyError, ValueError) as e:
            self.__tela_membro.mostrar_mensagem(f"Erro ao cadastrar membro: {e}")

    def alterar_dados(self):
        try:
            id_membro = self.__tela_membro.selecionar_membro()
            membro = self.pegar_membro_por_id(id_membro)
            if membro is None:
                return

            novos_dados_membro = self.__tela_membro.pegar_dados_membro()
            if not novos_dados_membro:
                return

            novo_id = int(novos_dados_membro["id"])
            # Remove o antigo se o ID mudar
            self.__membro_DAO.remove(membro.id)
            membro.id = novo_id
            membro.nome = novos_dados_membro["nome"]
            membro.nascimento = novos_dados_membro["nascimento"]
            membro.nacionalidade = novos_dados_membro["nacionalidade"]
            self.__membro_DAO.add(membro)
            self.__tela_membro.mostrar_mensagem("\nDados alterados com sucesso!")
        except (AttributeError, KeyError, ValueError) as e:
            self.__tela_membro.mostrar_mensagem(f"Erro ao alterar membro: {e}")

    def listar_membros(self):
        membros = self.__membro_DAO.get_all()
        if not membros:
            self.__tela_membro.mostrar_mensagem("Nenhum membro cadastrado.")
            return

        dados_membros = []
        for membro in membros:
            dados_membros.append({
                "id": membro.id,
                "nome": membro.nome,
                "nascimento": membro.nascimento,
                "nacionalidade": membro.nacionalidade
            })

        self.__tela_membro.mostrar_dados_membro(dados_membros)

    def remover_membro(self):
        try:
            id_membro = self.__tela_membro.selecionar_membro()
            membro = self.pegar_membro_por_id(id_membro)
            if membro is not None:
                self.__membro_DAO.remove(membro.id)
                self.__tela_membro.mostrar_mensagem("\nMembro removido com sucesso!")
            else:
                self.__tela_membro.mostrar_mensagem("Membro não encontrado.")
        except (AttributeError, KeyError, ValueError) as e:
            self.__tela_membro.mostrar_mensagem(f"Erro ao remover membro: {e}")

    def pegar_lista_membros(self):
        return self.__membro_DAO.get_all()

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