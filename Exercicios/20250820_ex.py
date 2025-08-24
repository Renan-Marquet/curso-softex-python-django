

from decimal import Decimal, ROUND_HALF_UP


print("Entre com o valor da hora trabalhada, utilize")
valor_hora=float(input("o ponto como separador de casas decimais -> R$ "))
quant_horas=float(input("Entre com a quantidade de horas trabalhadas: - > "))
salario_bruto=valor_hora*quant_horas
desconto_irpf=round(salario_bruto*0.11,2)
desconto_inss=round(salario_bruto*0.09,2)
desconto_sindical=round(salario_bruto*0.04,2)
descontos_totais=round(desconto_irpf+desconto_inss+desconto_sindical,2)
salario_liquido=round(salario_bruto-descontos_totais,2)
salario_bruto=round(salario_bruto,2)

print(f"\n ********************************")
tempx=salario_bruto
print(f"\n * Salário Bruto = R$ {Decimal(str(tempx)).quantize(Decimal('0.01'),ROUND_HALF_UP):,.2f} *")
tempx=desconto_irpf
print(f"\n * IRPF (11%) = R$ {Decimal(str(tempx)).quantize(Decimal('0.01'),ROUND_HALF_UP):,.2f} *")
tempx=desconto_inss
print(f"\n * INSS ( 9%) = R$ {Decimal(str(tempx)).quantize(Decimal('0.01'),ROUND_HALF_UP):,.2f}  *")
tempx=desconto_sindical
print(f"\n * Contribuição Sindical (04%) = R$ {Decimal(str(tempx)).quantize(Decimal('0.01'),ROUND_HALF_UP):,.2f} *")
tempx=salario_liquido
tempy=f"{tempx:_.2f}"
tempy=tempy.replace(".",",").replace("_",".")
print(f"\n * Salário Líquido = R$ {tempy}  *")
print(f"\n * Salário Líquido = R$ {Decimal(str(tempx)).quantize(Decimal('0.01'),ROUND_HALF_UP):,.2f}  *")
print(f"\n * Salário Líquido = R$ {tempy}  *")
print("   Notação Brasileira!")

print(f"\n ********************************")