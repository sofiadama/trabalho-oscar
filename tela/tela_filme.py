class TelaFilme():

    def tela_opcoes(self):
        print("*" * 15,"INDICAÇÃO DE FILMES","*" * 15)
        print("\n1. Adicionar filme\n" \
                "2. Alterar dados\n" \
                "3. Listar filmes\n" \
                "4. Remover filme\n" \
                "0. Menu\n")
        
        opcao = int(input("Digite a opção: "))
        return opcao
    
    def pegar_dados_filme(self):
        print("*" * 15, "INDICAR FILME", "*" * 15)

        titulo = input("\nTítulo: ").title()
        sinopse = input("Sinopse: ")
        categoria = input("Categoria: ").title()
        ano_indicacao = int(input("Ano de indicação: "))

        return {"titulo": titulo, "sinopse": sinopse, "categoria": categoria, "ano de indicacao": ano_indicacao}
    
    def mostrar_dados_filme(self, dados_filme):
        print("Filme: ", dados_filme["titulo"])
        print("Sinopse: ", dados_filme["sinopse"])
        print("Categoria: ", dados_filme["categoria"])
        print("Ano de indicação: ", dados_filme["ano de indicacao"])
        print("\n")

    def buscar_filme(self):
        filme = input("Buscar filme: ").title
        return filme

    def mostrar_mensagem(self, msg):
        print(msg)
