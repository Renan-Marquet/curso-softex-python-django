class Pessoa:
    def __init__(self,nome:str,idade:int):
        self._nome=nome
        self.idade=idade

    def __str__(self):
       
       return f"Essa é uma string do def __str__ ."
         
    @property
    def nome(self):
       print (f"{self._nome} conseguido com o GETTER")
       return self._nome
    

