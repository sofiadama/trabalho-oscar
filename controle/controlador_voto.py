from tela.tela_voto import TelaVoto
from exceções.id_nao_encontrado_exception import IDNaoEncontradoException

class ControladorVoto:
    def __init__(self, controlador_sistema):
        self.__votos_gerais = []
        self.__membro_autenticado = None
        self.__tela_voto = TelaVoto()
        self.__controlador_sistema = controlador_sistema

    @property
    def membro_autenticado(self):
        return self.__membro_autenticado
    
    def autenticar_membro(self):      
        while True:
            try:
                id_membro = self.__tela_voto.autenticacao_membro()
                
                if id_membro is None:
                    return False
                
                id_membro = int(id_membro)
                
                lista_membros = self.__controlador_sistema.controlador_membro.pegar_lista_membros()
                for membro in lista_membros:
                    if membro.id == id_membro:
                        self.__membro_autenticado = membro
                        self.__controlador_sistema.escolher_tipo_de_voto()
                        return True 
                raise IDNaoEncontradoException("ID não encontrado. Tente novamente.")
            except IDNaoEncontradoException as e:
                self.__tela_voto.mostrar_mensagem(str(e))     
            except ValueError:
                self.__tela_voto.mostrar_mensagem("Por favor, digite apenas números.")
            except Exception as e:
                self.__tela_voto.mostrar_mensagem(f"Erro inesperado:{e}.")
            
    def contar_votos_por_ano(self):
        ano_filtro = self.__tela_voto.buscar_vencedor_por_ano()
        contagem_por_ano = {}

        votos_filtrados = [voto for voto in self.__votos_gerais if voto.ano == ano_filtro]

        if not votos_filtrados:
            self.__tela_voto.mostrar_mensagem(f"Nenhum voto encontrado para o ano '{ano_filtro}'.")
            return None 

        for voto in votos_filtrados:
            contagem_por_ano[voto.indicado] = contagem_por_ano.get(voto.indicado, 0) + 1

        mais_votados = max(contagem_por_ano.values())
        vencedores = [indicado for indicado, votos in contagem_por_ano.items() if votos == mais_votados]

        votos_vencedores = []
        for vencedor in vencedores:
            for voto in votos_filtrados:
                if voto.indicado == vencedor:
                    votos_vencedores.append(voto)
                    break
        return votos_vencedores
    
    def contar_votos_por_categoria(self):
        categoria_filtro = self.__tela_voto.buscar_vencedor_por_categoria().strip().title()
        contagem_por_categoria = {}

        votos_filtrados = [voto for voto in self.__votos_gerais if voto.categoria.titulo == categoria_filtro]

        if not votos_filtrados:
            self.__tela_voto.mostrar_mensagem(f"Nenhum voto encontrado para a categoria '{categoria_filtro}'.")
            return None  

        for voto in votos_filtrados:
            contagem_por_categoria[voto.indicado] = contagem_por_categoria.get(voto.indicado, 0) + 1

        mais_votados = max(contagem_por_categoria.values())  
        vencedores = [indicado for indicado, votos in contagem_por_categoria.items() if votos == mais_votados]      

        votos_vencedores = []
        for vencedor in vencedores:
            for voto in votos_filtrados:
                if voto.indicado == vencedor:
                    votos_vencedores.append(voto)
                    break
        return votos_vencedores
    
    def contar_filmes_mais_premiados(self):
        votos_em_filmes = self.__controlador_sistema.controlador_voto_filme.pegar_votos_em_filmes()
        contagem_filmes = {}
        
        for voto in votos_em_filmes:
            indicado = voto.indicado
            contagem_filmes[indicado] = contagem_filmes.get(indicado, 0) + 1

        filmes_mais_premiados = list(contagem_filmes.keys())[:3]
        return filmes_mais_premiados
    
    def carregar_votos_gerais(self):
        votos_ator = self.__controlador_sistema.controlador_voto_ator.pegar_votos_em_atores()
        votos_diretor = self.__controlador_sistema.controlador_voto_diretor.pegar_votos_em_diretores()
        votos_filme = self.__controlador_sistema.controlador_voto_filme.pegar_votos_em_filmes()
        
        self.__votos_gerais = []
        self.__votos_gerais.extend(votos_filme)
        self.__votos_gerais.extend(votos_ator)
        self.__votos_gerais.extend(votos_diretor)
    
    def listar_votos_gerais(self):         
        if not self.__votos_gerais:
            self.__tela_voto.mostrar_mensagem("Nenhum voto registrado.")
            return

        dados_votos = []
        for voto in self.__votos_gerais:
            categoria_titulo = voto.categoria.titulo if hasattr(voto.categoria, 'titulo') else str(voto.categoria)
            indicado_nome = voto.indicado.titulo if hasattr(voto.indicado, 'titulo') else str(voto.indicado)
            dados_votos.append({
                "membro": voto.membro.nome,
                "indicado": indicado_nome,
                "categoria": categoria_titulo,
                "ano": voto.ano
            })
        self.__tela_voto.mostrar_dados_voto(dados_votos)
    
    def listar_vencedores_por_ano(self):
        vencedores = self.contar_votos_por_ano()

        if not vencedores:
            self.__tela_voto.mostrar_mensagem("Nenhum vencedor encontrado.")
            return
        
        mensagem = f"=========== VENCEDORES NO ANO DE '{vencedores[0].ano}' ===========\n"
        for i, vencedor in enumerate(vencedores, start=1):
            indicado = vencedor.indicado
            if hasattr(indicado, 'titulo'):
                indicado_nome = indicado.titulo
            elif hasattr(indicado, 'nome'):
                indicado_nome = indicado.nome
            else:
                indicado_nome = str(indicado)
            mensagem += f"{i}. {indicado_nome}\n"
    
        self.__tela_voto.mostrar_mensagem(mensagem)
            
    def listar_vencedores_por_categoria(self):
        vencedores = self.contar_votos_por_categoria()

        if not vencedores:
            self.__tela_voto.mostrar_mensagem("Nenhum vencedor encontrado.")
            return
        
        mensagem = f"========= VENCEDORES NA CATEGORIA '{vencedores[0].categoria.titulo}' =========\n"
        for i, vencedor in enumerate(vencedores, start=1):
            indicado = vencedor.indicado
            if hasattr(indicado, 'titulo'):
                indicado_nome = indicado.titulo
            elif hasattr(indicado, 'nome'):
                indicado_nome = indicado.nome
            else:
                indicado_nome = str(indicado)
            mensagem += f"{i}. {indicado_nome}\n"
        
        self.__tela_voto.mostrar_mensagem(mensagem)
    
    def listar_filmes_mais_premiados(self):
        filmes_mais_premiados = self.contar_filmes_mais_premiados()

        if not filmes_mais_premiados:
            self.__tela_voto.mostrar_mensagem("Nenhum filme encontrado.")
            return

        mensagem = "============= TOP 3 FILMES MAIS PREMIADOS =============\n"
        for i, filme in enumerate(filmes_mais_premiados, start=1):
            filme_titulo = filme.titulo if hasattr(filme.titulo, 'titulo') else str(filme.titulo)
            mensagem += f"{i}. {filme_titulo}\n"
        
        self.__tela_voto.mostrar_mensagem(mensagem)

    def pegar_membro_autenticado(self):
        return self.__membro_autenticado
                
    def pegar_lista_votos(self):
        return self.__votos_gerais

    def retornar_menu(self):
        self.__controlador_sistema.abrir_submenu_votos()

    def abrir_filtro_vencedores(self):
        opcoes = {
            1: self.listar_votos_gerais, 
            2: self.listar_vencedores_por_ano, 
            3: self.listar_vencedores_por_categoria,
            4: self.listar_filmes_mais_premiados,
            0: self.retornar_menu
        }

        while True:
            try:
                opcoes[self.__tela_voto.tela_filtros_de_relatorios()]()
            except KeyError:
                self.__tela_voto.mostrar_mensagem("Opção inválida!")