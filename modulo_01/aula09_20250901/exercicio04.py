"""entrada: Vários valores digitados pelo usuário, um de cada vez
    saída: A soma dos numeros válidos e a lista dos numeros coletados.
    validos enrte 0 e 100
    
    entradas: 10,50, abc, -5,101,20,-1
    resultado esperado :
    Soma dos números válidos=80
    numeros coletados:[10,50,20]"""

soma=0
numero=0
listanumero=[]


while True:
    numero=input("entre com um numero inteiro entre 0 e 100 ou digite -1 para parar")
    if numero == "-1":
        break
    if numero.isdigit() and int(numero)<100 and int(numero)>0 :
        soma=soma+int(numero)
        listanumero.append(numero)

    print(soma, listanumero )
 