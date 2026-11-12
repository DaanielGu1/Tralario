import pickle

with open("entrada100.bin", "rb") as dicionarios:
    cursos = pickle.load(dicionarios)
    alunos = pickle.load(dicionarios)
    notas = pickle.load(dicionarios)

    dicionarios.close()

def criar_list_matricula(notas):
    matriculas = []
    for nome in notas:
        matriculas.append()
        
    return matriculas
