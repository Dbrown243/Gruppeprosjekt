#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:06:39 2022

@author: mahdi_nasser
"""

#k
class Avtale:
    def __init__(self, tittel, sted, tidspunkt, varighet, kategori):
        self.tittel = tittel
        self.sted = sted
        self.tidspunkt = tidspunkt
        self.varighet = varighet
        self.kategori = []
        
    def legg_til_kategori(self, kategori):
        self.kategori.append(kategori)
       



#L
def lagre(avtaleliste):
    with open("avtaler.txt", "w", encoding=("UTF-8")) as file:
        string = ""
        for avtale in avtaleliste:
            string += str(avtale.tittel) + ";" + str(avtale.sted.id) + ";" + str(avtale.tidspunkt) + ";" + str(avtale.varighet) + ";"
            for kategori in avtale.kategori:
                string += str(kategori.id) + ","
            string.strip(",")
                
        file.write(string)


        
"tittel;sted_id;tidspunkt;varighet;kategori1,kategori2"

kolonne = [tittel, sted, tidspunkt, varighet , ["kategori1, kategori2"]]
kategori = [1,2,3,4]


def leser_file(filnavn = "avtaler.txt"):
    liste = []
    with open(filnavn, "r", encoding=("UTF-8")) as file:
        file.readfile()
        for avtale in avtaleliste:
            kolonne = linje.strip().split(";")
            avtale = kolonne[0]
            varighet = int(kolonne[3])
            tid = date.time.datetime(kolonne[2])
            kategori = kolonne[4].split(",")
            avtale = Avtale(avtale, kolonne[1], tid, varighet)
            for kategori_id in kategori:
                avtale.legg_til_kategori(kategorier[kategori_id])
            liste.append(avtale)
    return liste


#m

listemedavtaler=[]
kategorier = dict()

while True:
    print("1 : ny_avtale")
    print("2 : skrivutavtale")
    print("3 : tarinnlister")
    print("4 : legg til kategorier")
    print("5 : legg til steder")
    print("6 : avslutt")
    menysystem = input("hva ønsker du pcen skal skrive ? ")
    if menysystem == "1":  
        ny_avtale()
    elif menysystem == "2":   
        skrivutavtale(listemedavtaler)
    elif menysystem =="3":
        tarinnlister(listemedavtaler=list, tittel=str)
    elif menysystem == "4":
        ny_kategori()
    elif menysystem == "5":
        sted()
    elif print("6"):
        break
    
#n
 def ny_avtale():
     tittel = input("skriv inn tittel ")
     skriv_ut_sted()
     index = int(input("skriv inn index:[]"))
     sted =liste_med_steder(index)
     tidspunkt = datetime.fromisoformat(input("skriv inn år, måned, tid "))
     varighet = int(input("skriv varighet "))
     
     return Avtale(tittel, sted, tidspunkt, varighet)
