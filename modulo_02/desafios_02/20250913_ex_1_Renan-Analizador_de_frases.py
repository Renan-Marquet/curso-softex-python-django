# Analizador de frases

print(f"*"*90)

frase=input("\n Digite uma frase. ->  ")

def palavras() -> int:
    temp=frase.split()
    result=len(temp)
    print(f" A frase dada tem {result} palavras.")
    return

def vogais() -> int:
    contavogal=0
    temp=frase.lower()
    vogal=['a','á','à','ã','â','ä','e','é','è','ê','ë','i','í','ì','î','ï','o','ó','ò','õ','ô','ö','u','ú','ù','û','ü']
    for i in temp:
        for t in vogal:
            if i==t:
                contavogal+=1
    print(f" A frase dada tem {contavogal} vogais." )
    return

def consoantes() -> int:
    contaconsoante=0
    temp=frase.lower()
    consoante="bcdfghjklmnpqrstvwxyzñç"
    for i in temp:
        for t in consoante:
            if i==t:
                contaconsoante+=1
    print(f" A frase dada tem {contaconsoante} consoantes." )
    return

def palindromo() -> bool:

    pfrase=frase.lower()
    pfrase=pfrase.replace(".","")
    pfrase=pfrase.replace("?","")
    pfrase=pfrase.replace("!","")
    pfrase=pfrase.replace("¿","")
    pfrase=pfrase.replace("¡","")  
     #print(pfrase)
    esarf=pfrase[::-1]
    #print(esarf)
    if pfrase==esarf:
        print(" A frase é um palíndromo.")
    else:
        print(" A frase não é um palíndromo.")
    return

palavras()
vogais()
consoantes()
palindromo()

print(f"\n","*"*90)