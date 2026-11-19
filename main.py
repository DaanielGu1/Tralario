import pickle
from src.merge_sort import msort
from src.utils import criar_list_matricula, formatacao

def main():
    with open("./data/entrada100.bin", "rb") as dicionarios:
        cursos = pickle.load(dicionarios)
        alunos = pickle.load(dicionarios)
        notas = pickle.load(dicionarios)

    l = criar_list_matricula(alunos)
    msort(l, alunos)

    formatacao(l, cursos, alunos, notas)
if __name__ == "__main__":
    main()