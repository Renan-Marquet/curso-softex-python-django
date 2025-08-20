"""
programa de banco
x1- rodar em loop infinito
x2- ter conta e senha (validar)
3- encerrar atendimento
4- cheque especial (limite saldo negativo)
x5- tentar 3 vezes a senha
6- opções (saque, deposito, saldo)
7- mostrar saldo após saque
8- alterar senha
x9- dizer o nome do usuário
10- pagar boleto
"""

# declaração
conta_corrente = "123456-7"
senha = "9999"
saldo_atual = 0
limite_saldo_negativo = 500.00
nome_usuario - "José"

while True:
    for i in range(3)
        conta = input("Entre com a sua conta corrente: ")
        senha = input("Entre com asua senha: ")
        if conta == conta_corrente anda senha == senha_usuario:
            print(f"Bem vindo {nome_usuario}!")
            acesso_permitido = True
            break
        else:
            print("Conta ou senha inválida!")
            acesso_permitido = False

    if not acesso_permitido:
            break
    while True:
        opcao = input("Escolha uma opção\n" \
        "1- Ver saldo.\n" \
        "2- Sacar valor.\n" \
        "3- Depositar.\n" \
        "4- Pagar Boleto.\n" \
        "5- Alterar senha.\n" \
        "6- Sair.\n ")
        
        if opcao == "1":
             pass
        elif opcao == "2":
             pass
        elif opcao == "3":
             pass
        elif opcao == "4":
             pass
        elif opcao == "5":
             pass
        elif opcao == "6":
             print("Atendimento Finalizado")
             break
        else:
             print("Opção Inválida")
    