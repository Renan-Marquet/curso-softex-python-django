class Pessoa:

    def __init__(self,nome:str,idade:int):
        self._nome=nome
        self._idade=idade

        """ def __init__(self, nome:str,idade:int):
        if nome and isinstance(nome, str):
            self._nome=nome
        else:
            self._nome="Não definido."
        
        if idade>0 nd isinstance(idade,int):
            self._idade=idade
        else:
            self._idade="Desconhecida."
        """

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,novo_nome:str):
        if isinstance(novo_nome,str) and novo_nome:   # ou !="":
            self._nome=novo_nome
        else:
            print("Erro! O novo nome deve ser uma string e não deve estar vazio.")

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self,nova_idade:int):
        if isinstance(nova_idade,int) and nova_idade>0:
            self._idade=nova_idade
        else:
            print("Erro a idade deve ser um número maior que 0!")

novapessoa=Pessoa("","")
novapessoa.nome="Renan"
print(novapessoa.nome)
novapessoa.idade=65
print(novapessoa.idade)