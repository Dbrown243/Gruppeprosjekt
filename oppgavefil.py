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

def lagre(avtaleliste):
    with open("avtaler.txt", "w", encoding=("UTF-8")) as file:
        for avtale in avtaleliste:
            file.writelines(str(avtale) + "\n") 

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

<<<<<<< Updated upstream
#<<<<<<< Updated upstream
=======
>>>>>>> Stashed changes
def skrivutavtale(listemedavtaler):
    # listemedavtaler = [Avtale]
    i = 0
    for avtale in listemedavtaler:
        print(i, avtale)
        i += 1

#<<<<<<< HEAD
#k
def tarinnlister(listemedavtaler=list, tittel=str):
    listemedstreng = []
    for avtale in listemedavtaler:
        indeks = avtale.tittel.find(tittel)
        if indeks != -1:
            listemedstreng.append(avtale)
    return listemedstreng

#L

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
<<<<<<< Updated upstream


#======= M og N
listemedavtaler = list()

def delete(liste, index):
    liste.pop(index)
    

choice = 1
while choice!=0:
    print('1. delete')
    print('2. edit')
    choice=int(input('enter choice: '))
    if choice==1:
        n=int(input('enter avtale to remove: '))
        delete(listemedavtaler, n)
        skrivutavtale(listemedavtaler)
    elif choice==2:
        n=int(input('enter avtale to edit: '))
        delete(listemedavtaler, n)
        listemedavtaler.append(ny_avtale())
        skrivutavtale(listemedavtaler) 
    
#=======


# h
def lagre(avtaleliste):
    with open("avtaler.txt", "w", encoding=("UTF-8")) as file:
        for avtale in avtaleliste:
            file.writelines(str(avtale) + "\n") 
                

#>>>>>>> Stashed changes

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

=======
                
J)
>>>>>>> Stashed changes
if __name__ == "__main__":
    a = Avtale(1, 1, 1, 1)
    b = Avtale(2, 2, 2, 2)
    liste = [a, b]
    
    lagre(liste)

#
#>>>>>>> 6cc5c433fff17b61bb824808b87e5f8034f74904






