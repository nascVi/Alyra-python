
from math import pi


class Cercle:
    def __init__(self, r):
        self.r = r

    def aire(self):
        return pi * self.r ** 2

    def perimetre(self):
        return 2 * pi * self.r


def main():
    print("*** Trouver l'aire du cercle *** ")

    r = input("Entrez le rayon pour le calcul : ")
    try:
        r = int(r)
        cercle = Cercle(r)
        print("L'aire est de : " + str(cercle.aire()))
        print("Pour un périmètre de : " + str(cercle.perimetre()))
    except ValueError:
        print("Le rayon doit être un entier")


main()

