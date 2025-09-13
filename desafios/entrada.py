x=0

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

    


print(x+y)