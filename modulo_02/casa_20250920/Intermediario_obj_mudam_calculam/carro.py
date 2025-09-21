class Carro:
    def __init__(self, modelo: str, nivel_combustivel: float, consumo: float) -> None :
        self.modelo=modelo
        self.nivel_combustivel=nivel_combustivel
        self.consumo=consumo

    def abastecer(self) -> None:
        litros=float(input("Quanto de combustível vc quer abastecer? -> "))
        print(f"O nível de combustível atual é {self.nivel_combustivel:.2f} litros. ")
        self.nivel_combustivel += litros
        print(f"Você abasteceu {litros} e o nível de combustível agora é {self.nivel_combustivel:.2f} litros. ")

    def dirigir(self) -> None:
        
        
        if self.nivel_combustivel <= 0.0:
            print("Tanque vazio.")
            return
        distancia=float(input("Qual a distância em km a ser percorrida? "))
        necessario=distancia/self.consumo

        if necessario<= self.nivel_combustivel:
            self.nivel_combustivel-=necessario
            print(f"É possível dirigir por {distancia:.2f} km e restará {self.nivel_combustivel:.2f} litros.")
        else:
            print("Combustível insuficiente para fazer essa viagem. ")

modelo=str(input("Carro Modelo: -> "))
combustivel=float(input("Combustível inicial em litros: -> "))
consumo=float(input("Quantos kilômetros faz por litro? -> "))

coche=Carro(modelo,combustivel,consumo)

coche.abastecer()
coche.dirigir()
