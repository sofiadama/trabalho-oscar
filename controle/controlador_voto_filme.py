from tela.tela_voto import TelaVoto
from tela.tela_voto_filme import TelaVotoFilme
from entidade.voto_filme import VotoFilme

class ControladorVotoFilme:
    def __init__(self, controlador_sistema):
        self.__votos_em_filmes = []
        self.__tela_voto = TelaVoto()
        self.__tela_voto_filme = TelaVotoFilme()
        self.__controlador_sistema = controlador_sistema
    
    def adicionar_voto(self):
        try:
            dados_voto = self.__tela_voto.pegar_dados_voto()

            if self.verificar_filme_indicado(dados_voto):
                return
            if self.verificar_categoria_cadastrada(dados_voto):
                return
            if self.verificar_voto_existente(dados_voto):
                return

            voto = VotoFilme(
                self.retornar_membro_autenticado(), 
                dados_voto["indicado"],
                dados_voto["categoria"],
                dados_voto["ano"]
            )

            self.__votos_em_filmes.append(voto)
            self.__controlador_sistema.controlador_voto.pegar_lista_votos().append(voto)
            self.__tela_voto.mostrar_mensagem("Voto registrado com sucesso!")
            
        except KeyError:
            print(f"Voto já registrado para esse ID!")
        except AttributeError as e:
            print(f"Erro de atributo: {e}")
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
        if not self.__votos_em_filmes:
            self.__tela_voto.mostrar_mensagem("Nenhum voto em filme registrado.")
            return
            
        print("." * 10,"VOTOS EM FILMES","." * 10)
        for voto in self.__votos_em_filmes:
            self.__tela_voto.mostrar_dados_voto({
                "membro": voto.membro.nome, 
                "indicado": voto.indicado,
                "categoria": voto.categoria.titulo,
                "ano": voto.ano
            })

    def remover_voto(self):
        voto = self.selecionar_voto()

        if not voto:
            self.__tela_voto.mostrar_mensagem("\nVoto não foi registrado.")
            
        self.__votos_em_filmes.remove(voto)
        self.__tela_voto.mostrar_mensagem("\nVoto removido com sucesso!")
        
    def verificar_filme_indicado(self, dados_voto):
        filmes_indicados = self.__controlador_sistema.controlador_filme.pegar_filmes_indicados()
        
        if dados_voto["indicado"] not in [filme.titulo for filme in filmes_indicados]:
            print("\nFilme não indicado.")
            return True
        return False
    
    def verificar_categoria_cadastrada(self, dados_voto):
        categorias = [categoria.titulo.strip().title() for categoria in self.__controlador_sistema.controlador_categoria.pegar_categorias()]

        if dados_voto["categoria"].titulo.strip().title() not in categorias:
            print("\nCategoria não cadastrada.")
            return True
        return False
    
    def verificar_voto_existente(self, dados_voto):
        membro = self.retornar_membro_autenticado()
        for voto in self.__votos_em_filmes:
            if dados_voto["membro"].id == membro.id and voto.categoria == dados_voto["categoria"] and voto.ano == dados_voto["ano"]:
                print("Você já votou nessa categoria esse ano.")
                return True
        return False
    
    def selecionar_voto(self):
        try:
            membro = self.retornar_membro_autenticado()
            categoria = self.__tela_voto.buscar_voto_por_categoria().strip().title()
            ano = self.__tela_voto.buscar_voto_por_ano()
            votos_filtrados = [voto for voto in self.__votos_em_filmes if voto.membro.id == membro.id and voto.categoria.titulo.strip().title() == categoria and voto.ano == ano]
            
            if not votos_filtrados:
                self.__tela_voto.mostrar_mensagem("Voto não consta nos registros.")
                return None
            return votos_filtrados[0]
        
        except AttributeError:
            self.__tela_voto.mostrar_mensagem("ID do membro é inválido!")
        except Exception as e:
            self.__tela_voto.mostrar_mensagem(f"Erro inesperado: {e}")
                
    def gerar_relatorio_por_categoria(self):
        categoria = self.__tela_voto.buscar_voto_por_categoria().strip().title()
        votos_filtrados = [voto for voto in self.__votos_em_filmes if voto.categoria.titulo.strip().title() == categoria]
    
        if not votos_filtrados:
            self.__tela_voto.mostrar_mensagem(f"\nNenhum voto na categoria '{categoria}'.")
            return
        
        print("." * 15, f"VOTOS NA CATEGORIA '{categoria}'", "." * 15)
        for i, voto in enumerate(votos_filtrados, 1):
            print(f"{i}. Membro: {voto.membro.nome}, Indicado: {voto.indicado}, Ano: {voto.ano}")

    def gerar_relatorio_por_ano(self):
        ano = self.__tela_voto.buscar_voto_por_ano()
        votos_filtrados = [voto for voto in self.__votos_em_filmes if voto.ano == ano]
    
        if not votos_filtrados:
            self.__tela_voto.mostrar_mensagem(f"\nNenhum voto no ano '{ano}'.")
            return
        
        print("." * 15,f"VOTOS NO ANO DE '{ano}'", "." * 15)
        for i, voto in enumerate(votos_filtrados, 1):
            print(f"{i}. Membro: {voto.membro.nome}, Indicado: {voto.indicado}, Categoria: {voto.categoria.titulo}")
    
    def pegar_voto_por_ano(self, ano):
        return [voto for voto in self.__votos_em_filmes if voto.ano == ano]
    
    def retornar_membro_autenticado(self):
        return self.__controlador_sistema.controlador_voto.pegar_membro_autenticado()
    
    def retornar_menu(self):
        self.__controlador_sistema.abrir_submenu_votos()
    
    def abrir_tela_voto_filme(self):
        opcoes = {
            1: self.adicionar_voto, 
            2: self.alterar_voto, 
            3: self.abrir_filtro_filmes, 
            4: self.remover_voto, 
            0: self.retornar_menu
        }
    
        while True:
            try:
                opcoes[self.__tela_voto_filme.tela_votos_em_filmes()]()
            except KeyError:
                print("Opção inválida!")

    def abrir_filtro_filmes(self):
        opcoes = {
            1: self.listar_votos, 
            2: self.gerar_relatorio_por_ano, 
            3: self.gerar_relatorio_por_categoria,
            0: self.abrir_tela_voto_filme
        }

        while True:
            try:
                opcoes[self.__tela_voto_filme.tela_filtros_de_relatorios()]()
            except KeyError:
                print("Opção inválida!")

        