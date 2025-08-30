entrada=input("digite qualquer coisa: -> ")
if entrada.isalpha():
    print("você digitou só letras")
elif entrada.isdigit():
    print("você digitou só números")
elif entrada.isalnum():
    print("você digitou números e letras")
else:
    print("você digitou algo diferente de números e letras")