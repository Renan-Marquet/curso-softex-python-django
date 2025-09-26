
"""
clientes_por_cidade = {}

for cliente in clientes:
    cidade = cliente["cidade"]
    if cidade in clientes_por_cidade:
        clientes_por_cidade[cidade] += 1
    else:
        clientes_por_cidade[cidade] = 1

print("\n--- Clientes por Cidade ---")
print(clientes_por_cidade)"""

lista={}
while True:
    try:
        
        contato=input("Nome do contato ")
        if contato=="fim":
            break
        telefone=int(input("Entre com o telefone "))
        if contato in lista:
            print(f"Atualizando o telefone de {contato}")
            lista[contato]=telefone
        else:
            print(f"Acrescentando {contato} e seu telefone {telefone}.")
            lista[contato]=telefone
    except ValueError:
        print("entrada invalida")

print(lista)

while True:
        
    try:
        contato=input("Digite o nome de quem vc quer o telefone ")
        if contato == "sair":
            break
        if contato in lista:
            print(f"O telefone de {contato} é {lista[contato]}")
        else:
            print(f" {contato}, não consta da lista ")
    except ValueError:
        print ("entrada invalida")
        continue