
# exercicio 3 de 50

listadestrings=["Abacate","pote","cruzes","tamanho","tempo"]
print(len(listadestrings))
print(listadestrings)
#listadestrings.pop(0)
#print(listadestrings)



def remove_a(listastr:list[str]) -> list[str]:
#listastr=listadestrings

    a=True
    while a == True:
        novalista=listastr.copy()
        novalista2=[]    
        for indice in range(0,len(listastr)):
            print(indice)
            print(listastr[indice])
            palavra=listastr[indice]
            if "a" in palavra:
                novalista.remove(palavra)
                print(novalista)
                #print(novalista2)
            else:
                print(f"{listastr[indice]} não tem a letra a")
        a=False
    return (novalista)
            
#print()
            
            #print(indice)            
            #palavra=listastr[indice]
            #print(palavra)
            #if 'a' in palavra:
             #   listastr.pop(indice)
            #else:
                #    continue
            #continue
        #return listastr  """    
    
print(remove_a(listadestrings))
    
