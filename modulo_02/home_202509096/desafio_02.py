# Análise de Acessos de Usuários

acessos=[('Ana','Login'),('Pedro','Dashboard'),('Ana','Login'),('Ana','Perfil'),('Pedro','Configurações')]
acessoslist=list(acessos)
acessosconj=set(acessoslist)
novoacessoslist=list(acessosconj)
#acessostupla=tuple(novoacessoslist)
#print(acessoslist)
#print(acessosconj)
usuarios_unicos=set()
recursos_unicos=set()
lista_acessos_sem_repeticao=[]
for usuario,_ in acessos:
    usuarios_unicos.add(usuario)
for _,recursos in acessos:
    recursos_unicos.add(recursos)

print("\nLista de tuplas original:", acessos)
print("Conjunto dos usuários únicos:", usuarios_unicos)
print("Conjunto dos recursos únicos:", recursos_unicos)
print("Nova lista de tuplas sem repetição:", novoacessoslist)
