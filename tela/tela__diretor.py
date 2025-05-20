class TelaDiretor():

    def tela_opcoes(self):
        print("*" * 15,"INDICAÇÃO DE DIRETORES","*" * 15)
        print("\n1. Adicionar diretor\n" \
                "2. Alterar dados\n" \
                "3. Listar diretores\n" \
                "4. Remover diretor\n" \
                "0. Menu\n")
        
        opcao = int(input("Digite a opção: "))
        return opcao
    
    def pegar_dados_diretor(self):
        print("*" * 15, "INDICAR DIRETOR", "*" * 15)

        nome = input("\nNome: ").title()
        nacionalidade = input("Nacionalidade: ").capitalize()
        categoria = "Melhor Diretor"
        filme = input("Filme: ").title()
        ano_indicacao = int(input("Ano de indicação: "))

        return {"nome": nome, "nacionalidade": nacionalidade, "categoria": categoria, "filme": filme, "ano de indicacao": ano_indicacao}
    
    def mostrar_dados_diretor(self, dados_diretor):
        print("Diretor: ", dados_diretor["nome"])
        print("Nacionalidade: ", dados_diretor["nacionalidade"])
        print("Categoria: ", dados_diretor["categoria"])
        print("Filme: ", dados_diretor["filme"])
        print("Ano de indicação: ", dados_diretor["ano de indicacao"])
        print("\n")

    def buscar_diretor(self):
        diretor = input("Buscar diretor: ").title
        return diretor

    def mostrar_mensagem(self, msg):
        print(msg)
