#Exercicio 3: Verificador de Divisibilidade

numero=input("Digite um número inteiro :   ")
numero=int(numero)
if numero>0:
    novonum=numero%5
    if novonum==0:
        print("O número",numero, "É divisível por 5.")
    else:
        print("O número",numero, "NÃO é divisível por 5.")
else:
    print("O número" ,numero, "não é um número positivo.")
