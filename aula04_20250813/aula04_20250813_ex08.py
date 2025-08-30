senha=False
while senha!=True:

    entrada=input("digite uma senha com letras e números sem caracteres especiais: -> ")
    if entrada.isalpha():
        print("você digitou só letras, tente novamente")
    elif entrada.isdigit():
        print("você digitou só números, tente novamente")
    elif entrada.isalnum():
        print("você digitou números e letras senha válida")
        senha=True
    else:
        print("você digitou algo diferente de números e letras tente novamente")