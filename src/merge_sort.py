from .utils import comparador
import pickle

with open("./data/entrada100.bin", "rb") as dicionarios:
    cursos = pickle.load(dicionarios)
    alunos = pickle.load(dicionarios)
    notas = pickle.load(dicionarios)

def msort(l: list[str]):
    if len(l) > 1:
        meio = len(l) // 2
        lEsq = l[:meio]
        lDir = l[meio:]

        msort(lEsq)
        msort(lDir)
        merge(l, lEsq, lDir)

def merge(l: list[str], lEsq: list[str], lDir: list[str]):
    k = 0
    i = 0
    j = 0

    while i < len(lEsq) and j < len(lDir):
        if comparador(lEsq[i], lDir[j], alunos):
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