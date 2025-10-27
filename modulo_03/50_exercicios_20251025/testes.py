print (15%2)
print(15/2)
print(abs(15/2))
a=15
b=2
print(abs(15-(15%2))/2)
print(int(15/2))
"""
palavra=str
print(palavra)
while palavra != "sair":
    palavra =input("digite qualquer coisa.")
    print(f"Você digitou: {palavra}")
    if palavra.isalpha():
        print("Você digitou só letras.")
    elif palavra.isdigit():
        print("voce digitou so numeros")
    elif palavra.isspace():
        print("voce digitou so espacos em branco")
    elif palavra.isalnum():
        print("voce digitou numeros e letras")
    elif palavra.islower():
        print("voce digitou letras minusculas")
    elif palavra.isupper():
        print("voce digitou letras maiusculas")
"""
"""
seq=range(3,35,2)
seq2=list(seq)
print(list(seq2))
c=0
for ex in range(3,35,2):
    c+=1
    print(f"Olá! loop numero {c} a iteração é {ex}")
"""
palavra=str
while palavra != "sair":
    palavra=input(("digite uma palavra ").lower())
    #print(len(palavra))
    letra=input(("digite uma letra ").lower())
    for indice in range(len(palavra)):   
        if letra == palavra[indice]:
            print(f"O caractere '{letra}' está na posicão {indice+1} no indice {indice}")

"""palavra="Programação"
print(palavra.lower())
print(len(palavra))"""