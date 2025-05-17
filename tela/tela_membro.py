class TelaMembro:
    def tela_opcoes(self):
        print("-------- MEMBROS ----------")
        print("Escolha a opção:")
        print("1 - Incluir Membro")
        print("2 - Alterar Membro")
        print("3 - Listar Membros")
        print("4 - Excluir Membro")
        print("0 - Retornar")

        while True:    #se a entrada for não for um numero entre 0 e 4
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    print("Opção inválida. Digite um número entre 0 e 4.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def pegar_dados_membro(self):
        print("-------- DADOS MEMBRO ----------")
        nome = input("Nome: ")
        nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        nacionalidade = input("Nacionalidade: ")
        id = input("ID: ")

        return {"id": id, "nome": nome, "nascimento": nascimento, "nacionalidade": nacionalidade}

    def mostrar_membro(self, dados_membro):
        print("ID do Membro: ", dados_membro["id"])
        print("Nome: ", dados_membro["nome"])
        print("Data de nascimento: ", dados_membro["nascimento"])
        print("Nacionalidade: ", dados_membro["nacionalidade"])
        print("\n")

    def selecionar_membro(self):
        id = input("Digite o ID do membro que deseja selecionar: ")
        return id

    def mostrar_mensagem(self, msg):
        print(msg)


    
