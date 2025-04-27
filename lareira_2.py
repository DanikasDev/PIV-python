"""Testes"""
import random
import json
from lareira import Lareira, LareiraInicializada, LareiraGrandeAcesa

C=1
N=12
Results =[]
ListaLareiras = []
for i in range(1,N):
    ListaLareiras.append(Lareira())
    ListaLareiras.append(LareiraInicializada())
    ListaLareiras.append(LareiraGrandeAcesa())
    #x = Lareira()
    #ListaLareiras.append(x)

for lareira_corrent in ListaLareiras:
    if random.randint(0,1)==1:
        lareira_corrent.acender()
    elif random.randint(0,1)==0:
        lareira_corrent.apagar()
    C=C+1
    Results.append({C: str(lareira_corrent)})


with open("lareira_result.json", 'w', encoding = "utf-8") as fich:
    json.dump(Results, fich, ensure_ascii=False, indent=4)

#ListaLareiras[3].acender()
