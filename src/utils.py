from .types import DataSchemaAlunos
from typing import Literal

def criar_list_matricula(alunos: DataSchemaAlunos) -> list[str]:
    # matriculas.extend(alunos)
    matriculas = []

    for matr in alunos:
        matriculas.append(matr)
        
    return matriculas

def comparador(mat1: str, mat2: str, matriculas: DataSchema) -> bool:
    nome1, curso1, tipo1, (ano1, semestre1), _ = matriculas[mat1]
    nome2, curso2, tipo2, (ano2, semestre2), _ = matriculas[mat2]

    if curso1 < curso2:
        return True
    if curso1 > curso2:
        return False # Se passar disso, houve empate.

    if tipo1 > tipo2:
        return True
    if tipo1 < tipo2:
        return False

    if ano1 > ano2:
        return True
    if ano1 < ano2: #um comparador para o ano, se houver empate, compara o semestre
        return False

    if semestre1 > semestre2:
        return True
    if semestre1 < semestre2:
        return False

    if nome1 < nome2:
        return True
    if nome1 > nome2:
        return False

    return mat1 < mat2
    