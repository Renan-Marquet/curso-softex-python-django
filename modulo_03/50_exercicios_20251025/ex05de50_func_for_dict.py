# ex 5 de 50 funcao fordict(para contagem), list print

from random import randint

lista=[]
for _ in range(10):
    elemento1=randint(1,7)
    lista.append(elemento1)
print(f"lista original {lista}")



def encontrar_duplicatas(listx:list[any]) -> None:
    
    lista1=listx.copy()
    lista2=listx.copy()
    listanova=[]

    vezes=0
    dicionario1={}
    dicionario2={}

    for indice1 in range(len(lista1)):
        for indice2 in range(len(lista2)):
            if lista1[indice1] == lista2[indice2]:
                vezes+=1
                chave=lista1[indice1]          
                if vezes>=2  :
                    dicionario1.update({chave:vezes})
                    #lista3.append(chave) 
                    if vezes==2:
                        # usando del[chave] remove pela ['chave'] e não devolve valor
                        #del dicionario2[chave]
                        # usando .pop(chave) remove pela ('chave') e devolve valor se pedir 
                        #dicionario2.pop(chave)
                        # usando .popitem() remove último par adicionado "chave,valor"
                        # retorna uma tupla (chave,valor), mas não recebe argumentos ->() é opcional
                        dicionario2.popitem() # ou dicionario2.popitem

                else:
                    dicionario2.update({chave:vezes})             
                    #continue  
            else:            
                continue   
        vezes=0

    listanova=list(dicionario1.items())   
    print(f"Lista dos numeros que se repetem e suas quantidades:\n {listanova}")

    for item in listanova:
        print(f"O número {item[0]} se repete {item[1]} vêzes.")

    listanova2=list(dicionario2.keys())
    print(f"Lista dos numeros que se não repetem:\n {listanova2}")

    return

encontrar_duplicatas(lista)
