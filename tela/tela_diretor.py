class TelaDiretor():

    def tela_opcoes(self):
        print("*" * 15,"INDICAÇÃO DE DIRETORES","*" * 15)
        print("\n1. Adicionar diretor\n" \
                "2. Alterar dados\n" \
                "3. Listar diretores\n" \
                "4. Remover diretor\n" \
                "0. Menu\n")
        
        try: # se a entrada nao for um int entre 0 e 4
            opcao = int(input("Escolha a opcao: "))
            return opcao
        except ValueError:
            self.mostrar_mensagem("Opção inválida. Digite um número.")
            return -1
    
    def pegar_dados_diretor(self):
        print("*" * 15, "INDICAR DIRETOR", "*" * 15)

        nome = input("\nNome: ").title()
        nacionalidade = input("Nacionalidade: ").capitalize()
        categoria = "Melhor Diretor"
        filme = input("Filme: ").title()
        
        try: # se a entrada nao for um int
         ano_indicacao = int(input("Ano de indicação: "))
        except ValueError:
         self.mostrar_mensagem("Ano inválido. Use apenas números.")
        return None
        

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

