# exercicio desafio 3
# Agenda de Contatos

agenda={"teste1":{"99699441":"teste1@email.com"},"teste2":{"89896565":"teste2@email.com"}}
v=True

def remove():
    lnome=input("Digite o nome que quer remover -> ")
        
    if lnome in agenda:
        print(f"O Contato {lnome} será removido.")
        print("Digite 'S' ou 's' para remover ou qualquer outra tecla para cancelar.")
        confirma=""
        confirma=input(" - > ")
        if confirma=="S" or confirma=="s":
            del agenda[lnome]
            print(f"O contato {lnome} foi removido com sucesso.")
        else:
            print(f"O contato {lnome} não foi removido")
            return              
    else:
        print(f"{lnome} não está na agenda.")           
    return

def procura() -> str:
    lnome=input("Digite o nome que procura-> ")
    #print(lnome)
    if lnome in agenda:
        print(f"{lnome} {agenda[lnome]}")          
    else:
        print(f"{lnome} não está na agenda.")       
    return

def validatel() -> str:
    valida=False
    while valida==False:
           cond1=0
           tel=input("Digite um telefone com 8 caracteres-> ")
           tam=len(tel)
           if tam==8:
               for i in tel:
                    if i.isdigit():
                        cond1+=1
                    else:
                        print("O telefone só pode conter números.")
               if cond1==8:
                     print("Telefone válido. ")
                     valida=True
                     return tel   
               else:
                     print("O Telefone precisa conter apenas números.")
                     continue
           else:
               print("O Telefone precisa conter exatamente 8 números.")
               continue
           return

while v==True:
     print("\n===AGENDA DE CONTATOS===")
     print("1 - Adicionar contato")
     print("2 - Remover contato")
     print("3 - Procurar contato")
     print("4 - Listar todos")
     print("5 - Sair")
     entrada=input(" -> ")
     if entrada=="1":
            nome=input("Digite o nome do usuário - > ") 
            if nome in agenda:
               print("\nUsuário já cadastrado. ")
            else:
               telefone=validatel()
               email=input("entre com o email -> ")
               novocadastro={nome:{telefone:email}}
               agenda.update(novocadastro)
               print(f"\nUsuário {nome} cadastrado com sucesso!")
            #print(agenda)
     elif entrada=="2":
        remove()
     elif entrada=="3":
        procura()
     elif entrada=="4":
        print(agenda)
        pass
     elif entrada=="5":
        print("Execução do programa encerrada pelo usuário.")
        print("===AGENDA DE CONTATOS FECHADA===\n")
        v=False
     else:
          continue


          