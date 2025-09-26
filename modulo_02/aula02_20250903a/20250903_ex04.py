notas=[("Ana",9.5),("João",8.0),("Maria",10.0),("Pedro",7.5),("Ana",10.0),("Carlos",6.5)]
reprovados=set()
melhores=set()
maior=0

for nome,nota in notas: # pode ser for_,nota in notas:
    if nota < 7.0 :
        reprovados.add(nome)
    if nota > maior:
        maior=nota
for nome,nota in notas: # pode ser for_,nota in notas:
    if nota == maior:
        melhores.add(nome)

melhores=tuple(melhores)

print("\n Maior nota -> ",maior)
print(" Alunos com as melhores notas")
print(melhores)
print(" Reprovados com notas menores que 7: ")
print(reprovados,"\n")

# alunos_nota_baixa = {aluno for aluno, nota in notas if nota < 7.0}