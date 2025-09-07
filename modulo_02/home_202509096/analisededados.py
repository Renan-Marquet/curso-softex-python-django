# Análise de Dados de Acessos
entrada=[]
#status=""
teste=True
#while True:
usuario=input("Nome do Usuário")
#status=input("digite 1 para sucesso ou 2 para falha")
#print(status)
while True:
    status=input("digite 1 para sucesso ou 2 para falha")
    if status != "1" or status != "2":
        status=input ("entrada invalida, digite somente 1 ou 2 tente novamente")
    else:
        False
tempo=input("entre com a duração")
#    except:

entrada.append(usuario)
entrada.append(status)
entrada.append(tempo)

print(entrada)
nova=tuple(entrada)
print(nova)