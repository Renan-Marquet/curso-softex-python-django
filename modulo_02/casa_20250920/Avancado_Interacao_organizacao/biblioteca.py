
acervo=[]

class Livro:
    def __init__(self,titulo:str,autor:str)-> None:
        self.titulo=titulo
        self.autor=autor
       
class Biblioteca:
    def __init__(self,acervo:list) -> None:
        self.acervo=acervo

    def adicionar_livro(self, livro: list) -> None:
        self.livro=livro
        while True:
            self.acervo.append(livro)
            self.livro=(titulo,autor)
            entrada=input("Deseja adicionar um livro? Digite S para confirmar -> ")
            entrada.lower()
            if entrada == "s" or entrada == "S":
                titulo=input("Entre como o nome do Livro: -> ")
                autor=input(f"Entre com o autor de {self.titulo}: -> ")
                self.livro=Livro(titulo,autor)
                
                print(self.livro)
                self.acervo.append(self.livro)
            else:
                break

    def listar_livros(self):
        self.livro=livro
        for livro in self.acervo:
            print(livro.self.titulo,livro.self.autor)

Biblioteca.adicionar_livro()
Biblioteca.listar_livros()


