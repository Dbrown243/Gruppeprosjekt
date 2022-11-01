#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:30:16 2022

@author: mahdi_nasser
"""

    

listeAvaler = list()

def delete(liste, index):
    liste.pop(index)
    

choice = 1
while choice!=0:
    print('1. delete')
    print('2. edit')
    choice=int(input('enter choice: '))
    if choice==1:
        n=int(input('enter avtale to remove: '))
        delete(listeAvaler, n)
        skrivutavtale(listeavaler)
    elif choice==2:
        n=int(input('enter avtale to edit: '))
        delete(listeAvaler, n)
        listeAvaler.append(ny_avtale())
        skrivutavtale(listeAvaler)
        
        
        
    
    