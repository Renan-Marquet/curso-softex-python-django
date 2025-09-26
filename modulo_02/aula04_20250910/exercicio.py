# definindo funcao

def diga_oi():
        print("Oi! Tudo bem?")

        # chameando a função

diga_oi()

# 'nome' é um parâmetro

def saudar(nome):
    print(f"Olá, {nome}!")

saudar("Maria")
saudar("joão")

def somar(a,b):
    return a+b

total=somar(5,3)
print(total*2)

def calcular_area_perimetro(base,altura):
     area=base*altura
     perimetro=2*(base+altura)
     return area, perimetro

resultados=calcular_area_perimetro(5,10)
print(f"Resultados é uma tupla {resultados}")

def encontrar_par(lista):
    for numero in lista:
          if numero % 2 == 0:
               return numero
    return None

novo=encontrar_par([1,3,5,6,8])
# retorna o primeiro par
print(novo)

def verificar_idade(idade):
     if idade >= 18:
        return "Marior de idade"
     return "Menor de idade"

print(verificar_idade(25))
print(verificar_idade(16))

def sauda_com_idade(nome: str, idade: int) -> None:
     """ ela recebe um nome string e uma idade inteiro e faz print dos dados"""
     print(f"Olá, {nome}. Você tem {idade} anos.")

sauda_com_idade("Anderson",42)

def somar(a: int, b: int) -> int:
     return a+b
 
dobrar=lambda x : x*2
print(dobrar(5))

