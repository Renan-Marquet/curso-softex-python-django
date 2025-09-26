class FormaGeometrica:
    def __init__(self,cor) -> None:
        self.cor=cor

    def calcular_area(self) -> None:
        a=0

    def __str__(self):
        return f"{self.cor}"
        
class Retangulo(FormaGeometrica):
    def __init__(self, cor, largura :float, altura :float):
        super().__init__(cor)
        self.largura=largura
        self.altura=altura
    def calcular_area(self):
        arear=self.largura*self.altura
        print(f"A área do retângulo de {self.largura} por {self.altura} é de {arear}")
        
class Quadrado(Retangulo):
    def __init__(self, cor, largura, altura, lado:float):
        super().__init__(cor, largura, altura)
        self.largura=lado
        self.altura=lado


cor="branco"
largura=4.0
altura=3.0
lado=5.0
ob=cor
retangulo=Retangulo(ob,largura,altura)
quadrado=Quadrado(ob,lado,lado,lado)
retquad=(retangulo,quadrado)

#def calcular_soma_areas():