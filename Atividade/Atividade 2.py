import os 
from dataclasses import dataclass


os.system("cls || clear")
QUANT = 2


@dataclass
class Pets:
    nome: str 
    idade: int
    raca: str
    porte: str
    alimentacao:str

pets = [] 
for i in range    