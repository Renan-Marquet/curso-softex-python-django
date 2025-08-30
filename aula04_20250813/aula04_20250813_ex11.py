"""exercício 11 : Senha Forte
8 caracteres
1 letra maiúscula
1 letra minúscula
1 número
1 caracter especial"""

print("digite uma senha com no mínimo 8 caracteres e máximo de 16 contendo ")
print("no mínimo uma letra maiúscula, uma minúscula, um número e um caracter especial")

valido=False
maiuscula=False
minuscula=False
caracter=False
numero=False
while valido != True:
    senha1=input("digite nova senha: - > ")
    if len(senha1) > 7 and len(senha1) <= 16: 
        #print("quantidade de caracteres correta")
        for i in range(len(senha1)):
            letra = senha1[i]
            #print(letra)
            if letra.isalpha():
                #print("tem uma letra")
                if letra.isupper() :
                    maiuscula=True
                    #print(f"a letra {letra} é maiuscula")
                elif letra.islower() :
                    minuscula=True
                    #print(f"a letra {letra} é minuscula")
        
                else:
                    print("em ação")
            elif letra.isdigit():
                numero=True
                #print(f"tem o numero : {letra}")
            elif not letra.isalnum() and letra!=" ":
                caracter=True 
                #print(f"tem o caracter {letra}")
        else:
            if maiuscula==True and minuscula==True and numero==True and caracter==True:
                print("senha valida")
                senha2=input("digite a senha novamente : -> ") 
                valido=True
                if senha1 == senha2:
                    print("senha cadastrada!")
                while senha1 != senha2:
                    senha2=input("senha não confere digite a senha novamente: -> ")
                    if senha1 == senha2:
                        print("senha cadastrada")      
            else:
                valido=False
                print("senha invalida")

    else:
        print("Você não digitou uma senha válida")
        
            
    