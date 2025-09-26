#Exercício 2: Calculadora de desconto

numero2=input("Digite o preço original do produto desejado:   ")

floatnumero=float(numero2)
if floatnumero>100.00:
    percentual=floatnumero*0.1
    novopreco=floatnumero-percentual
    print("O novo preço com desconto do produto é ",novopreco)
else:
    print("Este valor não dá direito a desconto.")
