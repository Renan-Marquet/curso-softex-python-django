from math import pi
# forma altreantiv = import math -/. use math.py

class Circulo:
    def __init__(self,raio):
        self._raio=raio

    @property
    def raio(self):
        return self._raio
    
    @raio.setter   
    def raio(self, novo_raio: float):
        # isisntance verifica se o primeiro parametro é do tipo do segundo
        if isinstance(novo_raio, (float,int)) and novo_raio>0:
            self._raio = novo_raio
        else:
            print("Erro! O raio deve ser maior que 0")

    def calcular_area(self):
        area=pi*((self.raio)**2)
        print(f"A área do círculo de raio {self.raio} é de: -> {area:.4f}")
        
circulo=Circulo(0)
circulo.raio = 6
circulo.calcular_area()
