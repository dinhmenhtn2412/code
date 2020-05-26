# -*- coding: utf-8 -*-
"""
Created on Mon May 25 10:54:55 2020

@author: PC
"""

def Songuyento(n):
    if(n<2):
        return False
    i=2;
    while i <= n/2:
        if(n%i == 0):
            return False
        i+=1
    return True

a=[1,4,6,7,8,11,13]

print('\n List A: ')
for i in a:
    print (i, end=" ")
print("\n")
print('{:-^30}'.format("KET QUA LOC SO NT"))
for i in a:
    if(Songuyento(i)):
        print(i, end= " ")
