from tela.tela_voto import TelaVoto

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
                lista_membros = self.__controlador_sistema.controlador_membro.pegar_lista_membros()
                for membro in lista_membros:
                    if membro.id == id_membro:
                        self.__membro_autenticado = membro
                        self.__controlador_sistema.escolher_tipo_de_voto()
                        return True
                        
                self.__tela_voto.mostrar_mensagem("\nID não encontrado. Tente novamente.")
                            
            except Exception as e:
                self.__tela_voto.mostrar_mensagem(f"Erro inesperado:{e}.")
            
    
    def contar_votos_por_ano(self):
        ano_filtro = self.__tela_voto.buscar_vencedor_por_ano()
        contagem_por_ano = {}

        votos_filtrados = [voto for voto in self.__votos_gerais if voto.ano == ano_filtro]

        if not votos_filtrados:
            self.__tela_voto.mostrar_mensagem("Nenhum voto encontrado para o ano.")
            return None 
        
        for voto in votos_filtrados:
            contagem_por_ano[voto.indicado] = contagem_por_ano.get(voto.indicado, 0) + 1

        mais_votados = max(contagem_por_ano.values())
        vencedores = [indicado for indicado, votos in contagem_por_ano.items() if votos == mais_votados]

        return [voto for voto in votos_filtrados if voto.indicado in vencedores]
    
    def contar_votos_por_categoria(self):
        categoria_filtro = self.__tela_voto.buscar_vencedor_por_categoria().strip().title()
        contagem_por_categoria = {}

        votos_filtrados = [voto for voto in self.__votos_gerais if voto.categoria.titulo == categoria_filtro] # Filtra os votos que pertencem à categoria desejada

        if not votos_filtrados:
            self.__tela_voto.mostrar_mensagem("Nenhum voto encontrado para a categoria.")
            return None  # Retorna None se não houver votos
        
        for voto in votos_filtrados:
            contagem_por_categoria[voto.indicado] = contagem_por_categoria.get(voto.indicado, 0) + 1 # Conta os votos por indicado

        mais_votados = max(contagem_por_categoria.values())  
        vencedores = [indicado for indicado, votos in contagem_por_categoria.items() if votos == mais_votados]      
        
        return [voto for voto in votos_filtrados if voto.indicado in vencedores]
    
    def contar_filmes_mais_premiados(self):
        votos_em_filmes = self.__controlador_sistema.controlador_voto_filme.pegar_votos_em_filmes()
        contagem_filmes = {}
        
        for voto in votos_em_filmes:
            indicado = voto.indicado
            contagem_filmes[indicado] = contagem_filmes.get(indicado, 0) + 1

        filmes_mais_premiados = list(contagem_filmes.keys())[:3]
        return filmes_mais_premiados
    
    def listar_votos_gerais(self):         
        if not self.__votos_gerais:
            self.__tela_voto.mostrar_mensagem("Nenhum voto registrado.")
            return

        print("." * 15,"VOTOS GERAIS","." * 15)
        for voto in self.__votos_gerais:
            self.__tela_voto.mostrar_dados_voto({
                "membro": voto.membro.nome,
                "indicado": voto.indicado,
                "categoria": voto.categoria.titulo,
                "ano": voto.ano
            })
    
    def listar_vencedores_por_ano(self):
        vencedores = self.contar_votos_por_ano()

        if not vencedores:
            self.__tela_voto.mostrar_mensagem("Nenhum vencedor encontrado.")
            return
        
        print("." * 15, f"VENCEDORES NO ANO DE '{vencedores[0].ano}'", "." * 15)
        for i, vencedor in enumerate(vencedores, start=1):
            print(f"{i}. {vencedor.indicado}")
            
    def listar_vencedores_por_categoria(self):
        vencedores = self.contar_votos_por_categoria()

        if not vencedores:
            self.__tela_voto.mostrar_mensagem("Nenhum vencedor encontrado.")
            return
        
        print("." * 15, f"VENCEDORES NA CATEGORIA '{vencedores[0].categoria.titulo}'", "." * 15)
        for i, vencedor in enumerate(vencedores, start=1):
            print(f"{i}. {vencedor.indicado}")
    
    def listar_filmes_mais_premiados(self):
        filmes_mais_premiados = self.contar_filmes_mais_premiados()

        if not filmes_mais_premiados:
            self.__tela_voto.mostrar_mensagem("Nenhum filme encontrado.")
            return

        print("." * 15, "TOP 3 FILMES MAIS PREMIADOS", "." * 15)
        for i, filme in enumerate(filmes_mais_premiados, start=1):
            print(f"{i}. {filme}")

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
                print("Opção inválida!")