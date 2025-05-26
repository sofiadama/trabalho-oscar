class TelaSistema:

    def tela_opcoes_principais(self):
        print()
        print("*" * 15,"OSCARS MENU","*" * 15)

        print("\n1. Cadastros\n" \
                "2. Indicações\n" \
                "3. Votações\n" \
                "0. Sair")
        
        opcao = self.verificar_inteiro("\nDigite a opção: ", [0,1,2,3])
        return opcao

    def tela_opcoes_cadastros(self):
        print("." * 15,"CADASTROS","." * 15)

        print("\n1. Cadastro de Membros\n" \
                "2. Cadastro de Categorias\n" \
                "0. Menu Principal")
        
        opcao = self.verificar_inteiro("\nDigite a opção: ", [0,1,2])
        return opcao

    def tela_opcoes_indicacoes(self):
        print("." * 15,"INDICAÇÕES","." * 15)

        print("\n1. Indicações de Atores\n" \
                "2. Indicações de Diretores\n" \
                "3. Indicações de Filmes\n" \
                "0. Menu Principal")
        
        opcao = self.verificar_inteiro("\nDigite a opção: ", [0,1,2,3])
        return opcao

    def tela_opcoes_votos(self):
        print("." * 15,"VOTOS","." * 15)

        print("\n1. Registros de Votações\n" \
                "2. Relatórios de Vencedores\n" \
                "0. Menu Principal")
        
        opcao = self.verificar_inteiro("\nDigite a opção: ", [0,1,2])
        return opcao
    
    def verificar_inteiro(self, msg=" ", opcoes_validas = None):
        while True:
            entrada = input(msg)
            try:
                numero_int = int(entrada) 
                if opcoes_validas and numero_int not in opcoes_validas:
                    raise ValueError
                return numero_int
            except ValueError:
                print("\nValor incorreto!")
                if opcoes_validas:
                    print("Valores válidos: ", opcoes_validas)

    def mostrar_mensagem(self, msg):
        print(msg)



