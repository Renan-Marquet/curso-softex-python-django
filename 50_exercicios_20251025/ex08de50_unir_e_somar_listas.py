# unir e somar listas


lista_A=['A','B','C','d','e','f']#,'g','h','i']
lista_N=[1,2,3,4,5,6]

def juntar_listas(lista1:list,lista2:list) -> list:
    lista3=[]
    if len(lista1)>=len(lista2):
        maiorlista=lista1
    else:
        maiorlista=lista2

    if len(lista1)==len(lista2):
        print("listas de tamanhos iguais")

    try:
        for i in range(len(maiorlista)):
            lista3.append(lista1[i])
            lista3.append(lista2[i])
    except IndexError:
        if maiorlista==lista1:
            print("a primeira lista é maior que a segunda")
            for j in range((i+1),len(maiorlista)):
                lista3.append(maiorlista[j])
        if maiorlista==lista2:
            print("a segunda lista é maior que a primeira")
            for j in range((i),len(maiorlista)):
                lista3.append(maiorlista[j])
        #print("listas de tamanhos diferentes")
     
    return lista3

print(f"união das listas intercaladas {juntar_listas(lista_A,lista_N)}")