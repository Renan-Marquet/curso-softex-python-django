# Análise de Dados de Acessos
entrada=[]
#saida=[]
lista=[]
nova=()
#lista_valida=[]
tempo_total=0.0
usuarios=set()
#listc=set()
#vazio=()

while True:
  
    usuario=input("\n Entre com o nome do Usuário ou digite parar para encerrar o programa: -> ")
    if usuario == "parar":
        print("\n Você encerrou o programa. \n")
        break

    status=input("Digite 1 para sucesso ou 2 para falha -> ")

    while True:
        
        if status == "1":
            status="sucesso"
            break
        elif status == "2":
            status="falha"
            #entrada="vazio"
            break
        else:
            status=input(" Entrada inválida, digite apenas 1 ou 2 -> ")
    while True:
        if status=="falha":
            break
        try:
            tempo=float(input(" Entre com a duração da sessão: -> "))
        
        except ValueError:
            print(" Digite apenas numeros. -> ")
            continue
        
        if tempo>0:
            break
        else:
            print(" Digite apenas numeros positivos. -> ")
         

    if status == "sucesso":
        entrada.append(usuario)
        entrada.append(status)
        entrada.append(tempo)
        tempo_total=tempo_total+tempo
        usuarios.add(usuario)

    if entrada == ():
        entrada=[]
        break
        #print(entrada)
    else:
        nova=tuple(entrada)
        entrada=[]
        #print(nova)

        lista.append(nova)
      
print(" Registro dos acessos Válidos: ->  ",lista)
print(" Usuários bem sucedidos: -> ", usuarios)
print(" Tempo total de acesso: - > ", tempo_total)


