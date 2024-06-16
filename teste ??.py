import os
from dataclasses import dataclass

QUANT = 2

@dataclass
class Numero:
    n1: int 
    n2: int

medias = []
for i in range(QUANT):
    os.system("cls || clear")
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    # Criação do objeto Numero
    notas = Numero(
        n1=numero1,
        n2=numero2
    )    

    # Adicionar o objeto à lista
    medias.append(notas)

# Exibição dos dados das médias
for i, notas in enumerate(medias):
    print(f"{i+1}ª MÉDIA")
    print(f"Primeiro número: {notas.n1}")
    print(f"Segundo número: {notas.n2}")
