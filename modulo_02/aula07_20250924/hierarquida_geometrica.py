class FormaGeometrica:
    def __init__(self,cor) -> None:
        self.cor=cor

    def calcular_area(self) -> None:
        pass

    def __str__(self):
        return f"A cor é {self.cor}"
        
class Retangulo(FormaGeometrica):
    def __init__(self, cor, largura :float, altura :float):
        super().__init__(cor)
        self.largura=largura
        self.altura=altura
   
    def calcular_area(self):
        arear=self.largura*self.altura
        # print(f"A área do retângulo de {self.largura} por {self.altura} é de {arear}")
        return arear
    
class Quadrado(Retangulo):
    def __init__(self, cor, largura, altura, lado:float):
        super().__init__(cor, largura, altura)
        self.lado=lado
    def calcular_area(self):
        areaq=self.lado**2
        #print(f"A área do quadrado de {self.ladoa} de lado é de {areaq}")
        return areaq


cor="branco"
largura=4.0
altura=3.0
lado=5.0
ob=cor
retangulo=Retangulo(ob,largura,altura)
quadrado=Quadrado(ob,lado,lado,lado)
retquad=(retangulo,quadrado)

print(retangulo)
#def calcular_soma_areas():
respostaderet=retangulo.calcular_area()
print(respostaderet)

print(f"A área do retângulo de cor {retangulo.cor} com {retangulo.largura} por {retangulo.altura} é de {retangulo.calcular_area()}")
