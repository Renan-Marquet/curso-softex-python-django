# fatiamento circular

lista_A=['A0','B1','C2','D3','E4','F5','G6','H7','I8']
lista_B=['E0','F1','G2']
lista_C=[]

print("lista_A" ,lista_A)
print("lista_B" ,lista_B)
print("lista_C" ,lista_C)

def fatiamento_circular(lista:list,index1:int,index2:int)->list:
    listanova=[]
    if len(lista) == 0:
        print("esta lista não possue elementos para serem fatiados")
        #listanova=[]
        return listanova
    if index1 == index2:
        print("os indíces são iguais, não haverá fatiamento")
        #listanova=[]
        return listanova          
    if index1 >= len(lista) or index2 >= len(lista):
        print(f"{index1} {index2} {len(lista)}")
        print("a lista não possue pelo menos um destes índices")
        #listanova=[]
        return listanova
    if index1 and index2 < len(lista):
        if index1 <= index2:
            listanova=lista[index1:index2]
            #print(listanova)
        else:
            listanova=lista[index1:]+lista[:index2]
            #print(listanova)
        
        print("essa é a nova lista resultante do fatiamento")
        return listanova

print(fatiamento_circular(lista_A,4,7))


