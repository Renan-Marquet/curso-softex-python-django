# exercicio 1 de 50

from random import randint

list1pri=int(input("entre com o numero inicial da primeira faixa: "))
list1sec=int(input("entre com o numero final da primeira faixa: "))
quant1=int(input("entre como a quantidade de numeros da primeira lista: "))
list1=[]
i=0
while i < quant1:
    list1.append(randint(list1pri,list1sec))
    i+=1


list2pri=int(input("entre com o numero inicial da segunda faixa: "))
list2sec=int(input("entre com o numero final da segunda faixa: "))
quant2=int(input("entre como a quantidade de numeros da segunda lista: "))
list2=[]
i=0
while i < quant2:
    list2.append(randint(list2pri,list2sec))
    i+=1

print(f"primeira lista{list1}")
print(f"segunda lista {list2}")

"""
        # uso de .sort() .copy e sorted()
        list4=sorted(list3)
        list5=list3.copy()
        list7=list5.copy()
        list5.sort()
        list6=list5
        print(list3,list4,list5,list6,list7) 
"""

def intesecao(list1a:list[any],list2a:list[any]) -> list[any]:
    list3a=[]
    while True:
        for i2 in range(0,len(list2a)):
            for i1 in range(0,len(list1a)):  
                if list1a[i1]==list2a[i2]:
                    if list2a[i2] not in list3a:
                        list3a.append(list2a[i2])
                    else:
                        continue               
                else:
                    continue 
        break       
    return list3a

print(intesecao(list1,list2))




