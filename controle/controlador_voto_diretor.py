from tela.tela_voto import TelaVoto
from tela.tela_voto_diretor import TelaVotoDiretor
from entidade.voto_diretor import VotoDiretor

class ControladorVotoDiretor:
    def __init__(self, controlador_sistema):
        self.__votos_em_diretores = []
        self.__tela_voto = TelaVoto()
        self.__tela_voto_diretor = TelaVotoDiretor()
        self.__controlador_sistema = controlador_sistema
    
    def adicionar_voto(self):
        try:
            dados_voto = self.__tela_voto.pegar_dados_voto()

            if self.verificar_diretor_indicado(dados_voto):
                return
            if self.verificar_voto_existente(dados_voto):
                return
            
            voto = VotoDiretor(
                self.retornar_membro_autenticado(), 
                dados_voto["indicado"],
                dados_voto["categoria"],
                dados_voto["ano"]
            )

            self.__votos_em_diretores.append(voto)
            self.__controlador_sistema.controlador_voto.pegar_lista_votos().append(voto)
            self.__tela_voto.mostrar_mensagem("Voto registrado com sucesso!")
            
        except KeyError:
            print(f"Voto já registrado para esse ID!")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")  
    
    def alterar_voto(self):
        voto = self.selecionar_voto()
        if not voto:
            return
        
        novos_dados_voto = self.__tela_voto.pegar_dados_voto()
        voto.indicado = novos_dados_voto["indicado"]
        voto.categoria = novos_dados_voto["categoria"]
        voto.ano = novos_dados_voto["ano"]
    
        self.__tela_voto.mostrar_mensagem("\nVoto alterado com sucesso!")
    
    def listar_votos(self):
        if not self.__votos_em_diretores:
            self.__tela_voto.mostrar_mensagem("Nenhum voto em diretor registrado.")
            
        print("----- VOTOS EM DIRETORES -----\n")
        for voto in self.__votos_em_diretores:
            self.__tela_voto.mostrar_dados_voto({
                "membro": voto.membro.nome, 
                "indicado": voto.indicado,
                "categoria": voto.categoria.titulo,
                "ano": voto.ano
            })

    def remover_voto(self):
        voto = self.selecionar_voto()

        if not voto:
            return
        self.__votos_em_diretores.remove(voto)
        self.__tela_voto.mostrar_mensagem("\nVoto removido com sucesso!")

    def verificar_diretor_indicado(self, dados_voto):
        diretores_indicados = self.__controlador_sistema.controlador_diretor.pegar_diretores_indicados()

        if dados_voto["indicado"] not in [diretor.nome for diretor in diretores_indicados]:
            print("\nDiretor não indicado.")
            return True
        return False
    
    def verificar_voto_existente(self, dados_voto):
        membro = self.retornar_membro_autenticado()

        for voto in self.__votos_em_diretores:
            if membro.id == voto.membro.id and voto.categoria == dados_voto["categoria"] and voto.ano == dados_voto["ano"]:
                print("Você já votou nessa categoria esse ano.")
                return True
        return False

    def selecionar_voto(self):
        try:
            membro = self.retornar_membro_autenticado()
            ano = self.__tela_voto.buscar_voto_por_ano()
            votos_filtrados = [voto for voto in self.__votos_em_diretores if voto.membro.id == membro.id and voto.ano == ano]
            
            if not votos_filtrados:
                self.__tela_voto.mostrar_mensagem("Voto não consta nos registros.")
            return votos_filtrados[0]
        
        except AttributeError:
            self.__tela_voto.mostrar_mensagem("Erro de atributo!")
        except Exception as e:
            self.__tela_voto.mostrar_mensagem(f"Erro inesperado: {e}")

    def gerar_relatorio_por_ano(self):
        ano = self.__tela_voto.buscar_voto_por_ano()
        votos_filtrados = [voto for voto in self.__votos_em_diretores if voto.ano == ano]
            
        if not votos_filtrados:
            self.__tela_voto.mostrar_mensagem(f"Nenhum voto no ano de '{ano}'.")
            return

        print("." * 10,f"VOTOS NO ANO DE {ano}", "." * 10)
        print()
        for i, voto in enumerate(votos_filtrados, 1):
            print(f"{i}. Membro: {voto.membro.nome}, Indicado: {voto.indicado}, Categoria: {voto.categoria.titulo}")
            
    def retornar_membro_autenticado(self):
        return self.__controlador_sistema.controlador_voto.pegar_membro_autenticado()  
    
    def retornar_menu(self):
        self.__controlador_sistema.abrir_submenu_votos()
    
    def abrir_tela_voto_diretor(self):
        opcoes = {
            1: self.adicionar_voto, 
            2: self.alterar_voto, 
            3: self.abrir_filtro_diretores, 
            4: self.remover_voto, 
            0: self.retornar_menu
        }
    
        while True:
            try:
                opcoes[self.__tela_voto_diretor.tela_votos_em_diretores()]()
            except KeyError:
                self.__tela_voto.mostrar_mensagem("Opção inválida!")
    
    def abrir_filtro_diretores(self):
        opcoes = {
            1: self.listar_votos, 
            2: self.gerar_relatorio_por_ano, 
            0: self.abrir_tela_voto_diretor
        }

        while True:
            try:
                opcoes[self.__tela_voto_diretor.tela_filtros_de_relatorios()]()
            except KeyError:
                self.__tela_voto.mostrar_mensagem("Opção inválida!")