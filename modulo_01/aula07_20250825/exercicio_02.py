numero_secreto=7


for i in range(5):
    tentativa=int(input("digite um numero inteiro entre 0 e 10 -> "))
    if tentativa==numero_secreto:
        print(f"voce acertou o numero em {i+1} tentativas. ")
        break
    elif tentativa>numero_secreto:
        print(f"O número que você digitou é maior que o número secreto")
        print(f"Você tem mais {4-i} tentativas")
    elif tentativa<numero_secreto:
        print(f"O número que você digitou é menor que o número secreto")
        print(f"Você tem mais {4-i} tentativas")
    if i==4:
        print(f"Você esgotou seus palpites, o número era {numero_secreto}")

