from .types import DataSchemaAlunos, DataSchemaCursos

'''
def anterior(mat1: str, mat2: str, cursos: DataSchemaCursos, alunos: DataSchemaAlunos) -> bool:
    nome1, curso1, tipo1, (ano1, semestre1), _ = alunos[mat1]
    nome2, curso2, tipo2, (ano2, semestre2), _ = alunos[mat2]

    nome_curso1 = cursos[curso1]
    nome_curso2 = cursos[curso2]

    if nome_curso1 != nome_curso2:
        return nome_curso1 < nome_curso2
    
    if tipo1 != tipo2:
        return tipo1 == "I"
    
    if ano1 != ano2:
        return ano1 > ano2
    
    if semestre1 != semestre2:
        return semestre1 > semestre2

    if nome1 != nome2:
        return nome1 < nome2

    return mat1 < mat2
'''