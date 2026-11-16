from .types import DataSchemaAlunos
from typing import Literal

def criar_list_matricula(alunos: DataSchemaAlunos) -> list[str]:
    # matriculas.extend(alunos)
    matriculas = []

    for matr in alunos:
        matriculas.append(matr)
        
    return matriculas

def comparar_alunos(mat1: str, mat2: str, matriculas:DataSchemaAlunos)-> Literal[-1, 0, 1]:
