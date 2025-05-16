class TelaAtor():

    def tela_opcoes(self):
        print("*" * 15,"INDICAÇÃO DE ATORES","*" * 15)
        print("\n1. Adicionar ator\n" \
                "2. Alterar dados\n" \
                "3. Listar atores\n" \
                "4. Remover ator\n" \
                "0. Menu\n")
        
        opcao = int(input("Digite a opção: "))
        return opcao
    
    def pegar_dados_ator(self):
        print("*" * 15, "INDICAR ATOR", "*" * 15)

        nome = input("\nNome: ")
        nacionalidade = input("Nacionalidade: ")
        ano_indicacao = int(input("Ano de indicação: "))
        filme = input("Filme: ")
        categoria = "Melhor Ator"

        return {"nome": nome, "nacionalidade": nacionalidade, "ano de indicacao": ano_indicacao, "filme": filme, "categoria": categoria}
    
    def mostrar_dados_ator(self, dados_ator):
        print("Ator: ", dados_ator["nome"])
        print("Nacionalidade: ", dados_ator["nacionalidade"])
        print("Ano de indicação: ", dados_ator["ano de indicacao"])
        print("Filme: ", dados_ator["filme"])
        print("Categoria: ", dados_ator["categoria"])
        print("\n")

    def buscar_ator(self):
        ator = input("Buscar ator: ")
        return ator

    def mostrar_mensagem(self, msg):
        print(msg)
