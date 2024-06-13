import os 
from dataclasses import dataclass


os.system("cls || clear")
QUANT = 2

@dataclass
class Aluno:
    titulo: str 
    autor: str
    numero_paginas: int
    preco: float

alunos = []
for i in range (QUANT):
    os.system("cls || clear")
    aluno = Aluno(
        titulo = input("Digite o título do livro:"),
        autor = input("Digite o autor do livro:"),
        numero_paginas = input("Quantas páginas o livro possui?"),
        preco = input("Digite o preço do livro:")

    )

    alunos.append(aluno)

os.system("cls || clear")

for aluno in alunos:
    print(f"Título do livro: {aluno.titulo}")
    print(f"Autor do livro: {aluno.autor}")
    print(f"Número de páginas: {aluno.numero_paginas}")
    print(f"Preço do livro: R${aluno.preco}")
    print("\n")