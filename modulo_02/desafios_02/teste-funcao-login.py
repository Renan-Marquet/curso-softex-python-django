
cadastro={"teste1":"ABC123..","teste2":"cde123.."}
v=True


def login() -> bool:
    
    lnome=input("Digite o seu nome -> ")
    print(lnome)
    
    if lnome in cadastro:
        print("Usuário cadastrado.")
        senha=input("Entre sua senha -> ")
        if cadastro[lnome]==senha:
            print("Login com sucesso") 
        else:
            print("Senha inválida.")       
    else:
        print("Usuário não cadastrado")
    return


login()
