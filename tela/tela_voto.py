class TelaVoto:

    def autentificacao_membro(self):
        print("---- AUTENTICAÇÃO DE MEMBRO ------")
        while True:
            try:
                id_membro = int(input("Digite o ID do membro: "))
                return id_membro
            except ValueError:
                print("ID inválido. Digite um número inteiro.")

    def tela_opcoes(self):
        while True:
            print("\n" + "*" * 15, "CADASTRO DE VOTOS", "*" * 15)
            print("1 - Votar")
            print("2 - Alterar voto")
            print("3 - Listar votos")
            print("4 - Remover voto")
            print("0 - Menu")

            try:
                opcao = int(input("Digite a opção: "))
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Digite um número inteiro válido.")

    def pegar_dados_voto(self):
        print("\n-------- DADOS DO VOTO ----------")
        try:
            membro_id = int(input("ID do membro: "))
            indicado_id = int(input("ID do indicado: "))
            ano = int(input("Ano da premiação: "))
            return {"membro": membro_id, "indicado": indicado_id, "ano": ano}
        except ValueError:
            print("Erro: Digite valores válidos (números inteiros).")
            return self.pegar_dados_voto()  # Tenta novamente

    def mostrar_voto(self, dados_voto):
        print("\n--- VOTO ---")
        print("ID do Membro:", dados_voto["membro"])
        print("ID do Indicado:", dados_voto["indicado"])
        print("Ano:", dados_voto["ano"])
        print("-" * 30)

    def buscar_voto(self):
        try:
            voto_id = int(input("Digite o ID do voto que deseja buscar: "))
            return voto_id
        except ValueError:
            print("ID inválido. Digite um número inteiro.")
            return self.buscar_voto()

    def mostra_mensagem(self, msg):
        print("\n" + str(msg))
