#Prosjektleder  : Bashar Sameer Fawaz Albittar
#Technical      : director Mahdi Nasser
#Problemguy     : Mulumba Blaise
#Bigman best    : Abdiazizzzz Hassan

# a)



# b)


# c)
from mimetypes import init

class Kategori:
    def __init__(self, id, navn, prioritet=1):
        self.id = id
        self.navn = navn
        self.prioritet = prioritet

    def __str__(self):
        # kategori = "Kategori:" + "id: "+str(self.id) + " navn: "+ str(self.navn) + "Proritet: " + str(self.prioritet)
        kategori = f"Kategori: id: {self.id}, navn: {self.navn}, Proritet: {self.prioritet}"
        return kategori

# d)
def ny_kategori():

    id = input("skriv inn id'en din her : ")
    navn= input("skriv inn navnet ditt her : ")
    prioritet = int(input("skriv inn prioriteten til kategorien her : "))

    type_kategori = Kategori(id, navn, prioritet)
    return type_kategori



# e)
# Enten lag funksjoner som lagrer og leser inn kategorier fra en egen kategori-fil, eller utvid 
# funksjonene fra øving 9 slik at de også lagrer og leser inn kategorilista. Avgjør om kategoriene 
# skal lagres i samme fil som avtalene eller i sin egen fil. 


def funksjonlagrer(kategoriliste):
    with open ("kategori.txt", "w") as file:
        for kategori in kategoriliste:
            file.write(str(kategori.id) + ";" + str(kategori.navn) + ";" + str(kategori.prioritet))
            
def funksjonleser():
    kategoriliste = []
    with open("kategori.txt", "r") as text:
        for line in text:
            split_list = line.split(";")
            id = split_list[0]
            navn = split_list[1]
            prioritet = int(split_list[2])
            kategori = Kategori(id, navn, prioritet)
            kategoriliste.append(kategori)
    return kategoriliste

 #sjekk for funksjonlagrer:
#liste_kategori = []
#a1 = ny_kategori()
#liste_kategori.append(a1)
#funksjonlagrer(liste_kategori)

#sjekk for funksjonleser:
# listemedkategorier = funksjonleser()
# for kategori in listemedkategorier:
#     print(kategori)


# f)
# Sjekk funksjonen for å skrive ut alle avtalene inkludert indeksene i lista fra øving 9 
# deloppgave g. Kan den brukes uforandret også for å skrive ut ei liste med kategorier? Hvis ja, 
# bruk den, og kanskje gi den et nytt navn for å vise det mer generelle formålet med 
# funksjonen nå. Ellers må dere enten lage en egen funksjon for å skrive ut ei liste med 
# kategorier eller modifisere funksjonen for avtaler fra øving 9 slik at den også kan brukes for 
# kategorier. 

def skrivutliste(liste):
    # liste = [Avtale]
    i = 0
    for avtale in liste:
        print(i, avtale)
        i += 1



# g)

class Sted:
    def __init__(self, id,navn,gate, post,post_sted):
        self.id = id 
        self.navn = navn 
        self.gate = gate
        self.post = post 
        self.post_sted= post_sted
    


    def __str__(self):
        return f"{self.gate}, {self.post}, {self.post_sted}"


        









# h)
def sted ():
    id = input("skriv inn id ")
    navn = input("skriv inn navn ")
    gate = input("skrin inn adresse")
    post= input("skriv inn postnummer")
    post_sted = input("skriv inn post_sted")

    sted_objekt = Sted(id,navn,gate, post,post_sted)
    return sted_objekt







# i)



# j)



# k)



# l)



# m)



# n)



# o)



# p)



# q)


















#bare for å teste
# if __name__ == "__main__":
#     k1 = Kategori(0, "jobb", 3)
#     k2 = Kategori(0, "trening", 2)
    
#     kat_list = [k1, k2]
    
#     skrivutliste(kat_list)