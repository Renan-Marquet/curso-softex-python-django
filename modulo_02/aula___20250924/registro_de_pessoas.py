class Pessoa:
    def __init__(self,nome:str,idade:int) -> None:
        self.nome=nome
        self.idade=idade

    def apresentar(self):

        print(f"Esta é uma frase que inclui {self.nome} que tem {self.idade} anos.")

class Estudante(Pessoa):
    def __init__(self,nome,idade,curso):
        super().__init__(nome,idade)
        self.curso=curso

    def apresentar(self):
        print(f"Esta é uma frase que inclui {self.nome} que tem {self.idade} anos e cursa {self.curso}")

estudando=Pessoa("Joaquim",25) # objeto estudando classe Pessoa
cursando=Estudante("Anita",20,"matemática") # pbjeto cursando classe Estudante

lista1:list[Pessoa]=[estudando,cursando] # lembrar de tipar lista1 é bom, não é obrigatório

for item in lista1:
    item.apresentar()

lista=[("João",25,"engenharia"),("Andrea",20,"matemática"),("Pedro",24,"belas artes"),("Gilda",23,"geografia")]

for item2 in lista:
    nome,idade,curso=item2 # como item2 é uma tupla, estou desestruturando para poder usar na ordem
    cursando=Estudante(nome,idade,curso) # criando obj cursando com a classe Estudante
    cursando.apresentar()

