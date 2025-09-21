class Filme:
    def __init__(self, nome: str, diretor: str, ano: int) -> None:
        self.nome = nome
        self.diretor = diretor
        self.ano = ano

    def __str__(self) -> str:
        return f"O filme '{self.nome}' é do diretor {self.diretor} do ano de {self.ano}."

filme = Filme("De volta pro futuro", "Robert Zemeckis", 1985)

# não vi vantagem com essa funcao __str__
print(filme)