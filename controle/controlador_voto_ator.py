from tela.tela_voto import TelaVoto
from tela.tela_voto_ator import TelaVotoAtor
from entidade.voto_ator import VotoAtor
from DAOs.voto_ator_dao import VotoAtorDAO
from exceções.voto_duplicado_exception import VotoDuplicadoException

class ControladorVotoAtor:
    def __init__(self, controlador_sistema):
        self.__voto_ator_DAO = VotoAtorDAO()
        self.__tela_voto = TelaVoto()
        self.__tela_voto_ator = TelaVotoAtor()
        self.__controlador_sistema = controlador_sistema

    def adicionar_voto(self):
        try:
            dados_voto = self.__tela_voto.pegar_dados_voto()
            if not dados_voto:
                return

            membro_obj = self.retornar_membro_autenticado()
            if not membro_obj:
                self.__tela_voto.mostrar_mensagem("Membro não autenticado.")
                return

            ator_obj = self.__controlador_sistema.controlador_ator.pegar_ator_por_nome(dados_voto["indicado"])
            if not ator_obj:
                self.__tela_voto.mostrar_mensagem("Ator não indicado.")
                return

            categoria_obj = self.__controlador_sistema.controlador_categoria.pegar_categoria_por_titulo(dados_voto["categoria"])
            if not categoria_obj:
                self.__tela_voto.mostrar_mensagem("Categoria não cadastrada.")
                return

            dados_voto["indicado"] = ator_obj
            dados_voto["categoria"] = categoria_obj

            if self.verificar_ator_indicado(dados_voto):
                return
            if self.verificar_categoria_cadastrada(dados_voto):
                return
            if self.verificar_voto_existente(dados_voto):
                return

            voto = VotoAtor(
                membro_obj,
                ator_obj,
                categoria_obj,
                dados_voto["ano"]
            )

            self.__voto_ator_DAO.add(voto)
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

        ator_obj = self.__controlador_sistema.controlador_ator.pegar_ator_por_nome(novos_dados_voto["indicado"])
        if not ator_obj:
            self.__tela_voto.mostrar_mensagem("Ator não indicado.")
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

        voto.indicado = ator_obj
        voto.categoria = categoria_obj
        voto.ano = ano

        self.__voto_ator_DAO.update(voto)
        self.__tela_voto.mostrar_mensagem("\nVoto alterado com sucesso!")

    def listar_votos(self):
        votos = self.__voto_ator_DAO.get_all()
        if not votos:
            self.__tela_voto.mostrar_mensagem("Nenhum voto em ator registrado.")
            return

        dados_votos = []
        for voto in votos:
            categoria_nome = voto.categoria.titulo if hasattr(voto.categoria, 'titulo') else str(voto.categoria)
            indicado_nome = voto.indicado.nome if hasattr(voto.indicado, 'nome') else str(voto.indicado)
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
        for v in self.__voto_ator_DAO.get_all():
            if v.membro == voto.membro and v.indicado == voto.indicado and v.categoria == voto.categoria and v.ano == voto.ano:
                self.__voto_ator_DAO.remove(v.membro, v.indicado)
                self.__tela_voto.mostrar_mensagem("\nVoto removido com sucesso!")
                return
        self.__tela_voto.mostrar_mensagem("Voto não consta nos registros.")

    def verificar_ator_indicado(self, dados_voto):
        atores_indicados = self.__controlador_sistema.controlador_ator.pegar_atores_indicados()
        if hasattr(dados_voto["indicado"], "nome"):
            nome_indicado = dados_voto["indicado"].nome.strip().title()
        else:
            nome_indicado = str(dados_voto["indicado"]).strip().title()
        nomes_atores = [ator.nome.strip().title() for ator in atores_indicados]
        if nome_indicado not in nomes_atores:
            self.__tela_voto.mostrar_mensagem("\nAtor não indicado.")
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
        for voto in self.__voto_ator_DAO.get_all():
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
            for voto in self.__voto_ator_DAO.get_all():
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

    def gerar_relatorio_por_ano(self):
        ano = self.__tela_voto.buscar_voto_por_ano()
        votos_filtrados = [voto for voto in self.__voto_ator_DAO.get_all() if voto.ano == ano]

        if not votos_filtrados:
            self.__tela_voto.mostrar_mensagem(f"Nenhum voto no ano de '{ano}'.")
            return

        mensagem = f"========== VOTOS NO ANO DE {ano} ==========\n"
        for i, voto in enumerate(votos_filtrados, 1):
            indicado_nome = voto.indicado.nome if hasattr(voto.indicado, 'nome') else str(voto.indicado)
            categoria_nome = voto.categoria.titulo if hasattr(voto.categoria, 'titulo') else str(voto.categoria)
            mensagem += f"{i}. Membro: {voto.membro.nome}, Indicado: {indicado_nome}, Categoria: {categoria_nome}\n"

        self.__tela_voto.mostrar_mensagem(mensagem)

    def gerar_relatorio_por_categoria(self):
        categoria = self.__tela_voto.buscar_voto_por_categoria().strip().title()
        votos_filtrados = [
            voto for voto in self.__voto_ator_DAO.get_all()
            if (hasattr(voto.categoria, 'titulo') and voto.categoria.titulo.strip().title() == categoria)
            or (isinstance(voto.categoria, str) and voto.categoria.strip().title() == categoria)
        ]

        if not votos_filtrados:
            self.__tela_voto.mostrar_mensagem(f"\nNenhum voto na categoria '{categoria}'.")
            return

        mensagem = f"========= VOTOS NA CATEGORIA '{categoria}' =========\n"
        for i, voto in enumerate(votos_filtrados, 1):
            indicado_nome = voto.indicado.nome if hasattr(voto.indicado, 'nome') else str(voto.indicado)
            mensagem += f"{i}. Membro: {voto.membro.nome}, Indicado: {indicado_nome}, Ano: {voto.ano}\n"

        self.__tela_voto.mostrar_mensagem(mensagem)

    def pegar_votos_em_atores(self):
        return self.__voto_ator_DAO.get_all()

    def retornar_membro_autenticado(self):
        return self.__controlador_sistema.controlador_voto.pegar_membro_autenticado()

    def retornar_menu(self):
        self.__controlador_sistema.abrir_submenu_votos()

    def abrir_tela_voto_ator(self):
        opcoes = {
            1: self.adicionar_voto,
            2: self.alterar_voto,
            3: self.abrir_filtro_atores,
            4: self.remover_voto,
            0: self.retornar_menu
        }

        while True:
            try:
                op = self.__tela_voto_ator.tela_votos_em_atores()
                if op in opcoes:
                    opcoes[op]()
                else:
                    self.__tela_voto_ator.mostrar_mensagem("Opção inválida!")
            except Exception as e:
                self.__tela_voto_ator.mostrar_mensagem(f"Erro inesperado: {e}")

    def abrir_filtro_atores(self):
        opcoes = {
            1: self.listar_votos,
            2: self.gerar_relatorio_por_ano,
            3: self.gerar_relatorio_por_categoria,
            0: self.abrir_tela_voto_ator
        }

        while True:
            try:
                op = self.__tela_voto_ator.tela_filtros_de_relatorios()
                if op in opcoes:
                    opcoes[op]()
                else:
                    self.__tela_voto_ator.mostrar_mensagem("Opção inválida!")
            except Exception as e:
                self.__tela_voto_ator.mostrar_mensagem(f"Erro inesperado: {e}")