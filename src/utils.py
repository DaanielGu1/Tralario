from .types import DataSchemaAlunos, DataSchemaCursos, DataSchemaNotas
from typing import Literal

def criar_list_matricula(alunos: DataSchemaAlunos) -> list[str]:
    # matriculas.extend(alunos)
    matriculas = []

    for matr in alunos:
        matriculas.append(matr)
        
    return matriculas

def comparador(mat1: str, mat2: str, cursos: DataSchemaCursos, alunos: DataSchemaAlunos) -> bool:
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