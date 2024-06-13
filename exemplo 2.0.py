from dataclasses import dataclass
import os 


os.system("cls || clear")

QUANTIDADE_ALUNOS = 2

@dataclass
class Aluno:
    nome: str
    idade:int
    peso: float
    sexo: str
    telefone: int

alunos = []
for i in range (QUANTIDADE_ALUNOS):
    os.system("cls || clear")
    nome_do_luno =input("Digite seu nome:")
    idade_do_aluno = input("Digite sua idade:")
    peso_do_aluno = input("digite seu peso:")

    aluno = Aluno(nome = nome_do_luno, idade = idade_do_aluno, peso = peso_do_aluno)
    alunos.append(aluno)

os.system("cls || clear")

for aluno in alunos:
    print(f"Nome: {aluno.nome} de {aluno.idade} anos")
    print(f"Idade: {aluno.idade}")
    print(f"Peso do aluno: {aluno.peso}")