#ex 4 de 50 list comprehension, isinstance()

lista=[14,False,'Abc',15,True,'Çab',16.1,'Nome','OR','AND',17,18,'!?*']
listanova=[elemento for elemento in  lista if isinstance(elemento,int) or isinstance(elemento,float)] 
listanova2=[elemento for elemento in listanova if isinstance(elemento,bool)]
#juntando1=set(listanova)
#juntando2=set(listanova2)
listafinal=list(set(listanova).difference(set(listanova2)))
print(listanova)
print(listanova2)
print(listafinal)