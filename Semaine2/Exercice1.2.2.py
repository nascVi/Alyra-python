"""
Exercice 1.2.2 : Obtenir les meilleurs pourboires
On définit un ensemble de transactions avec leur taille (en octets) et leur pourboire (en satoshis) associés :

Taille (octets)

2000 6000 800 700 1200 1000 1300 600

Pourboire (satoshis)

13000 9000 2000 1500 3500 2800 5000 1500


Étant donné un bloc donc la taille maximale est 6 000 octets, quelles sont les transactions qui devraient être incluses pour récupérer le meilleur pourboire ?

Définir un algorithme pour résoudre ce problème quel que soit le nombre de transactions. On pourra essayer une approche exhaustive qui essaye toutes les combinaisons de transactions et une approche plus tactique.

"""


# The following function gets the max bits amount available from a list, and retrieves from it the bigger possible amount of satoshis.
def bestTip(limBits, bits, satoshis, tip):

    P = [[0 for k in range(limBits + 1)] for k in range(tip + 1)]

    for i in range(tip + 1):

        for x in range(limBits + 1):

            if i == 0 or x == 0:
                P[i][x] = 0

            elif bits[i - 1] <= x:
                P[i][x] = max(satoshis[i - 1] + P[i - 1][x - bits[i - 1]], P[i - 1][x])

            else:
                P[i][x] = P[i - 1][x]

    tipsAmount = P[tip][limBits]

    trList = []
    satoshisList = []

    bitsAmount = limBits
    for i in range(tip, 0, -1):

        if tipsAmount <= 0:
            break

        if tipsAmount == P[i - 1][bitsAmount]:
            continue

        else:

            trList.append(bits[i - 1])
            satoshisList.append(satoshis[i - 1])

            tipsAmount = tipsAmount - satoshis[i - 1]
            bitsAmount = bitsAmount - bits[i - 1]

    print("\nLes transactions pour atteindre le pourboire le plus important, sont les suivantes:\n", trList)
    print("\nSoit un total de ", P[tip][limBits], "satoshis, résultant du cumule des indices correspondant:\n", satoshisList)


satoshis = [13000, 9000, 2000, 1500, 3500, 2800, 5000, 1500]
bits = [2000, 6000, 800, 700, 1200, 1000, 1300, 600]
limBits = 6000
tip = len(satoshis)

bestTip(limBits, bits, satoshis, tip)


