'''
Exercice 1.2.1: Calculer la factorielle d'un nombre
On souhaite calculer factoriel d'un nombre a. Factoriel s'exprime comme le produit des entiers jusqu'à a inclus : a! = 1 x 2 x 3 ... x a

Définir un programme pour calculer la factorielle d'un nombre a . Quel est le nombre d'opérations à effectuer?

Discutons en ensemble sur le forum:
https://forum.alyra.fr/t/exercice-1-2-1-calculer-la-factorielle-dun-nombre/71
'''

import os
import math

# Tant que n n'est pas N la console propose l'entrée d'un nombre
n = -1

while n<0:
    n = input("\n Calculer la valeur factorielle d'un nombre de votre choix:  ")

    try:
        # Soit n la valeur entrée par l'utilisateur convertie pour le calcule
        n = int(n)

        # Prise en compte de la saisie d'une valeur autre qu'un N
    except ValueError:
        print("Le calcul sera effectué à partir d'un entier naturel.")
        n = -1
    continue

# initialisation des variables pour le nombre d'opérations nécessaires et pour la factorielle
i = 1
f = 1

while i <= n :
    f = f * i
    i = i+1
    # nombre d'opérations effectuées
    print(i)

print("La factorielle pour ", n, "est: ", f)


