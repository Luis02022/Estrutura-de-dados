import os 
from dataclasses import dataclass

os.system("cls || clear")

QUANT = 3

@dataclass
class Aluno:
    nome: str 
    idade: int
    peso: float
    sexo: str
    telefone: int

alunos = []
for i in range (QUANT):
    os.system("cls || clear")
   
    nome_aluno = input("Digite seu nome: "),
    idade_aluno = input("Digite sua idade: "),
    peso_aluno = input("Digite seu peso: "),
    sexo_aluno = input("Digite seu sexo: "),
    telefone_aluno = input("Digite seu telefone: ")           

    info = Aluno(nome = nome_aluno, idade = idade_aluno, peso = peso_aluno, sexo = sexo_aluno, telefone = telefone_aluno)
    alunos.append(info)

for i, info in enumerate (alunos):
    print(f"{i+1}º ALUNO")
    print(f"Nome do aluno: {info.nome}")
    print(f"Idade do aluno: {info.idade}")
    print(f"Peso do aluno: {info.peso}")
    print(f"Telefone: {info.telefone}")
    print(f"Sexo: {info.sexo}")
    print("\n")



