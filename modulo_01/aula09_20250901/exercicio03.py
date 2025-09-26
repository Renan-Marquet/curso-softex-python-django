numeros = [1,2,3,4,5,6,7,8,9,10]
primos=[]

for numero in numeros:
    eh_primo = True
    if numero < 2:
        eh_primo = False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                eh_primo = False
                break

    if eh_primo:
        primos.append(numero)

print(f"lista original: {numeros}")
print(f"números primos na lista: {primos}")




"""numeros2 = numeros
# listar numeros primos
quantidade=len(numeros)
lista_primos=[]
lista_nao_primos=[]


for item in numeros:
    for item2 in numeros2:
        if item%item2!=0:
            #print(item)
            lista_primos.append(item)
"teste se numero é primo"
'''for i in range(quantidade):
    for j in range(quantidade):
        if numeros[quantidade-i]%numeros[quantidade-j]==0:
            lista_nao_primos.append(numeros[j])# o numero não é primo
            pass
            
        else : 
            lista_primos.apend(numeros[j])'''

print(lista_primos)

#for item in numeros:
    #primos

    #if """ 