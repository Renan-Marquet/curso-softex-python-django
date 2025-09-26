vendas = [("teclado",50,2),("Mouse",25.50,4),("Monitor",300,1),("Fone",45,1),("Webcam",75.20,2)]
#vendas filtradas (valor total>100) lista de tuplas
#produtos únicos: {"monitor","Fone","Mouse","Teclado","Webcam"}
"""vendas_filtradas=[] 
produtos_unicos=[] 

i=0

for item,preco,quant in vendas:

    if preco*quant >=100 :
        vendas_filtradas.append(vendas[i])
    if quant == 1 :
        produtos_unicos.append(vendas[i])

    i+=1

print (vendas_filtradas)

print (produtos_unicos)"""

vendas_filtradas=list()
produtos_unicos=set()

for produto, valor, quant in vendas:
    valor_toral = valor * quant
    if valor_toral >= 100:
        vendas_filtradas.append(( produto, valor, quant))

    produtos_unicos.add(produto)

print("vendas filtradas (valor tota >= 100):")
print(vendas_filtradas)
print("\nProdutos únicos:")
print(produtos_unicos)



