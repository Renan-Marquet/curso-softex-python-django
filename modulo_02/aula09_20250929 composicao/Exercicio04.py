"""4. Dispositivos de um Computador (Fácil/Médio) 
 
●  Classes: Teclado, Mouse, Monitor e Computador. 
●  Classes Teclado, Mouse, Monitor: 
○  Método: __init__ (sem atributos). 
○  Método: ligar() que imprime uma mensagem indicando que o dispositivo está ligado 
(ex: "O teclado foi ativado."). 
●  Classe Computador: 
○  Atributos (Composição): teclado, mouse e monitor, que devem ser instâncias das 
classes correspondentes. 
○  Método: __init__ que inicializa os três atributos. 
○  Método: ligar_computador() que chama o método ligar() de cada um dos seus 
dispositivos. 
 """

class Teclado:
    def __init__(self):
        pass
    def ligar(self):
        print("O teclado está ligado.")
class Mouse:
    def __init__(self):
        pass
    def ligar(self):
        print("O mouse está ligado.")
class Monitor:
    def __init__(self):
        pass
    def ligar(self):
        print("O monitor está ligado.")
class Computador:
    def __init__(self):
        self.teclado=Teclado()
        self.mouse=Mouse()
        self.monitor=Monitor()
    def ligar_computador(self):
        self.teclado.ligar()
        self.mouse.ligar()
        self.monitor.ligar()
        print("O computador foi inicalizado.")

meu_computador=Computador()
meu_computador.ligar_computador()