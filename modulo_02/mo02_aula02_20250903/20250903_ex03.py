acessos = [("Pedro","sucesso"),("Ana","falha"),("Maria","sucesso"),("Pedro","falha"),("Ana","falha")]
sucesso=set()
falha=set()
so_falha=set()

for nome,status in acessos:
    if status == "sucesso" :
        sucesso.add(nome)
    if status == "falha" :
        falha.add(nome)

so_falha=falha.difference(sucesso)
       
#print(falha)
print(sucesso)
print(so_falha)
