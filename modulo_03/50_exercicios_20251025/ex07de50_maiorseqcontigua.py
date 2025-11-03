# ex 7 maior sequencia contigua
# criar funcao que receba uma lista de numeros e retorne a soma máxima de 
# qualquer sublista contígua (algorítimo de Kadane - Avançado)
"""
from random import randint

lista=[]

for _ in range (15):
    lista.append(randint(-9,9))

print(lista)"""

lista=[-5, 3, 9, 1, 8, -9, 6,-3, 4, 9, -4, 8, -2, -2, -1,]

#lista=[-5, 3, 9, 1, 8, -9, 6,-3, 4, 9, -4, 8, -2, -2, -1,]

def sublistaMaxima(lista):
    #sublista=[]
    somaMaxima=float('-inf')
    somaAtual=0

    for i in range(len(lista)):
        somaAtual+=lista[i]
        somaMaxima=max(somaMaxima,somaAtual)

        if somaAtual<0:
            somaAtual=0           
            #sublista=[]
                              
        #else:
            #sublista.append(lista[i]) 
    
    #print(sublista)    
    return somaMaxima

lista=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sublistaMaxima(lista))