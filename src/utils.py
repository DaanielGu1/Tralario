from .types import DataSchema

def criar_list_matricula(alunos: DataSchema) -> list[str]:
    # matriculas.extend(alunos)
    matriculas = []

    for matr in alunos:
        matriculas.append(matr)
        
    return matriculas