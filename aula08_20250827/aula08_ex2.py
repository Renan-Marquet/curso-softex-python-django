"""recebe numero tel 11 digitos"
"verificar se tem 11 e se todos numeros mas não pode ter 3 ou mais numeros iguais"
se for válido formatar (XX)XXXXX-XXXX.
O programa deve imprimir numro formatado ou msg de erro
"""
numeros="0123456789"
novo=""
seutel=input("Digite o numero do seu telefone.  ")
i=0

while len(seutel) != 11 or seutel[i] not in numeros :
    seutel=input("Numero inválido digite novamente. ")
    for i in range(11):
        novo=novo+seutel[i]
        #if seutel[i] not in numeros:
        # print("Entrada inválida")
        #print(f"{novo} , {seutel[i]}")
        for c in numeros:
            contador_repetidos=0
            for d in numeros:
                #print(f"num C {c} num D {d} são iguais? {c==d}")
                if c==d:
                    contador_repetidos+=1
        if contador_repetidos >= 3:
            
            print("um número se repete mais de duas vezes")
            valido = True

print(f"numero valido : ",seutel)


for c in numeros:
    contador_repetidos=0
    for d in numeros:
        #print(f"num C {c} num D {d} são iguais? {c==d}")
        if c==d:
            contador_repetidos+=1
        if contador_repetidos >= 3:
            
            print("um número se repete mais de duas vezes")
            valido = True
            break


else:
    print(f"("
            + numeros[0]
            + numeros[0]
            + ") "
            + numeros[0]
            + numeros[0]
            + numeros[0]
            + numeros[0]
            + "-"
            + numeros[0]
            + numeros[0]
            + numeros[0]
            + numeros[0]
            + numeros[0]
            + ")")