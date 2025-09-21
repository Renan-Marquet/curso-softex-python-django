class Carro:
    def __init__(self,modelo: str,motor: int) -> None:
        self.modelo=modelo
        self.motor=motor
        pass
    def exibir_potencia(self) -> None:
        print(f"A potência do modelo {self.modelo} é de {self.motor} HPs")

automovel=input("Digite o Modelo do automóvel: -> ")
motor=int(input(f"Digite o motor do {automovel}-> "))
coche= Carro(automovel,motor)

coche.exibir_potencia()