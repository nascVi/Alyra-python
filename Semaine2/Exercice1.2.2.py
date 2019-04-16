'''
Exercice 1.2.2 : Obtenir les meilleurs pourboires
On définit un ensemble de transactions avec leur taille (en octets) et leur pourboire (en satoshis) associés :

Taille (octets)

2000 6000 800 700 1200 1000 1300 600

Pourboire (satoshis)

13000 9000 2000 1500 3500 2800 5000 1500


Étant donné un bloc donc la taille maximale est 6 000 octets, quelles sont les transactions qui devraient être incluses pour récupérer le meilleur pourboire ?

Définir un algorithme pour résoudre ce problème quel que soit le nombre de transactions. On pourra essayer une approche exhaustive qui essaye toutes les combinaisons de transactions et une approche plus tactique.

'''

import os
import math
import sys
from itertools import *

# initial array of the transactions datas
trans = [[600,1500], [700, 1500], [800, 2000], [1000, 2800], [1200, 3500], [1300, 5000], [2000, 13000], [6000, 9000]]

# get transation by the tips
tip_trans = sorted(trans, key=lambda l:l[1], reverse=True)


# function to mix and extract the best tip from transactions 
def mix_trans(a):
    mix = combinations_with_replacement(tip_trans, a)
    return mix

limBit = 6000
# Amount of transactions available
a = 1
fin_tip = 0
fin_a = 0

while a <=10 :
# The limit being fixed to 6000 bits, there will be a maximum of 10 transactions
    M = mix_trans(a)
    for n in M:
        i=0
        tip = 0
        bit = 0
        while i < a :
            tip = tip + n[i][1]
            bit = bit + n[i][0]
            i+=1

        if bit <= limBit :
        #The amount of transactions sorted as soon as the top bits value (6000), is reached
            print("\n A", a,"transactions, le plus gros pourboire est de:", tip, " satoshis, et" , bit, "octets.")
            break
        
    if tip > fin_tip :
        fin_tip = tip
        fin_a = a
    a+=1
    
print("\n LE MEILLEURS POURBOIRE ET DE", fin_tip, "SATOSHIS, OBTENU SUITE A", fin_a, "TRANSACTIONS. \n")


