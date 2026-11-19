from .enade_sort import anterior
from .types import DataSchemaAlunos, DataSchemaCursos

def qsort_normal(l: list[str], cursos: DataSchemaCursos, alunos: DataSchemaAlunos) -> list[str]:
    if len(l) <= 1:
        return l
    else:
        pivo = l[0]
        menores = []
        maiores = []
        for i in range(1,len(l)):
            if anterior(l[i], pivo, cursos, alunos):
                menores.append(l[i])
            else:
                maiores.append(l[i])

        return qsort_normal(menores, cursos, alunos) + [pivo] + qsort_normal(maiores, cursos, alunos)