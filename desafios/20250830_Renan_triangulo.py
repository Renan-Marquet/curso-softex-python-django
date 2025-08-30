""" Validação de triângulo"""
"""Este programa verifica o triangulo pelos lados"""

lado1="0"
lado2="0"
lado3="0"
reto=False
obtuso=False
valido=True

print("\n Esse programa verifica se os três valores de entrada são válidos para lados de um triângulo.")

invalido1=True
lado1=input("-> Entre com o valor do primeiro lado: - > ")
while invalido1: 
    if lado1.isnumeric() and int(lado1)>0:
        print(" * Lado UM válido.")
        invalido1=False
    else:
        lado1=input("Lado inválido digite novamente: - > ")
invalido2=True
lado2=input("-> Entre com o valor do segundo lado: - > ")
while invalido2: 
    if lado2.isnumeric() and int(lado2)>0:
        print(" * Lado DOIS válido.")
        invalido2=False
    else:
        lado2=input("Lado inválido digite novamente: - > ")
invalido3=True
lado3=input("-> Entre com o valor do terceiro lado: - > ")
while invalido3:
    if lado3.isnumeric() and int(lado3)>0:
        print(" * Lado TRÊS válido.")
        invalido3=False
    else:
        lado3=input("Lado inválido digite novamente: - > ")
lado1=int(lado1)
lado2=int(lado2)
lado3=int(lado3)
print(f"\n Os lados são: primeiro -> {lado1} , segundo -> {lado2} , terceiro -> {lado3} .")

if lado1<(lado2+lado3) and lado2<(lado3+lado1) and lado3<(lado2+lado1):
    print("-- Esse é um triândulo válido verificado pela soma.")
if lado1>abs(lado2-lado3) and lado2>abs(lado3-lado1) and lado3>abs(lado1-lado2):
    print("-- Esse é um triângulo válido verificado pela diferença.")
else:
    valido=False
    print("** Esse não é um triângulo válido.")
    while valido==False:
        break
    
if valido:
    if lado1 == lado2 == lado3:
        print("* Esse é um triângulo equilátero.")
    if lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado3 == lado1 != lado2:
        print("* Esse é um triângulo isósceles.")
    if lado1 != lado2 != lado3:
        print("* Esse é um triângulo escaleno.")
        

quad1=lado1**2
quad2=lado2**2
quad3=lado3**2

while valido:
    if quad1 + quad2 == quad3 or quad2 + quad3 == quad1 or quad3 + quad1 == quad2:
        print("* Esse é um triângulo retângulo.")
        reto=True
        break
    if (quad1 + quad2) < quad3 or (quad2 + quad3) < quad1 or (quad3 + quad1) < quad2:
        print("* Esse é um triângulo obtusângulo.")
        obtuso=True
        break
    if (( quad1 + quad2) > quad3 or (quad2 + quad3) > quad1 or (quad3 + quad1) > quad2) # and not reto and not obtuso:
        print("* Esse é um triângulo acutângulo.")
        break
