class TelaCategoria():
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("*" * 15,"CADASTRO DE CATEGORIAS","*" * 15)
        print("\n1. Adicionar categoria\n" \
                "2. Alterar título\n" \
                "3. Listar categorias\n" \
                "4. Remover categoria\n" \
                "0. Menu\n")

        opcao = int(input("Digite a opção: "))
        return opcao

    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pegar_dados_categoria(self):
        print("*" * 15, "CADASTRAR CATEGORIA", "*" * 15)
        titulo = input("Titulo: ")

        return {"titulo": titulo}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostrar_categoria(self, dados_categoria):
        print("Categoria: ", dados_categoria["titulo"])
        print("\n")
        
    def buscar_categoria(self):
        titulo = input("Buscar categoria: ")
        return titulo
    
    def mostrar_mensagem(self, msg):
        print(msg)


