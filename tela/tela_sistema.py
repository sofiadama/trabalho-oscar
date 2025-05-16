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
        print("----- Votação do Oscar -----\n")
        print("\n1. Cadastros" \
                "2. Indicações" \
                "3. Votos" \
                "0. Encerrar\n")
        
        opcao = self.le_num_inteiro("Digite a opção: ", [0,1,2,3])
        return opcao

    def tela_opcoes_cadastros(self):
        print("------ Cadastros ------\n")
        print("1. Cadastrar Membro" \
              "2. Cadastrar Categoria" \
              "0. Retornar ao Menu\n")
        
        opcao = self.le_num_inteiro("Digite a opção: ", [0,1,2])
        return opcao

    def tela_opcoes_indicacoes(self):
        print("------ Indicações ------\n")
        print("1. Indicar Ator" \
              "2. Indicar Diretor" \
              "3. Indicar Filme" \
              "0. Retornar ao Menu\n")
        
        opcao = self.le_num_inteiro("Digite a opção: ", [0,1,2,3])
        return opcao

    def tela_opcoes_votos(self):
        print("------ Votos ------\n")
        print("1. Votar em Ator" \
              "2. Votar em Diretor" \
              "3. Votar em Filme" \
              "4. Gerar Relatório" \
              "0. Retornar ao Menu\n")
        
        opcao = self.le_num_inteiro("Digite a opção: ", [0,1,2,3,4])
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

