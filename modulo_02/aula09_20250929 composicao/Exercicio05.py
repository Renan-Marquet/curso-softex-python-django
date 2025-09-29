""" 5- Casa e Cômodos (Médio) 
 
●  Classes: Comodo e Casa. 
●  Classe Comodo: 
○  Atributo: nome. 
○  Método: __init__(nome). 
●  Classe Casa: 
○  Atributo (Composição): comodos, que deve ser uma lista vazia. 
○  Método: __init__ que inicializa a lista comodos. 
○  Método: adicionar_comodo(nome) que cria uma instância de Comodo e a adiciona 
na lista comodos. 
○  Método: listar_comodos() que itera sobre a lista e imprime o nome de cada cômodo. 
 
"""

class Comodo:
    def __init__(self,nome):
        self.nome=nome
    pass

    def __str__(self):
        pass

class Casa:
    def __init__(self, lista_comodos: list[Comodo]):
        self.comodos=lista_comodos

    def adicionar_comodo(self,comodo):
        self.comodos.append(comodo)

    def listar_comodos(self):
        for item in self.comodos:
            print(item.nome)

comodo_01=Comodo("Sala")
comodo_02=Comodo("Quarto")
comodo_03=Comodo("Cozinha")
comodo_04=Comodo("Banheiro")
comodo_05=Comodo("Varanda")
comodo_06=Comodo("Corredor")

lista = [comodo_01,comodo_02,comodo_03,comodo_04,comodo_05]

casa_01=Casa(lista)
casa_01.listar_comodos()

casa_01.adicionar_comodo(comodo_06)
print()
casa_01.listar_comodos()

casa_01.adicionar_comodo(Comodo("Porão"))
print()
casa_01.listar_comodos()

