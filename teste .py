import os 
from dataclasses import dataclass


os.system("cls || clear")

QUANTIDADE_ALUNOS = 2

@dataclass
class Aluno:
    nome: str 
    idade: int

alunos = []
for i in range (QUANTIDADE_ALUNOS):
    nome_do_aluno = input("Digite seu nome:")    
    idade_do_aluno = input("Digite sua idade:")

    aluno = Aluno(nome = nome_do_aluno, idade = idade_do_aluno)
    alunos.append(aluno)

os.system("cls || clear")    

for aluno in alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade} anos")