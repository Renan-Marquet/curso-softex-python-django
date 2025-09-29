class Motor:
    def __init__(self):
        pass
    def ligar_motor(self):
        print("O motor ligou.")
    def desligar_motor(self):
        print("O motor desligou")



class Carro:
    def __init__ (self):
        self.motor=Motor()

    def ligar_carro(self):
        self.motor.ligar_motor()
        print("O carro ligou o Motor")


carroa=Carro()
carroa.ligar_carro()