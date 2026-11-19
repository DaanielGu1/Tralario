import pickle
from src.merge_sort import msort
from src.quicknovo import quick_sort2
from src.utils import criar_list_matricula

def main():
    with open("./data/entrada100.bin", "rb") as dicionarios:
        cursos = pickle.load(dicionarios)
        alunos = pickle.load(dicionarios)
        notas = pickle.load(dicionarios)

    l = criar_list_matricula(alunos)
    quick_sort2(l, 0, len(l)-1, alunos)

    print(l)

if __name__ == "__main__":
    main()