class TelaFilme():
    
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def tela_opcoes(self):
        print("." * 15,"INDICAÇÃO DE FILMES","." * 15)
        print("\n1. Adicionar filme\n" \
                "2. Alterar dados\n" \
                "3. Listar filmes\n" \
                "4. Remover filme\n" \
                "0. Menu\n")
        
        opcao = self.verificar_inteiro("Digite a opção: ")
        return opcao
    
    def tela_filtros_de_relatorios(self):
        print("." * 10,"RELATÓRIO DE INDICAÇÕES","." * 10)
        print("\n1. Listar todos os indicados\n" \
                "2. Listar indicados por ano\n" \
                "3. Listar indicados por categoria\n" \
                "0. Menu de indicação de filmes\n")

        opcao = self.verificar_inteiro("Digite a opção: ")
        return opcao
    
    def pegar_dados_filme(self):
        print("." * 15, "INDICAR FILME", "." * 15)

        titulo = input("\nTítulo: ").strip().title()
        sinopse = input("Sinopse: ")
        titulo_categoria = input("Categoria: ").strip().title()
        categoria = self.__controlador_sistema.controlador_categoria.pegar_categoria_por_titulo(titulo_categoria)
        
        if categoria is None:
            self.mostrar_mensagem("\nCategoria não encontrada. Cadastre a categoria primeiro.")
            return None
        
        anos_validos = list(range(2020,2026))
        ano_indicacao = self.verificar_inteiro("Ano de indicação: ", anos_validos)

        return {"titulo": titulo, "sinopse": sinopse, "categoria": categoria, "ano_indicacao": ano_indicacao}
    
    def mostrar_dados_filme(self, dados_filme):
        print("Filme: ", dados_filme["titulo"])
        print("Sinopse: ", dados_filme["sinopse"])
        print("Categoria: ", dados_filme["categoria"].titulo)
        print("Ano de indicação: ", dados_filme["ano_indicacao"])
        print("\n")

    def buscar_filme_por_titulo(self):
        filme = input("Digite o título do filme: ").strip().title()
        return filme

    def buscar_indicados_por_categoria(self):
        categoria = input("Digite a categoria a qual deseja filtrar: ").strip().title()
        return categoria
    
    def buscar_indicados_por_ano(self):
        anos_validos = list(range(2020,2026))
        ano_indicacao = self.verificar_inteiro("Digite o ano de indicação o qual deseja filtrar: ", anos_validos)
        return ano_indicacao
    
    def verificar_inteiro(self, msg=" ", opcoes_validas = None):
        while True:
            entrada = input(msg)
            try:
                numero_int = int(entrada) 
                if opcoes_validas and numero_int not in opcoes_validas:
                    raise ValueError
                return numero_int
            except ValueError:
                print("Valor incorreto!")
                if opcoes_validas:
                    print("Valores válidos: ", opcoes_validas)

    def mostrar_mensagem(self, msg):
        print(msg)
