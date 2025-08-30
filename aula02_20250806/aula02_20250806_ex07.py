idade=int(input("digite a sua idade "))
if idade>=0 and idade<=12:
    print("você é uma criança.")
elif idade>=13 and idade<=17:
    print("você é um adolescente.")
elif idade>=18 and idade<=59:
    print("você é um adulto.")
else:
    print("É hora de você aproveitar o tempo que tem.")

