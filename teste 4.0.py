import os
from dataclasses import dataclass

def logoSenai():
    os.system("cls || clear")
    print("=== SENAI ===")

@dataclass
class Valor:
    nome: str
    sobrenome: str
    peso: float
    altura: float
    idade: int
    resultado: str
    imc: float
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

def resultado_imc(imc):
    if imc<18.5:
        resultado = "Muito Magro"
    elif imc <25:
        resultado = "Peso Normal"
    elif imc <30:
        resultado = "Acima do peso"
    elif imc <35:
        resultado = "Obesidade grau I"
    elif imc <40:
        resultado = "Obesidade grau II"
    else:
        resultado = "Obesidade grau III (morbida)"
    return resultado

dados = []

while True:
    logoSenai()
    nome = input("Digite seu nome ou sair para encerrar o programa: ")
    if nome.lower() == 'sair':
        break
    sobrenome = input("Digite o sobrenome: ")
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))

    imc = calcular_imc(peso, altura)
    resultado_calculo_imc = resultado_imc(imc)
    
    dadosUsuario = Valor(nome= nome,sobrenome=sobrenome,idade=idade,altura=altura,peso=peso, imc = imc, resultado = resultado_calculo_imc)
    dados.append(dadosUsuario)

for i in dados:
    print(f"Nome: {i.nome} {i.sobrenome}")
    print(f"Idade: {i.idade}")
    print(f"Peso: {i.peso:.2f}", "Kg")
    print(f"Altura: {i.altura:.2f}")
    print(f"IMC: {i.imc:.2f}")
    print(f"Situacao: {i.resultado}")