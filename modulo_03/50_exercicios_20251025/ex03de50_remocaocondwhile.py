
# exercicio 3 de 50 remove()

listadestrings=["Abacate","Antítese","pote","cruzes","tamanho","tempo"]
#print(len(listadestrings))
print(listadestrings)

def remove_a(listastr:list[str]) -> tuple:
    a=True
    while a == True:
        novalista=listastr.copy()
        novalista2=[]    
        for indice in range(0,len(listastr)):
            #print(indice)
            #print(listastr[indice])
            palavra=listastr[indice]
            if "a" in palavra.lower():
                novalista2.append(listastr[indice])
                novalista.remove(palavra)
                #print(novalista)
                #print(novalista2)
            else:
                #print(f"{listastr[indice]} não tem a letra a")
                continue
            
            #print(novalista2)
        a=False
    return (novalista),(novalista2)

resultado=list(remove_a(listadestrings))
            

print(f"Palavras sem 'a' {resultado[0]}.")
print(f"Palavras com 'a' {resultado[1]}.")
    
