from estudante import Estudante

class Escola:
    def __init__(self):
        self.turma:list[Estudante]=[]
        
    def adicionar_estudante(self,estudante:Estudante):
        for estudante_turma in self.turma:
        
            if  estudante_turma.matricula == estudante.matricula:
                print("estudante já cadastrado")
                return         
        self.turma.append(estudante)

    def mostrar_relatorio(self):
        print(self.turma)