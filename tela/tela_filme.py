class TelaFilme():

    def tela_opcoes(self):
        print("*" * 15,"INDICAÇÃO DE FILMES","*" * 15)
        print("\n1. Adicionar filme\n" \
                "2. Alterar dados\n" \
                "3. Listar filmes\n" \
                "4. Remover filme\n" \
                "0. Menu\n")
        
        opcao = self.le_num_inteiro("Digite a opção: ")
        return opcao
    
    def tela_opcoes_filtros(self):
        print("*" * 15,"RELATÓRIO DE INDICAÇÕES","*" * 15)
        print("\n1. Filtrar por categoria\n" \
                "2. Filtrar por ano\n" \
                "3. Obter relatório completo\n" \
                "0. Menu\n")

        opcao = self.le_num_inteiro("Digite a opção: ")
        return opcao
    
    def pegar_dados_filme(self):
        print("*" * 15, "INDICAR FILME", "*" * 15)

        titulo = input("\nTítulo: ").title()
        sinopse = input("Sinopse: ")
        categoria = input("Categoria: ").title()
        ano_indicacao = self.le_num_inteiro("Ano de indicação: ")

        return {"titulo": titulo, "sinopse": sinopse, "categoria": categoria, "ano de indicacao": ano_indicacao}
    
    def mostrar_dados_filme(self, dados_filme):
        print("Filme: ", dados_filme["titulo"])
        print("Sinopse: ", dados_filme["sinopse"])
        print("Categoria: ", dados_filme["categoria"])
        print("Ano de indicação: ", dados_filme["ano de indicacao"])
        print("\n")

    def buscar_filme_por_titulo(self):
        filme = input("Digite o título do filme: ").title
        return filme

    def buscar_categoria(self):
        categoria = input("Digite a categoria a qual deseja filtrar: ").title()
        return categoria
    
    def buscar_ano_indicacao(self):
        ano_indicacao = self.le_num_inteiro("Digite o ano de indicação o qual deseja filtrar: ")
        return ano_indicacao
    
    def le_num_inteiro(self, mensagem=" ", ints_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido) 
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError 
                return valor_int
            except ValueError: 
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

    def mostrar_mensagem(self, msg):
        print(msg)
