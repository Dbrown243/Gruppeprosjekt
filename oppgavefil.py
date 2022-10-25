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


   ' def ny_avtale(ny_avtale):'



