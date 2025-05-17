class TelaCategoria():
    def tela_opcoes(self):
        while True:
            print("\n" + "*" * 15, "CADASTRO DE CATEGORIAS", "*" * 15)
            print("1 - Adicionar categoria")
            print("2 - Alterar título")
            print("3 - Listar categorias")
            print("4 - Remover categoria")
            print("0 - Menu")

            try:
                opcao = int(input("Digite a opção: "))
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Digite um número inteiro válido.")

    def pegar_dados_categoria(self):
        print("\n" + "*" * 15, "CADASTRAR CATEGORIA", "*" * 15)
        titulo = input("Título da categoria: ").strip()
        while not titulo:
            print("Título não pode ser vazio.")
            titulo = input("Título da categoria: ").strip()
        return {"titulo": titulo}

    def mostrar_categoria(self, dados_categoria):
        print("\n--- Categoria ---")
        print("Título:", dados_categoria["titulo"])
        print("-" * 30)

    def buscar_categoria(self):
        titulo = input("Digite o título da categoria que deseja buscar: ").strip()
        while not titulo:
            print("Título não pode ser vazio.")
            titulo = input("Digite o título da categoria que deseja buscar: ").strip()
        return titulo

    def mostrar_mensagem(self, msg):
        print(f"\n{msg}")

    
    def mostrar_mensagem(self, msg):
        print(msg)


