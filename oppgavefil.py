from calendar import leapdays
from datetime import datetime
from turtle import title


class Avtale:
    def __init__(self, tittel, sted, tidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self.tidspunkt = tidspunkt
        self.varighet = varighet

    def __str__(self):
        return f"{self.tittel}, {self.sted}, {self.tidspunkt}, {self.varighet}"

def ny_avtale():
    tittel = input("skriv inn tittel ")
    sted = input("skriv inn sted ")
    tidspunkt = datetime.fromisoformat(input("skriv inn år, måned, tied "))
    varighet = int(input("skriv varighet "))
    
    return Avtale(tittel, sted, tidspunkt, varighet)


def skrivutavtale(listemedavtaler):
    # listemedavtaler = [Avtale]
    i = 0
    for avtale in listemedavtaler:
        print(i, avtale)
        i += 1


def tarinnlister(listemedavtaler=list, tittel=str):
    listemedstreng = []
    for avtale in listemedavtaler:
        indeks = avtale.tittel.find(tittel)
        if avtale.tittel[indeks] == tittel:
            listemedstreng.append(avtale)
    return listemedstreng

listemedavtaler=[]
while True:
    print("1 : ny_avtale")
    print("2 : skrivutavtale")
    print("3 : tarinnlister")
    print("4 : avslutt")
    menysystem = input("hva ønsker du pcen skal skrive ? ")
    if menysystem == "1":  
        ny_avtale()
    elif menysystem == "2":   
        skrivutavtale(listemedavtaler)
    elif menysystem =="3":
        tarinnlister(listemedavtaler=list, tittel=str)
    elif print("4"):
        break








