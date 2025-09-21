
class Contabancaria:
    def __init__ (self, titular: str, saldo: float) -> None:
        self.titular= titular
        self.saldo= saldo

    def depositar(self) -> float:
        valor1=float(self.saldo)
        deposito=float(input("Digite o valor depositado "))
        valor1=valor1+deposito
        self.saldo=valor1
        print(f"Saldo atual: {valor1}")


    def sacar(self) -> float:      
        valor2=float(self.saldo)
        saque=float(input("Digite o valor a sacar "))
        if saque>valor2:
            print("Saldo insuficiente.")
            #return
        else:
            saldo=valor2-saque
            self.saldo=saldo
            print("Saque realizado com sucesso")
            print(f"Saldo atual: {saldo}")


    def situacao(self) -> None:
        print(f"O Sr.{self.titular} tem atualmente {self.saldo} de saldo.")
              

titular1=Contabancaria("Antonio",10)

titular1.depositar()

titular1.sacar()

titular1.situacao()






  






        




