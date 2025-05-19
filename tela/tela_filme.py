class TelaFilme:
    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")

    def mostra_filmes(self, filmes):
        print("\n--- Filmes Indicados ---")
        for i, filme in enumerate(filmes, start=1):
            print(f"{i}. {filme.titulo} | Diretor: {filme.diretor.nome} | Categoria: {filme.categoria.nome}")
        print()

    def pegar_dados_filme(self):
        print("\n--- Cadastro de Filme ---")
        titulo = input("Título do Filme: ")
        id_diretor = input("ID do Diretor: ")
        id_categoria = input("ID da Categoria: ")
        return {
            "titulo": titulo,
            "id_diretor": id_diretor,
            "id_categoria": id_categoria
        }

    def selecionar_filme(self):
        escolha = input("Digite o número do filme desejado: ")
        return escolha

    def menu(self):
        print("\n--- Menu Filme ---")
        print("1 - Cadastrar Filme")
        print("2 - Listar Filmes")
        print("3 - Alterar Filme")
        print("4 - Remover Filme")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")
        return opcao
