def duaslistas():
    pass


# 2

def rot_lista(lista:list[any], k:int) -> list[any]:  
    primeira_parte=lista[:k]
    segunda_parte=lista[k:]
    nova_lista=segunda_parte+primeira_parte
    return nova_lista

print(rot_lista([1,2,3,4,5],2))

# 3

listadestrings=["Abacate","pote","cruzes","tamanho","tempo"]

def remove_a(listastr:list[str]) -> list[str]:
    while True:
        pass