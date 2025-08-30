palavra=input("digite uma palavra: -> ")
mpalavra=palavra.lower()
tamanho=len(palavra)
letra_a=0
letra_e=0
letra_i=0
letra_o=0
letra_u=0
for letra in mpalavra:
    if letra=="a":
        letra_a+=1
    elif letra=="e":
        letra_e+=1
    elif letra=="i":
        letra_i+=1
    elif letra=="o":
        letra_o+=1
    elif letra=="u":
        letra_u+=1

vogais=(letra_a+letra_e+letra_i+letra_o+letra_u)


print(f"Na palavra {palavra} há {vogais} vogais, sendo {letra_a} a, {letra_e} e, {letra_i} i, {letra_o} o, e {letra_u} u.")
