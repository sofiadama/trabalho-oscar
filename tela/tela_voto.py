class TelaVoto():

    def autenticacao_membro(self):
        print("----- AUTENTIFICAÇÃO -----")
        id = int(input("\nDigite seu ID para autentificação: "))
        return id
    
    def tela_tipo_indicados(self):
        print("*" * 15,"VOTAR EM:","*" * 15)
        print("\n1. Atores\n" \
                "2. Diretores\n" \
                "3. Filmes\n" \
                "0. Menu\n")
        
        opcao = int(input("Digite a opção: "))
        return opcao
    
    def tela_votos_em_atores(self):
        print("*" * 15,"VOTOS EM ATORES","*" * 15)
        print("\n1. Adicionar voto\n" \
                "2. Alterar voto\n" \
                "3. Listar votos\n" \
                "4. Remover voto\n" \
                "0. Menu\n")
        
        opcao = int(input("Digite a opção: "))
        return opcao
    
    def tela_votos_em_diretores(self):
        print("*" * 15,"VOTOS EM DIRETORES","*" * 15)
        print("\n1. Adicionar voto\n" \
                "2. Alterar voto\n" \
                "3. Listar votos\n" \
                "4. Remover voto\n" \
                "0. Menu\n")
        
        opcao = int(input("Digite a opção: "))
        return opcao
    
    def tela_votos_em_filmes(self):
        print("*" * 15,"VOTOS EM FILMES","*" * 15)
        print("\n1. Adicionar voto\n" \
                "2. Alterar voto\n" \
                "3. Listar votos\n" \
                "4. Remover voto\n" \
                "0. Menu\n")
        
        opcao = int(input("Digite a opção: "))
        return opcao
    
    def pegar_dados_voto(self):
        print("*" * 15, "VOTAR", "*" * 15)

        indicado = input("\nIndicado: ").title()
        categoria = input("Categoria: ").title()
        ano = int(input("Ano de votação: "))

        return {"indicado": indicado, "categoria": categoria, "ano": ano}
    
    def mostrar_dados_voto(self, dados_voto):
        
        print("Membro: ", dados_voto["membro"])
        print("Indicado: ", dados_voto["indicado"])
        print("Categoria: ", dados_voto["categoria"])
        print("Ano de votação: ", dados_voto["ano"])
        print("\n")

    def buscar_voto(self):
        categoria = input("Buscar voto na categoria: ").title
        return categoria

    def mostrar_mensagem(self, msg):
        print(msg)
