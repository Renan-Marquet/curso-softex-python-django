
posicao_atual=0
print(f"Entre com uma das seguintes opções: ")
print(f"Para avançar digite 1 ")
print(f"Para recuar digite 2 ")
print(f"Para saber a posição do robô digite 3")
print(f"Para desligar digite 4")
while True:
    
    commando=int(input("digite seu comando -> "))
    if commando == 1:
        posicao_atual+=1
    elif commando == 2:
        posicao_atual-=1
    elif commando == 3:
        print(f"A posição atual é :   -->{posicao_atual}")
    elif commando == 4:
        print(f"O Robô foi desligado na posição :{posicao_atual}")
        break
    else:
        print("continue")
