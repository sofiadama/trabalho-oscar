from entidade.categoria import Categoria

class TelaVoto:

    def autenticacao_membro(self):
        print("*" * 15,"AUTENTICAÇÃO","*" * 15)
        while True:        
            try:
                id = int(input("\nDigite seu ID para autenticação: "))
                return id
            except ValueError:
                self.mostrar_mensagem("ID inválido! Digite apenas números.")
                return 
    
    def tela_filtros_de_relatorios(self):
        print("." * 15,"FILTROS","." * 15)

        print("\n1. Listar vencedores \n" \
                "2. Listar vencedores por ano\n" \
                "3. Listar vencedores por categoria\n" \
                "4. BÔNUS: Listar filmes mais premiados\n" \
                "0. Menu de Votos")
        
        opcao = self.verificar_inteiro("\nDigite a opção: ", [0,1,2,3,4])
        return opcao
    
    def tela_tipos_de_votos(self):
        print("." * 15,"VOTOS","." * 15)

        print("\n1. Votos em Atores\n" \
                "2. Votos em Diretores\n" \
                "3. Votos em Filmes\n" \
                "0. Menu de Votos")
        
        opcao = self.verificar_inteiro("\nDigite a opção: ", [0,1,2,3])
        return opcao
    
    def pegar_dados_voto(self):
        anos_validos = list(range(2020, 2026))

        print("." * 15,"VOTAR", "." * 15)

        indicado = input("\nIndicado: ").strip().title()
        titulo_categoria = input("Categoria: ").strip().title()
    
        try:
            categoria = Categoria(titulo_categoria)
        except KeyError:
            print("Categoria inválida! Digite uma categoria existente.")
            return None
        ano = self.verificar_inteiro("Ano de votação: ", anos_validos)

        return {"indicado": indicado, "categoria": categoria, "ano": ano}
    
    def mostrar_dados_voto(self, dados_voto):
        print("\nMembro: ", dados_voto["membro"])
        print("Indicado: ", dados_voto["indicado"])
        print("Categoria: ", dados_voto["categoria"])
        print("Ano de votação: ", dados_voto["ano"])
        print("\n")

    def buscar_voto_por_ano(self):
        ano = self.verificar_inteiro("Buscar voto no ano de: ")
        return ano
    
    def buscar_voto_por_categoria(self):
        categoria = input("Buscar voto na categoria: ").strip().title()
        return categoria
    
    def buscar_vencedor_por_ano(self):
        ano = self.verificar_inteiro("Buscar vencedores no ano de: ")
        return ano
    
    def buscar_vencedor_por_categoria(self):
        categoria = input("Buscar vencedores na categoria: ").strip().title()
        return categoria

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
