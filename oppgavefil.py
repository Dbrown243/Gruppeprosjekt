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


<<<<<<< Updated upstream
def skrivutavtale(listemedavtaler):
    listemedavtaler = [Avtale]
    i = 0
    for avtale in listemedavtaler:
        print(i, avtale)
        i += 1

        
    
=======


# h
def lagre(avtaleliste):
    with open("avtaler.txt", "w", encoding=("UTF-8")) as file:
        for avtale in avtaleliste:
            file.writelines(str(avtale) + "\n") 
                

>>>>>>> Stashed changes

# i
def leser_file(filnavn = "avtaler.txt"):
    liste = []
    with open(filnavn, "r", encoding=("UTF-8")) as file:
        file.readfile()
        for avtale in avtaleliste:
            kolonne = linje.strip().split(";")
            avtale = kolonne[0]
            varighet = int(kolonne[3])
            tid = date.time.datetime(kolonne[2])
            avtale = Avtale(avtale, kolonne[1], tid, varighet)
            liste.append(avtale)
    return liste


# j

if __name__ == "__main__":
    a = Avtale(1, 1, 1, 1)
    b = Avtale(2, 2, 2, 2)
    liste = [a, b]
    
    lagre(liste)

#






