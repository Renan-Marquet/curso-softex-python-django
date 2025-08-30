"""exercício 12: acumulador de soma
peça ao usuárionpara digitar 5 números
use um while com um contador para somar todos os 
números digitados e imprimir o resultado final."""

contador=1
soma=0
while contador<=5:
    numero=int(input("digite um número inteiro "))
    soma=soma+numero
    contador+=1
else:
    print("a soma é ",soma)
    