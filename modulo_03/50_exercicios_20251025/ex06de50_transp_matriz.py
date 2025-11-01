# ex 6 de 50 trasposição de matriz

    # Uma matriz \(N\times M\) é uma tabela retangular com 
    #\(N\) linhas (horizontais) e \(M\) colunas (verticais). 
    #Onde o primeiro número (\(N\)) se refere ao número de linhas
    #e o segundo número (\(M\)) representa o número de colunas. 
    #Cada elemento da matriz é representado por \(a_{ij}\),
    #onde '\(i\)' é o número da linha e '\(j\)' é o número da coluna.

"""lista de linhas [['A', 'B', 'C', 'D', 'E', 'F'], 
                    ['G', 'H', 'I', 'J', 'K', 'L'], 
                    ['M', 'N', 'O', 'P', 'Q', 'R'],
                    ['S', 'T', 'U', 'V', 'W', 'X']]"""
"""matriz=
        [{(0,0):'A'},{(0,1):'B'},{(0,2):'C'},{(0,3):'D'},{(0,4):'E'},{(0,5):'F'},
        {(1,0):'G'},{(1,1):'H'},{(1,2):'I'},{(1,3):'J'},{(1,4):'K'},{(1,5):'L'},
        {(2,0):'M'},{(2,1):'N'},{(2,2):'O'},{(2,3):'P'},{(2,4):'Q'},{(2,5):'R'},
        {(3,0):'S'},{(3,1):'T'},{(3,2):'U'},{(3,3):'V'},{(3,4):'W'},{(3,5):'X'}]"""
# quantidade de novaslinhas tem que ficar igual à quantidade das antigas colunas
# quantidade de novascolunas tem que ficar igual à quantidade das antigas linhas
"""contramatriz=[{(0,0):'A'},{(0,1):'G'},{(0,2):'M'},{(0,3):'S'},
                {(1,0):'B'},{(1,1):'H'},{(1,2):'N'},{(1,3):'T'},
                {(2,0):'C'},{(2,1):'I'},{(2,2):'O'},{(2,3):'U'},
                {(3,0):'D'},{(3,1):'J'},{(3,2):'P'},{(3,3):'V'},
                {(4,0):'E'},{(4,1):'K'},{(4,2):'Q'},{(4,3):'W'},
                {(5,0):'F'},{(5,1):'L'},{(5,2):'R'},{(5,3):'X'}"""

# Início

linha1=list('ABCDEF')
linha2=list('GHIJKL')
linha3=list('MNOPQR')
linha4=list('STUVWX')

listadelinhas=[linha1,linha2,linha3,linha4]

quant_line=len(listadelinhas) # quantidade de linhas
quant_col=len(linha1) # quantidade de colunas

def faz_matriz(linhas:list[any],quant_l,quant_c) -> list:
    matriz={}
    for i in range(quant_l):
        linha=linhas[i]
        #print(linha)
        for j in range(quant_c) : #(len(linha)):
               #print(linha[j])
               indice=(i,j)
               matriz.update({indice:linha[j]})
               #print(indice)
            #print(f"i={i} j={j} linha{i+1} {linha[i]}")
            #elemento={(i,j):linhas[i]}
            #print(elemento)
    return matriz
    

def faz_contramatriz(linhas:list[any],quant_l,quant_c) -> list:
    contramatriz={}
    for i in range(quant_l):
        novalinha=linhas[i]
        for j in range(quant_c):
                #print(novalinha[j])
                indice=(j,i)
                contramatriz.update({indice:novalinha[j]})

    return contramatriz

print(f"\n A lista de linhas a ser trabalhada é : \n {listadelinhas}")
print(f"\n Essa é a matriz originária: \n {faz_matriz(listadelinhas,quant_line,quant_col)}")
print(f"\n E essa é a matriz transposta: \n {faz_contramatriz(listadelinhas,quant_line,quant_col)}")



