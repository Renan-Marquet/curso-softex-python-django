from saldo import verificar_saldo, sacar_valor, depositar_valor
import boletos
from clientes import alterar_senha

def menu_operacoes(usuario:dict) -> None:
    """Exibe o menu de operacoes e efetua a escolha do usuaário autenticado"""
    while True:
        print(f"Vem-vindo, {usuario["noe"]} !")
        print("Escolha uma opção")
        print("1- Ver saldo")
        print("2- Salvar valor") 
        print("3- Depositar valor") 
        print("4- Pagar boleto") 
        print("5- Alterar Senha")
        print("6- Sair")

        opcao=input(opcao)

        if opcao =='1':
            verificar_saldo(usuario)
        if opcao =='2':
            sacar_valor(usuario)
        if opcao =='3':
            depositar_valor(usuario)
        if opcao =='4':
            boletos.pagar_boleto(usuario)
        if opcao =='5':
            alterar_senha(usuario)
        if opcao =='6':
         print ("Atendimento Finalizado")
         break
         