"""exercício 11: Tabuada Simples
Peça um número ao usuário
use um while para imprimir a tabuada desse número de 1 a 10.
exemplo: 5 x 1 = 5 , 5 x 2 = 10 , etc..."""

numero=int(input("digite um número interio "))
contador=1
while contador<=10:
    print(f"{contador} x {numero} = ",contador*numero)
    contador+=1
else:
    print("fim")
    