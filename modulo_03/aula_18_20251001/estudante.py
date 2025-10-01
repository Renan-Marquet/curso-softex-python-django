from pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula:str):
        super().__init__(nome, idade)
        self.matricula=matricula
        self._notas:dict[str,list[float]]={}
   
    def adicionar_nota(self,materia:str,nota:float):   
        aula=self._notas.get(materia)
        print(f"aula atual: {aula}")
        if aula:
            aula.append(nota)
        else:
            self._notas[materia]=[nota]

        print(f"dicionario de materias: {self._notas}")

        
       
nova_nota=Estudante("Alberto",25,"453959-7")
nova_nota.adicionar_nota("matemática",10.0)
nova_nota.adicionar_nota("matemática",9.5)







#andre_math=Materia("historia",6.0)
#andre_math.adicionar_nota_historia()
    
