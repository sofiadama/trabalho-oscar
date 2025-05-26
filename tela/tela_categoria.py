class TelaCategoria():

    def tela_opcoes(self):
        print("." * 15,"CADASTRO DE CATEGORIAS","." * 15)
        print("\n1. Adicionar categoria\n" \
                "2. Alterar título\n" \
                "3. Listar categorias\n" \
                "4. Remover categoria\n" \
                "0. Menu\n")
        try:
            opcao = int(input("Escolha a opcao: "))
            return opcao
        except ValueError:
            self.mostrar_mensagem("Opção inválida. Digite um número.")
            return -1
    
    def pegar_dados_categoria(self):
        print("." * 15, "CADASTRAR CATEGORIA", "." * 15)

        titulo = input("\nTítulo: ").strip().title()

        return {"titulo": titulo}
    
    def mostrar_dados_categoria(self, dados_categoria):
        print(dados_categoria["titulo"])

    def buscar_categoria(self):
        categoria = input("Buscar categoria: ").strip().title()
        return categoria

    def mostrar_mensagem(self, msg):
        print(msg)

