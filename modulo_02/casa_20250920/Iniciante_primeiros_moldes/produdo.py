class Produto:
    def __init__(self,produto: str,preco: float) -> None:
        self.produto = produto
        self.preco = preco
        

prod1=Produto("Caderno",15.50)
prod2=Produto("Caneta",3.00)

print(prod1.produto)
print(prod1.preco)
print(prod2.produto)
print(prod2.preco)
