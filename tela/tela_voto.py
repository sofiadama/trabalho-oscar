class TelaVoto:
  
  def autentificacao_membro(self, id):
    print("---- AUTENTIFICAÇÃO ------")
    id = input("ID: ")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("*" * 15, "CADASTRO DE VOTOS","*" * 15)
    print("\n1. Votar\n" \
            "2. Alterar voto\n" \
            "3. Listar votos\n" \
            "4. Remover voto\n" \
            "0. Menu\n")
        
    opcao = int(input("Digite a opção: "))
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pegar_dados_voto(self):
    print("-------- DADOS VOTO ----------")
    membro = input("Membro: ")
    indicado = input("Indicado: ")
    ano = input("Ano: ")

    return {"nome": nome, "telefone": telefone, "cpf": cpf}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostrar_voto(self, dados_voto):
    print("Votante: ", dados_voto["membro"])
    print("Indicado: ", dados_voto["indicado"])
    print("Ano: ", dados_voto["ano"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def buscar_voto(self):
    voto = input("Buscar voto: ")
    return voto

  def mostra_mensagem(self, msg):
    print(msg)