
from dataclasses import dataclass
import os 

os.system("cls || clear")

QUANT = 2 


@dataclass
class Aluno:
    nome: str 
    idade: int

alunos = []

for i in range (QUANT):
    aluno = Aluno(
        nome = input("Digite seu nome:"),
        idade = input("Digite sua idade:")
    
    )
    alunos.append(aluno)

arquivo = 'alunos.txt'

with open(arquivo,'w') as arquivo:
    for aluno in alunos:
        arquivo.write(f"Nome: {aluno.nome}\nIdade: {aluno.idade}\n")

print("Dados Gravados com sucesso")   


arquivo_de_origem = 'alunos.txt'

lista_alunos = []

with open()

