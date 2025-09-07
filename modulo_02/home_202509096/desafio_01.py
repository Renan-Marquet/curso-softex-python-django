# Vendas e Descontos
vendas=[('Mesa',200),('Cadeira',120),('Mesa',200),('Luminária',50)]
produtos_com_desconto=['Mesa','Luminária']
total=0.0
lista_vendas=[]
produto=""
produtos_sem_desconto=[]
valor_do_desconto=0.0

for produto,valor in vendas:
    total=total+(float(valor))
    lista_vendas.append(produto)
    if produto not in produtos_com_desconto:
        produtos_sem_desconto.append(produto)
    else:
        valor_do_desconto=valor_do_desconto+(float(valor))




print(f" Valor total das vendas: ", total)
#print(f" Mercadorias vendidas ",lista_vendas)
print(f" Valor das vendas das mercadorias com desconto: " , valor_do_desconto)
print(f" Mercadorias sem desconto: ", produtos_sem_desconto)
