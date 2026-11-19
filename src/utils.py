from .types import DataSchemaAlunos, DataSchemaCursos, DataSchemaNotas
from typing import Literal

def criar_list_matricula(alunos: DataSchemaAlunos) -> list[str]:
    # matriculas.extend(alunos)
    matriculas = []

    for matr in alunos:
        matriculas.append(matr)
        
    return matriculas

def comparador(mat1: str, mat2: str, matriculas: DataSchemaAlunos) -> bool:
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

def formatacao(l: list[str], cursos: DataSchemaCursos, alunos: DataSchemaAlunos, notas: DataSchemaNotas):
    cursoAux = ''
    tipoAux = ''
    ficha = ''

    f = open("teste.txt", "w")

    for aluno in l:
        nome, curso, tipo, (ano, semestre), status = alunos[aluno]

        if curso != cursoAux:
            f.write(f'Curso: {cursos[curso]}\n')
            cursoAux = curso

        if tipo != tipoAux:
            if tipo == "I":
                f.write('Ingressantes:\n')
            else:
                f.write('Concluintes:\n')

            tipoAux = tipo
    
        ficha = f'* {nome} - {aluno} - {ano}/{semestre}'
        
        if status:
            ficha += ' - Ok'
                
        else:
            ficha += ' - Pendente'

        if tipo == "C":
            if aluno in notas:
                ficha += f' - {notas[aluno]}'
            else:
                ficha += ' - 0.00'

        f.write(f'{ficha}\n')