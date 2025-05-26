from entidade.categoria import Categoria

class TelaDiretor():
    
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def tela_opcoes(self):
        print("." * 15,"INDICAÇÃO DE DIRETORES","." * 15)
        print("\n1. Adicionar diretor\n" \
                "2. Alterar dados\n" \
                "3. Listar diretores\n" \
                "4. Remover diretor\n" \
                "0. Menu\n")
        
        try: # se a entrada nao for um int entre 0 e 4
            opcao = int(input("Escolha a opcao: "))
            return opcao
        except ValueError:
            self.mostrar_mensagem("Opção inválida. Digite um número.")
            return -1
        
    def tela_filtros_de_relatorios(self):
        print("." * 10,"RELATÓRIO DE INDICAÇÕES","." * 10)

        print("\n1. Listar todos os indicados\n" \
                "2. Listar indicados por ano\n" \
                "0. Menu de indicação de diretores\n")
        
        opcao = self.verificar_inteiro("Digite a opção: ", [0,1,2])
        return opcao
    
    def pegar_dados_diretor(self):
        print("." * 15, "INDICAR DIRETOR", "." * 15)

        nome = input("\nNome: ").title()
        nacionalidade = input("Nacionalidade: ").capitalize()
        categoria = Categoria("Melhor Diretor")
        titulo_filme = input("Filme: ").title()
        filme = self.__controlador_sistema.controlador_filme.pegar_filme_por_titulo(titulo_filme)
        
        anos_validos = list(range(2020,2026))
        ano_indicacao = self.verificar_inteiro("Ano de indicação: ", anos_validos)

        return {"nome": nome, "nacionalidade": nacionalidade, "categoria": categoria, "filme": filme, "ano_indicacao": ano_indicacao}
    
    def mostrar_dados_diretor(self, dados_diretor):
        print("Diretor: ", dados_diretor["nome"])
        print("Nacionalidade: ", dados_diretor["nacionalidade"])
        print("Categoria: ", dados_diretor["categoria"].titulo)
        print("Filme: ", dados_diretor["filme"].titulo)
        try:
            print("Ano de indicação: ", int(dados_diretor["ano_indicacao"]))
        except (ValueError, KeyError):
            self.mostrar_mensagem("Ano inválido. Use apenas números.")
            return None
        print("\n")

    def buscar_diretor_por_nome(self):
        diretor = input("Buscar diretor: ").strip().title()
        return diretor
    
    def buscar_indicados_por_ano(self):
        anos_validos = list(range(2020,2026))
        ano_indicacao = self.verificar_inteiro("Digite o ano de indicação o qual deseja filtrar: ", anos_validos)
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
                print("Valor incorreto!")
                if opcoes_validas:
                    print("Valores válidos: ", opcoes_validas)

    def mostrar_mensagem(self, msg):
        print(msg)


