import pickle

def binario(caminho="data/entrada100.bin"):
    
    with open(caminho, "rb") as infos:
        cursos = pickle.load(infos)
        alunos = pickle.load(infos)
        notas = pickle.load(infos)

    return cursos, alunos, notas

