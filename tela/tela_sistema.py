class TelaSistema:

    #essa função trata o caso de não digitar um valor valido
    #note que está dentro de um while True. Só sai do loop quando digitado um valor correto
    def le_num_inteiro(self, mensagem=" ", ints_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido) #tenta transformar o valor lido em inteiro.
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError #será lançada apenas se o número não é o esperado
                return valor_int
            except ValueError: #aqui cai se não for int ou se não for valido
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

    def tela_opcoes_principais(self):
        print("----- Votação do Oscar -----")
        print("\n1. Cadastros\n" \
                "2. Indicações\n" \
                "3. Votos\n" \
                "0. Encerrar\n")
        
        opcao = self.le_num_inteiro("Digite a opção: ", [0,1,2,3])
        return opcao

    def tela_opcoes_cadastros(self):
        print("------ Cadastros ------")
        print("\n1. Cadastrar Membro\n" \
                "2. Cadastrar Categoria\n" \
                "0. Menu\n")
        
        opcao = self.le_num_inteiro("Digite a opção: ", [0,1,2])
        return opcao

    def tela_opcoes_indicacoes(self):
        print("------ Indicações ------")
        print("\n1. Indicar Ator\n" \
                "2. Indicar Diretor\n" \
                "3. Indicar Filme\n" \
                "0. Menu\n")
        
        opcao = self.le_num_inteiro("Digite a opção: ", [0,1,2,3])
        return opcao

    def tela_opcoes_votos(self):
        print("*" * 15,"VOTOS","*" * 15)
        print("\n1. Votar\n" \
                "2. Listar votos\n" \
                "0. Menu\n")
        
        opcao = self.le_num_inteiro("Digite a opção: ", [0,1,2])
        return opcao

if __name__ == "__main__":
    tela = TelaSistema()
    while True:
        opcao = tela.tela_opcoes_principais()
        if opcao == 0:
            print("Encerrando o sistema.")
            break
        elif opcao == 1:
            tela.tela_opcoes_cadastros()
        elif opcao == 2:
            tela.tela_opcoes_indicacoes()
        elif opcao == 3:
            tela.tela_opcoes_votos()

