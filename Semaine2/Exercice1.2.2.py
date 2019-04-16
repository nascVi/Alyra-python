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

import math
