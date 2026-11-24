from .utils import comparador
import pickle

def msort(l: list[str], cursos, alunos):
    if len(l) > 1:
        meio = len(l) // 2
        lEsq = l[:meio]
        lDir = l[meio:]

        msort(lEsq, cursos, alunos)
        msort(lDir, cursos, alunos)
        merge(l, lEsq, lDir, cursos, alunos)

def merge(l: list[str], lEsq: list[str], lDir: list[str], cursos, alunos):
    k = 0
    i = 0
    j = 0

    while i < len(lEsq) and j < len(lDir):
        if comparador(lEsq[i], lDir[j], cursos, alunos):
            l[k] = lEsq[i]
            i += 1
        else:
            l[k] = lDir[j]
            j += 1
        
        k += 1

    while i < len(lEsq):
        l[k] = lEsq[i]
        i += 1
        k += 1

    while j < len(lDir):
        l[k] = lDir[j]
        j += 1
        k += 1