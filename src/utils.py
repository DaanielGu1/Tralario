from .types import DataSchemaAlunos
from typing import Literal

def criar_list_matricula(alunos: DataSchemaAlunos) -> list[str]:
    # matriculas.extend(alunos)
    matriculas = []

    for matr in alunos:
        matriculas.append(matr)
        
    return matriculas

