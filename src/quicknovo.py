from .utils import comparador

def troca(l,i,j):
    aux = l[i]
    l[i] = l[j]
    l[j] = aux

def quick_sort2(l, inicio, fim, alunos):
    if (inicio < fim):
            pos = particao(l, inicio, fim, alunos)
            quick_sort2(l, inicio, pos-1, alunos)
            quick_sort2(l, pos+1, fim, alunos)

def particao(l, inicio, fim, alunos):
    pivo = l[inicio]
    i = inicio + 1
    j = fim

    #comparador(x, y, l): retorna True se X for maior que Y, e retorna False se Y maior que X
    while (i <= j):
        matric_i = l[i]
        matric_j = l[j]
        while (i <= j and comparador(matric_i, pivo, alunos)): 
            i+= 1
            if (i <= fim):
                matric_i = l[i]
        while (j >= i and comparador(pivo, matric_j, alunos)):
            j-= 1
            matric_j = l[j]

        if (i < j):
            troca(l, i, j)

    troca(l, inicio, j)
    return j