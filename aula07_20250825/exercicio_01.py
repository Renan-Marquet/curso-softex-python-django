preco_hamburguer=1000.00
# preco_hamburguer=float(preco_hamburguer)
cupom_desconto="ABCD"
nome_produto="produto"
while nome_produto != "hamburguer":
    nome_produto=input("Entre com o nome do produto  ") 
    nome_produto=nome_produto.lower()
cupon=input("Possui um cupom de desconto? Digite S ou N ")
cupon=cupon.upper()
if cupon == "S":
    desconto=input("Entre com o código do cupom ")
    While True:
    if desconto==cupom_desconto:
        print(f"O valor do hamburguer é: R$ {preco_hamburguer:,.2f}")
        print(f"O valor do desconto é: R$ {preco_hamburguer*0.2:,.2f}")
        print(f"O valor a pagar é: R$ {preco_hamburguer-preco_hamburguer*0.2:,.2f}")
        break
    else:
        print("Cupom inválido deseja continuar?")
        denovo=input("Digite S ou N ")
        denovo=denovo.upper()
        if denovo=="N":
            break
        

print(f"O valor do hamburguer é: R$ {preco_hamburguer:,.2f}")
             
#print(nome_produto)
