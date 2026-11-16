import pickle

with open("entrada100.bin", "rb") as dicionarios:
    cursos = pickle.load(dicionarios)
    alunos = pickle.load(dicionarios)
    notas = pickle.load(dicionarios)
