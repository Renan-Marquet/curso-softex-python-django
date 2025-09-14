# exercicio desafio 3
# Sistema de Login Simples e Seguro

cadastro={"teste1":"ABC123..","teste2":"cde123.."}
v=True

def login() -> bool:
    
    lnome=input("Digite o seu nome -> ")
    #print(lnome)
    
    if lnome in cadastro:
        #print("Usuário cadastrado.")
        senha=input("Entre sua senha -> ")
        if cadastro[lnome]==senha:
            print(f"Login bem-sucedido! Bem-vindo, {lnome}.") 
        else:
            print("Senha inválida.")       
    else:
        print("Usuário não cadastrado ou incorreto.")
    return



def validasenha() -> str:
    valida=False
    while valida==False:
           senha=input("Digite uma senha com 8 caracteres-> ")
           tam=len(senha)
           if tam==8:
               cond1=False
               cond2=False
               cond3=False
               for i in senha:
                     if i.isdigit():
                        cond1=True
                     if i.isalpha():
                        cond2=True
                     if not i.isdigit() and not i.isalpha():
                        cond3=True
               if cond1 and cond2 and cond3:
                     #print("Senha válida. ")
                     valida=True
                     #return senha   
               else:
                     print("A senha precisa conter no mínimo uma letra, um número e um caracter.")
                     continue
           else:
               print("A senha precisa conter exatamente 6 caracteres.")
               continue
           return senha



while v==True:
     print("\n===SISTEMA DE LOGIN===")
     print("1 - Cadastrar usuário")
     print("2 - Fazer login")
     print("3 - Sair")
    
     entrada=input(" -> ")

     if entrada=="1":
       
            nome=input("Digite o nome do usuário - > ") 
            if nome in cadastro:
               print("\nUsuário já cadastrado. ")
            else:
               
               novocadastro={nome:validasenha()}
            
               cadastro.update(novocadastro)
               print(f"\nUsuário {nome} cadastrado como sucesso!")
            #print(cadastro)
            
           
     elif entrada=="2":
        login()
     elif entrada=="3":
        print("Execução do programa encerrada pelo usuário.")
        print("===SISTEMA DE LOGIN DESLIGADO===\n")
        v=False
     else:
          continue


          