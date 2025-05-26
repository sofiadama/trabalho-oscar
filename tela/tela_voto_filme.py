class TelaVotoFilme:
    
    def tela_votos_em_filmes(self):
        print("." * 15,"VOTOS EM FILMES","." * 15)

        print("\n1. Adicionar Voto\n" \
                "2. Alterar Voto\n" \
                "3. Listar Votos\n" \
                "4. Remover Voto\n" \
                "0. Menu de Votos")
        
        opcao = self.verificar_inteiro("\nDigite a opção: ", [0,1,2,3,4])
        return opcao

    def tela_filtros_de_relatorios(self):
        print("." * 15,"FILTROS","." * 15)

        print("\n1. Listar todos os votos\n" \
                "2. Listar votos por ano\n" \
                "3. Listar votos por categoria\n" \
                "0. Menu de votos em filmes")
        
        opcao = self.verificar_inteiro("\nDigite a opção: ", [0,1,2,3])
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