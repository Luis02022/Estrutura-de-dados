from dataclasses import dataclass
import os 


os.system("cls || clear")

QUANTIDADE_ALUNOS = 2

@dataclass
class Aluno:
    nome: str
    idade:int
    peso: float
    

alunos = []
for i in range (QUANTIDADE_ALUNOS):
    os.system("cls || clear")
    aluno = Aluno(
    nome = input("Digite seu nome:"),
    idade = input("Digite sua idade:"),
    peso = input("digite seu peso:")
    )
    alunos.append(aluno)

os.system("cls || clear")

for aluno in alunos:
    print(f"Nome: {aluno.nome} de {aluno.idade} anos")
    #print(f"Idade: {aluno.idade}")
    print(f"Peso do aluno: {aluno.peso}")
    print("\n")