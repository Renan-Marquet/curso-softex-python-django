frase=input("digite uma frase: -> ")
mfrase=frase.lower()
tamanho=len(frase)
letra_a=0
letra_e=0
letra_i=0
letra_o=0
letra_u=0
novafrase=""
for letra in mfrase:
    
    if letra=="a":
        letra_a+=1
        mfrase=mfrase.replace(letra,"1")
    elif letra=="e":
        letra_e+=1
        mfrase=mfrase.replace(letra,"2")
    elif letra=="i":
        letra_i+=1
        mfrase=mfrase.replace(letra,"3")
    elif letra=="o":
        letra_o+=1
        mfrase=mfrase.replace(letra,"4")
    elif letra=="u":
        letra_u+=1
        mfrase=mfrase.replace(letra,"5")

vogais=(letra_a+letra_e+letra_i+letra_o+letra_u)
novafrase=mfrase

print(f"Na frase original : {frase} há {vogais} vogais, sendo {letra_a} a, {letra_e} e, {letra_i} i, {letra_o} o, e {letra_u} u.")

print(f"frase original : \n {frase}")
print(f"frase condificada : \n {novafrase}")
