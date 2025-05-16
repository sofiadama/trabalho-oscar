class TelaDiretor:
  
  def tela_opcoes(self):
    print("-------- DIRETORES ----------")
    print("Escolha a opção")
    print("1 - Incluir Diretor")
    print("2 - Alterar Diretor")
    print("3 - Listar Diretores")
    print("4 - Excluir Diretor")
    print("0 - Retornar")

    opcao = int(input("Escolha a opção: "))
    return opcao

  def pegar_dados_diretor(self):
    print("-------- DADOS DIRETOR ----------")
    id = int(input("ID: "))
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    nacionalidade = input("Nacionalidade: ")

    return {
      "nome": nome,
      "nacionalidade": nacionalidade
      "categoria" : categoria
      "filme" : filme
      "ano_indicação" : ano_indicação  
    }

  def mostrar_diretor(self, dados_diretor):
    print("NOME DO DIRETOR: ", dados_diretor["nome"])
    print("CATEGORIA:  " ,dados_diretor["categoria"])
    print("FILME:  " , dados_diretor["filme"])
    print("ANO_INDICAÇÃO:  " dados_diretor["ano_indicação"])
    print("NACIONALIDADE: ", dados_diretor["nacionalidade"])
    print("\n")

  def selecionar_diretor(self):
    id = int(input("ID do diretor que deseja selecionar: "))
    return id

  def mostrar_mensagem(self, msg):
    print(msg)

