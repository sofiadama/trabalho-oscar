from tela.tela_voto import TelaVoto
from tela.tela_voto_filme import TelaVotoFilme
from entidade.voto_filme import VotoFilme
from DAOs.voto_filme_dao import VotoFilmeDAO
from exceções.voto_duplicado_exception import VotoDuplicadoException

class ControladorVotoFilme:
    def __init__(self, controlador_sistema):
        self.__voto_filme_DAO = VotoFilmeDAO()
        self.__tela_voto = TelaVoto()
        self.__tela_voto_filme = TelaVotoFilme()
        self.__controlador_sistema = controlador_sistema

    def adicionar_voto(self):
        try:
            dados_voto = self.__tela_voto.pegar_dados_voto()
            if not dados_voto:
                return
            
            filme_obj = self.__controlador_sistema.controlador_filme.pegar_filme_por_titulo(dados_voto["indicado"])
            if not filme_obj:
                self.__tela_voto.mostrar_mensagem("Filme não cadastrado.")
                return

            categoria_obj = self.__controlador_sistema.controlador_categoria.pegar_categoria_por_titulo(dados_voto["categoria"])
            if not categoria_obj:
                self.__tela_voto.mostrar_mensagem("Categoria não cadastrada.")
                return

            membro_obj = self.retornar_membro_autenticado()
            if not membro_obj:
                self.__tela_voto.mostrar_mensagem("Membro não autenticado.")
                return

            dados_voto["indicado"] = filme_obj
            dados_voto["categoria"] = categoria_obj

            if self.verificar_filme_indicado(dados_voto):
                return
            if self.verificar_categoria_cadastrada(dados_voto):
                return
            if self.verificar_voto_existente(dados_voto):
                return

            voto = VotoFilme(
                membro_obj,
                filme_obj,
                categoria_obj,
                dados_voto["ano"]
            )

            self.__voto_filme_DAO.add(voto)
            self.__controlador_sistema.controlador_voto.pegar_lista_votos().append(voto)
            self.__tela_voto.mostrar_mensagem("Voto registrado com sucesso!")

            raise VotoDuplicadoException("Voto já registrado para esse ID!")
        except VotoDuplicadoException as e:
            self.__tela_voto.mostrar_mensagem(str(e)) 
        except Exception as e:
            self.__tela_voto.mostrar_mensagem(f"Ocorreu um erro inesperado: {e}")

    def alterar_voto(self):
        voto = self.selecionar_voto()
        if not voto:
            return

        novos_dados_voto = self.__tela_voto.pegar_dados_voto()
        if not novos_dados_voto:
            return

        filme_obj = self.__controlador_sistema.controlador_filme.pegar_filme_por_titulo(novos_dados_voto["indicado"])
        if not filme_obj:
            self.__tela_voto.mostrar_mensagem("Filme não cadastrado.")
            return

        categoria_obj = self.__controlador_sistema.controlador_categoria.pegar_categoria_por_titulo(novos_dados_voto["categoria"])
        if not categoria_obj:
            self.__tela_voto.mostrar_mensagem("Categoria não cadastrada.")
            return

        try:
            ano = int(novos_dados_voto["ano"])
        except (TypeError, ValueError):
            self.__tela_voto.mostrar_mensagem("Ano de votação inválido.")
            return

        voto.indicado = filme_obj
        voto.categoria = categoria_obj
        voto.ano = ano

        self.__voto_filme_DAO.update(voto)
        self.__tela_voto.mostrar_mensagem("\nVoto alterado com sucesso!")
    
    def listar_votos(self):
        votos = self.__voto_filme_DAO.get_all()
        if not votos:
            self.__tela_voto.mostrar_mensagem("Nenhum voto em filme registrado.")
            return

        dados_votos = []
        for voto in votos:
            categoria_nome = voto.categoria.titulo if hasattr(voto.categoria, 'titulo') else str(voto.categoria)
            indicado_nome = voto.indicado.titulo if hasattr(voto.indicado, 'titulo') else str(voto.indicado)
            dados_votos.append({
                "membro": voto.membro.nome,
                "indicado": indicado_nome,
                "categoria": categoria_nome,
                "ano": voto.ano
            })
        self.__tela_voto.mostrar_dados_voto(dados_votos)

    def remover_voto(self):
        voto = self.selecionar_voto()
        if not voto:
            return
        self.__voto_filme_DAO.remove(voto.membro, voto.indicado)
        self.__tela_voto.mostrar_mensagem("\nVoto removido com sucesso!")

    def verificar_filme_indicado(self, dados_voto):
        filmes_indicados = self.__controlador_sistema.controlador_filme.pegar_filmes_indicados()
        if hasattr(dados_voto["indicado"], "titulo"):
            titulo_indicado = dados_voto["indicado"].titulo.strip().title()
        else:
            titulo_indicado = str(dados_voto["indicado"]).strip().title()
        titulos_filmes = [filme.titulo.strip().title() for filme in filmes_indicados]
        if titulo_indicado not in titulos_filmes:
            self.__tela_voto.mostrar_mensagem("\nFilme não indicado.")
            return True
        return False

    def verificar_categoria_cadastrada(self, dados_voto):
        categorias = [categoria.titulo.strip().title() for categoria in self.__controlador_sistema.controlador_categoria.pegar_categorias()]
        if hasattr(dados_voto["categoria"], 'titulo'):
            categoria_nome = dados_voto["categoria"].titulo.strip().title()
        else:
            categoria_nome = str(dados_voto["categoria"]).strip().title()
        if categoria_nome not in categorias:
            self.__tela_voto.mostrar_mensagem("\nCategoria não cadastrada.")
            return True
        return False

    def verificar_voto_existente(self, dados_voto):
        membro = self.retornar_membro_autenticado()
        for voto in self.__voto_filme_DAO.get_all():
            voto_categoria = voto.categoria.titulo.strip().title() if hasattr(voto.categoria, 'titulo') else str(voto.categoria).strip().title()
            dados_categoria = dados_voto["categoria"].titulo.strip().title() if hasattr(dados_voto["categoria"], 'titulo') else str(dados_voto["categoria"]).strip().title()
            if membro.id == voto.membro.id and voto_categoria == dados_categoria and voto.ano == dados_voto["ano"]:
                self.__tela_voto.mostrar_mensagem("Você já votou nessa categoria esse ano.")
                return True
        return False

    def selecionar_voto(self):
        try:
            membro = self.retornar_membro_autenticado()
            categoria = self.__tela_voto.buscar_voto_por_categoria().strip().title()
            ano = self.__tela_voto.buscar_voto_por_ano()
            votos_filtrados = []
            for voto in self.__voto_filme_DAO.get_all():
                voto_categoria = voto.categoria.titulo.strip().title() if hasattr(voto.categoria, 'titulo') else str(voto.categoria).strip().title()
                if voto.membro.id == membro.id and voto_categoria == categoria and voto.ano == ano:
                    votos_filtrados.append(voto)
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
        votos_filtrados = [voto for voto in self.__voto_filme_DAO.get_all() if voto.categoria.titulo.strip().title() == categoria]

        if not votos_filtrados:
            self.__tela_voto.mostrar_mensagem(f"\nNenhum voto na categoria '{categoria}'.")
            return

        mensagem = f"========= VOTOS NA CATEGORIA '{categoria}' =========\n"
        for i, voto in enumerate(votos_filtrados, 1):
            indicado_titulo = voto.indicado.titulo if hasattr(voto.indicado, 'titulo') else str(voto.indicado)
            mensagem += f"{i}. Membro: {voto.membro.nome}, Indicado: {indicado_titulo}, Ano: {voto.ano}\n"

        self.__tela_voto_filme.mostrar_mensagem(mensagem)

    def gerar_relatorio_por_ano(self):
        ano = self.__tela_voto.buscar_voto_por_ano()
        votos_filtrados = [voto for voto in self.__voto_filme_DAO.get_all() if voto.ano == ano]

        if not votos_filtrados:
            self.__tela_voto.mostrar_mensagem(f"\nNenhum voto no ano '{ano}'.")
            return

        mensagem = f"============= VOTOS NO ANO DE '{ano}' =============\n"
        for i, voto in enumerate(votos_filtrados, 1):
            indicado_titulo = voto.indicado.titulo if hasattr(voto.indicado, 'titulo') else str(voto.indicado)
            categoria_titulo = voto.categoria.titulo if hasattr(voto.categoria, 'titulo') else str(voto.categoria)
            mensagem += f"{i}. Membro: {voto.membro.nome}, Indicado: {indicado_titulo}, Categoria: {categoria_titulo}\n"

        self.__tela_voto_filme.mostrar_mensagem(mensagem)
    
    def pegar_voto_por_ano(self, ano):
        return [voto for voto in self.__voto_filme_DAO.get_all() if voto.ano == ano]
    
    def pegar_votos_em_filmes(self):
        return self.__voto_filme_DAO.get_all()
    
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
                self.__tela_voto_filme.mostrar_mensagem("Opção inválida!")

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
                self.__tela_voto_filme.mostrar_mensagem("Opção inválida!")