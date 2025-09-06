# Tupla coordenadas

coordenadas=(10,20)
tamanho=len(coordenadas)
for i in range(tamanho):
    print(coordenadas[i])

# imutabilidade da tupla, exercicio de erro

dias_da_semana=('segunda','terça','quarta')

"""while True:
    try:
        dias_da_semana.add('quinta')
    except ValueError:
        print("código inválido.")"""

# o uso do .count

numeros=(1,2,3,2,4,2)
vezes_do_2=numeros.count(2)
print(vezes_do_2)

# encontrando um elemento

nomes=('Carlos','Ana','Pedro')
indice=nomes.index('Ana')
print(indice)

# conjuntos

produtos={'pão','leite','pão','queijo'}
print(produtos)

# adicionar e remover de um conjunto

linguas={'português','inglês'}
print(linguas)
linguas.add('espanhol')
print(linguas)
linguas.remove('português')
print(linguas)

# pertinencia

frutas={'maçã','banana','morango'}
if 'banana' in frutas:
    print("banana está em frutas")