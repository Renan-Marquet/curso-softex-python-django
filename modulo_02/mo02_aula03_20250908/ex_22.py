jogadores={"Renan":10,"Roberto":27,"Tito":15,"Andre":15}

print (jogadores)

#Rodada 1
jogadores["Roberto"]=jogadores["Roberto"]+5
jogadores["Andre"]=jogadores["Andre"]-5

print (jogadores)


while True:
    try:
        
        novojogador=input("Nome do Jogador ")
        if novojogador=="fim":
            break
        novospontos=int(input("Entre com os novos pontos "))
        player=novojogador
     
        if player in jogadores:
            jogadores[player]+=novospontos
        else:
            jogadores[player]=novospontos
    except ValueError:
        print("entrada invalida")


print(jogadores)



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