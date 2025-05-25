class TelaAtor():

    def tela_opcoes(self):
        print("*" * 15,"INDICAÇÃO DE ATORES","*" * 15)
        print("\n1. Adicionar ator\n" \
                "2. Alterar dados\n" \
                "3. Listar atores\n" \
                "4. Remover ator\n" \
                "0. Menu\n")
        try:
            opcao = int(input("Escolha a opcao: "))
            return opcao
        except ValueError:
            self.mostrar_mensagem("Opção inválida. Digite um número.")
            return -1
    
    def pegar_dados_ator(self):
        print("*" * 15, "INDICAR ATOR", "*" * 15)

        nome = input("\nNome: ").title()
        nacionalidade = input("Nacionalidade: ").capitalize()
        categoria = "Melhor Ator"
        filme = input("Filme: ").title()
        ano_indicacao = int(input("Ano de indicação: "))

        return {"nome": nome, "nacionalidade": nacionalidade, "categoria": categoria, "filme": filme, "ano de indicacao": ano_indicacao}
    
    def mostrar_dados_ator(self, dados_ator):
        print("Ator: ", dados_ator["nome"])
        print("Nacionalidade: ", dados_ator["nacionalidade"])
        print("Categoria: ", dados_ator["categoria"])
        print("Filme: ", dados_ator["filme"])
        try:
            print("Ano de indicação: ", int(dados_ator["ano de indicacao"]))
        except (ValueError, KeyError):
            self.mostrar_mensagem("Ano inválido. Use apenas números.")
            return None
        print("\n")

    def buscar_ator(self):
        ator = input("Buscar ator: ").title
        return ator

    def mostrar_mensagem(self, msg):
        print(msg)
