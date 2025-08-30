frase=input("digite uma frase: -> ")
letra=input("escolha uma letra e digite-a -> ")
contador=frase.count(letra)
if contador!=0:
    print(f"a letra {letra} aparece {contador} vêz(es) na frase: {frase}")
else:
    print(f"a letra {letra} não aparece na frase: {frase}")
