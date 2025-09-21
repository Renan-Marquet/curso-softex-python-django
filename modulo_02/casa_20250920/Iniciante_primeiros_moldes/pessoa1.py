
class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome 
        self.idade = idade 
        
    def apresentar(self) -> None:
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
    
