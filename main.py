import pickle
from src.merge_sort import msort
from src.utils import criar_list_matricula, formatacao
import time

def main():
    x = time.time()
    with open("./data/entrada1000000.bin", "rb") as dicionarios:
        cursos = pickle.load(dicionarios)
        alunos = pickle.load(dicionarios)
        notas = pickle.load(dicionarios)

    l = criar_list_matricula(alunos)
    msort(l, cursos, alunos)

    formatacao(l, cursos, alunos, notas)
    y = time.time()

    print(y-x)
if __name__ == "__main__":
    main()