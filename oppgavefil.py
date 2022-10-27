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
    listemedavtaler = [Avtale]
    i = 0
    for avtale in listemedavtaler:
        print(i, avtale)
        i += 1

        
    







