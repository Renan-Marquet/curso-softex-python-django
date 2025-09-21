
class Retangulo:

    def __init__(self,base: float,altura: float) -> None:
            self.base=base
            self.altura=altura
            
    def calcular_area(self) -> None:
          area=self.base*self.altura
          print(f"A área do retângulo é: {area}")
          
    def calcular_perimetro(self) -> None:
          perimetro=2*(self.base+self.altura)
          print(f"O perímetro do retângulo é: {perimetro}")

base=float(input("Digite a base do retângulo -> "))
altura=float(input("Digite a altura do retângulo -> "))

retangulo=Retangulo(base,altura)

retangulo.calcular_area()
retangulo.calcular_perimetro()

    


