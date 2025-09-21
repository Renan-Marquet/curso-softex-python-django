
class Contabancaria:
    def __init__ (self, titular: str, saldo: float) -> None:
        self.titular= titular
        self.saldo= saldo


    def depositar(self) -> float:
        deposito=input("digite o valor depositado")
        self.saldo=self.saldo+deposito
        print("Saldo atual: {self.saldo}")


    def sacar(self,valor: float) -> float:
        saque=input("digite o valor a sacar")
        if saque<self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo=self.saldo-saque
            print("Saldo realizado com sucesso")
            print("Saldo atual: {self.saldo}")


    def situacao(self) -> None:
        print(f"{self.titular} {self.saldo}")
              

titular1=Contabancaria("Antonio",10)

titular1.depositar()

titular1.sacar()

titular1.situacao()






  






        




