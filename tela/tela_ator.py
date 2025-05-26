from entidade.categoria import Categoria

class TelaAtor():
    
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def tela_opcoes(self):
        print("." * 15,"INDICAÇÃO DE ATORES","." * 15)
        print("\n1. Adicionar ator\n" \
                "2. Alterar dados\n" \
                "3. Listar atores\n" \
                "4. Remover ator\n" \
                "0. Menu\n")
        try:
            opcao = int(input("Escolha a opcao: "))
            return opcao
        except ValueError:
            self.mostrar_mensagem("Opção inválida. Digite um número.")
            return -1

    def tela_filtros_de_relatorios(self):
        print("." * 10,"RELATÓRIO DE INDICAÇÕES","." * 10)

        print("\n1. Listar todos os indicados\n" \
                "2. Listar indicados por ano\n" \
                "0. Menu de indicação de atores")
        
        opcao = self.verificar_inteiro("\nDigite a opção: ", [0,1,2])
        return opcao
    
    def pegar_dados_ator(self):
        print("." * 15, "INDICAR ATOR", "." * 15)

        nome = input("\nNome: ").strip().title()
        nacionalidade = input("Nacionalidade: ").capitalize()
        categoria = Categoria("Melhor Ator")
        
        if categoria is None:
            self.mostrar_mensagem("\nCategoria não encontrada. Cadastre a categoria primeiro.")
            return None
        
        titulo_filme = input("Filme: ").strip().title()
        filme = self.__controlador_sistema.controlador_filme.pegar_filme_por_titulo(titulo_filme)
        
        anos_validos = list(range(2020,2026))
        ano_indicacao = self.verificar_inteiro("Ano de indicação: ", anos_validos)

        return {"nome": nome, "nacionalidade": nacionalidade, "categoria": categoria, "filme": filme, "ano_indicacao": ano_indicacao}
    
    def mostrar_dados_ator(self, dados_ator):
        print("Ator: ", dados_ator["nome"])
        print("Nacionalidade: ", dados_ator["nacionalidade"])
        print("Categoria: ", dados_ator["categoria"].titulo)
        print("Filme: ", dados_ator["filme"].titulo)
        try:
            print("Ano de indicação: ", int(dados_ator["ano_indicacao"]))
        except (ValueError, KeyError):
            self.mostrar_mensagem("\nAno inválido. Use apenas números.")
            return None
        print("\n")

    def buscar_ator_por_nome(self):
        ator = input("\nDigite o nome do ator que deseja buscar: ").strip().title()
        return ator
    
    def buscar_indicados_por_ano(self):
        anos_validos = list(range(2020,2026))
        ano_indicacao = self.verificar_inteiro("\nDigite o ano de indicação o qual deseja filtrar: ", anos_validos)
        return ano_indicacao
    
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

