# Super Calculadora Interativa
x=0
y=0 
r=0
v=True
# Soma
def soma() -> float:
    while True:
        try:
            x=float(input("Entre com o primeiro número: -> "))
            break
        except ValueError:
            print("Entre apenas com números")
    while True:
        try:
            y=float(input("Entre com o segundo número: -> "))
            break
        except ValueError:
            print("Entre apenas com números")
            continue
    r=x+y
    print(f"Resultado: {r}")
# Subtração
def subtrai() -> float:
    while True:
        try:
            x=float(input("Entre com o primeiro número: -> "))
            break
        except ValueError:
            print("Entre apenas com números")
    while True:
        try:
            y=float(input("Entre com o segundo número: -> "))
            break
        except ValueError:
            print("Entre apenas com números")
            continue
    r=x-y
    print(f"Resultado: {r}")
# Multiplicação
def multiplica() -> float:
    while True:
        try:
            x=float(input("Entre com o primeiro número: -> "))
            break
        except ValueError:
            print("Entre apenas com números") 
    while True:
        try:
            y=float(input("Entre com o segundo número: -> "))
            break
        except ValueError:
            print("Entre apenas com números")
            continue
    r=x*y
    print(f"Resultado: {r}")
# Divisão
def divide() -> float:
    while True:
        try:
            x=float(input("Entre com o primeiro número: -> "))
            break
        except ValueError:
            print("Entre apenas com números")
    while True:
        try:
            y=float(input("Entre com o segundo número: -> "))
            break
        except ValueError:
            print("Entre apenas com números")
            continue
    try:
        r=x/y
        print(f"Resultado: {r}")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero!")

while v==True:
     print("\n===CALCULADORA===")
     print("1 - Somar")
     print("2 - Subrair")
     print("3 - Multiplicar")
     print("4 - Dividir")
     print("5 - Sair")
     entrada=input(" -> ")

     if entrada=="1":
        soma()
     elif entrada=="2":
        subtrai()
     elif entrada=="3":
        multiplica()
     elif entrada=="4":
        divide()
     elif entrada=="5":
        v=False
     else:
          continue
          

