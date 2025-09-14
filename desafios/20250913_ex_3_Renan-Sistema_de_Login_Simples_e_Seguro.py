
cadastro={}
v=True


def cadastra() -> dict:
    cadastro={}
    nome=input("Digit o nome do usuário - > ")
    senha=input("Digite a senha do usuário -> ")
    cadastro=cadastro{"nome":senha}
    print(cadastro)


while v==True:
     print("\n===SISTEMA DE LOGIN===")
     print("1 - Cadastrar usuário")
     print("2 - Fazer login")
     print("3 - Sair")
    
     entrada=input(" -> ")

     if entrada=="1":
        cadastra()
     elif entrada=="2":
        login()
     elif entrada=="3":
        v=False
     else:
          continue
          