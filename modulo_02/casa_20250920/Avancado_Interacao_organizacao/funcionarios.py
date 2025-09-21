class Funcionario:

    def __init__(self,nome:str, salario:float) -> None:
        self.nome=nome
        self.salario=salario
        self.bonus=1.10

    def aplicar_bonus(self) -> None:
        aplicar=self.salario*self.bonus
        print(f"O salário de {self.nome} é de {self.salario},")
        print(f"com o bonus de 10% fica: -> {aplicar:.2f}")

funcionario=Funcionario("Andre",5000)
funcionario.aplicar_bonus()
funcionario=Funcionario("Maria",7000)
funcionario.aplicar_bonus()

