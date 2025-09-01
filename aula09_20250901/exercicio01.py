numeros = [1,5,2,8,5,3,5]
numero_procurado = 5
cont=0

for numero in numeros:
    if numero == numero_procurado:
        cont += 1

cont1 = numeros.count(numero_procurado)

print(f"O número {numero_procurado} aparece {cont} vezes na lista")
print(f"O número {numero_procurado} aparece {cont1} vezes na lista.")
