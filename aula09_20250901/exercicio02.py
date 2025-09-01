lista1 = ["vermelho","azul","verde","amarelo"]
lista2 = ["verde","roxo","azul","preto"]
"""resultado esperado: ["azul","verde"]"""
listafinal=[]

for item in lista1:
    for item2 in lista2:
        if item == item2:
            #print(item)
            listafinal.append(item)

            """ for item in lista1:
                    if item in lista2 and item not im elementos_comuns
                        elementos_comuns.apend(item)"""
  

print(listafinal)