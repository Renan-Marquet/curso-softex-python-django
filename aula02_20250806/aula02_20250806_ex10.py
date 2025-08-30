"""exercício 10: Contador regressivo
peça um numero inteiro ao usuário
use um while para fazer uma contagem regressiva
a partir desse numero até o 0.
imprima cada número."""

numero=int(input("digite um número inteiro  "))
while numero>0:
    print(f"o número atual é {numero}")
    numero-=1
else:
    print("o número chegou a 0")