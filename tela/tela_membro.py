class TelaMembro():

    def tela_opcoes(self):
        print("." * 15,"CADASTRO DE MEMBROS","." * 15)
        print("\n1. Adicionar membro\n" \
                "2. Alterar dados\n" \
                "3. Listar membros\n" \
                "4. Remover membro\n" \
                "0. Menu\n")
        
        opcao = int(input("Digite a opção: "))
        return opcao
    
    def pegar_dados_membro(self):
        print("." * 15, "CADASTRAR MEMBRO", "." * 15)

        id = int(input("\nID: "))
        nome = input("Nome: ").strip().title()
        nascimento = input("Nascimento: ")
        nacionalidade = input("Nacionalidade: ").capitalize()

        return {"id": id, "nome": nome, "nascimento": nascimento, "nacionalidade": nacionalidade}
    
    def mostrar_dados_membro(self, dados_membro):
        print("\nID: ", dados_membro["id"])
        print("Nome: ", dados_membro["nome"])
        print("Nascimento: ", dados_membro["nascimento"])
        print("Nacionalidade: ", dados_membro["nacionalidade"])
        print("\n")

    def buscar_membro(self):
        membro = int(input("Buscar ID do membro: "))
        return membro

    def mostrar_mensagem(self, msg):
        print(msg)
