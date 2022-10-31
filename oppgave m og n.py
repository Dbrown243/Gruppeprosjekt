#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:30:16 2022

@author: mahdi_nasser
"""
class avtaler():
    def __init__(self):
        self.n =[]
    def add(self, a):
        return self.n.append(a)
    def remove(self, b):
        self.n.remove(b)
    def dis(self):
        return (self.n)
    def __str__(self):
        return (self,n)
    


obj= avtaler()



choice = 1
while choice!=0:
    print('1. delete')
    print('2. edit')
    choice=int(input('enter choice: '))
    if choice==1:
        n=int(input('enter avtale to remove: '))
        obj.remove(n)
        print('List: ', obj.dis())
    elif choice==2:
        n=int(input('enter avtale to edit: '))
        obj.replace(int(input('enter what you want to remove here: ')), int(input('enter your edit here: ')))
        print('List: ', obj.dis())
        
        
        
        
    
    