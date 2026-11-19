from src.quick_sort import qsort_normal
from src.leitura_bin import binario
from src.utils import criar_list_matricula

def main():
    cursos, alunos, notas = binario()

    matriculas = criar_list_matricula(alunos)

    matriculas_ordenadas = qsort_normal(matriculas, cursos, alunos)


    print(f"Matrículas ordenadas: {matriculas_ordenadas}")

    return 0
if __name__ == "__main__":
    main()
