



valor_hora=float(input("Entre com o valor da hora trabalhada em reais: -> R$"))
quant_horas=float(input("Entre com a quantidade de horas trabalhadas: - > "))
salario_bruto=valor_hora*quant_horas
desconto_irpf=round(salario_bruto*0.11,2)
desconto_inss=round(salario_bruto*0.09,2)
desconto_sindical=round(salario_bruto*0.04,2)
descontos_totais=round(desconto_irpf+desconto_inss+desconto_sindical,2)
salario_liquido=round(salario_bruto-descontos_totais,2)
salario_bruto=round(salario_bruto,2)

print(f"\n ********************************")
print(f"\n * Salário Bruto = R${salario_bruto}  *")
print(f"\n * IRPF (11%) = R${desconto_irpf}  *")
print(f"\n * INSS ( 9%) = R${desconto_inss}  *")
print(f"\n * Contribuição Sindical (04%) = R${desconto_sindical}  *")
print(f"\n * Salário Líquido = R${salario_liquido}  *")
print(f"\n ********************************")