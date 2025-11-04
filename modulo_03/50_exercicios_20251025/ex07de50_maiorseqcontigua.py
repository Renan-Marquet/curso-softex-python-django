# ex 7 maior sequencia contigua
# criar funcao que receba uma lista de numeros e retorne a soma máxima de 
# qualquer sublista contígua (algorítimo de Kadane - Avançado)


# bloco para criar uma lista
"""
from random import randint

lista=[]

for _ in range (15):
    lista.append(randint(-9,9))

print(lista)
"""
# lista criada para teste 

# lista=[-5, 3, 9, 1, 8, -9, 6,-3, 4, 9, -4, 8, -2, -2, -1,]

# algorítimo de Kadane para conseguir o valor máximo contíguo"""

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

# lista exemplo do Algoritimo de Kadane que resulta em 6

lista=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("\n")
print("*"*100)
print(f"Valor o obtido da lista:\n {lista} \nPelo algorítimo de Kadane: \n {sublistaMaxima(lista)}")

# para obter a sublista que forneceu o resultado

soma=float('-inf')
listanova=[]
for j in range(len(lista)):
    listat=[]
    if j>0:        
        for i in range(len(lista)):         
            listat.append(lista[i])                
            if soma< sum(listat):
                soma=sum(listat)  
                if soma==sum(listat):
                    listanova=listat.copy()                                
            if i==j:
                #print(listat)
                #print(sum(listat))
                continue
            if i>j:
                listat.pop(0)
                #print(listat)
                #print(sum(listat)) 

print(f"Este é o resultado da soma de sublista por sublista que confirma o algorítimo de Kadane: \n {soma}")  
print(f"Esta é a sublista que forneceu o resultado de Kadane: \n {listanova} ")
print("*"*100)
print("\n")
