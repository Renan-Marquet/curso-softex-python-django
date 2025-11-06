
# Exercicio 2 de 50

def rot_lista(lista:list[any], k:int) -> list[any]:  
    primeira_parte=lista[:k]
    segunda_parte=lista[k:]
    nova_lista=segunda_parte+primeira_parte
    return nova_lista

print(rot_lista([1,2,3,4,5],2))
