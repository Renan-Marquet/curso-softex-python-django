

class Livro:
    def __init__(self,titulo:str,autor:str)-> None:
        self.titulo=titulo
        self.autor=autor
       
class Biblioteca:
    def __init__(self) -> None:
        self.acervo=[]

    def adicionar_livro(self) -> None:
       
        while True:
            
            entrada=input("Deseja adicionar um livro? Digite S para confirmar -> ")
            entrada.lower()
            if entrada == "s" or entrada == "S":
                titulo=input("Entre como o nome do Livro: -> ")
                autor=input(f"Entre com o autor de {titulo}: -> ")
                livro=Livro(titulo,autor)
                
                print(livro)
                self.acervo.append(livro)

            else:
                break

    def listar_livros(self):
        for livro in self.acervo:
            print(livro.titulo,livro.autor)

biblio = Biblioteca()
biblio.adicionar_livro()
biblio.listar_livros()


