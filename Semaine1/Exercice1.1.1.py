
# import de la librairie nécessaire
import random

# initialisation de la variable guess
guess = 0

# Message d'accueil et variable pour stocker le nom du joueur
print("Bonjour! comment t'appelles-tu?")
name = input()

# initialisation du nombre aléatoire number
number = random.randint(1, 100)
print("Ok, " + name + ", je pense a un nombre entier, de 1 et 100. Le quel est-il?")

# boucle pour relancer tant que le nombre n'est pas trouvé
while guess != number:
    # invitation a l'entrée d'un entier
    print("Allez, choisi ton nombre.")
    # guess devient la saisie de l'utilisateur
    guess = input()
    # guess devient un entier
    guess = int(guess)
    # if statements pour les différents rapports à la valeur recherché
    if guess < number:
        if (number - guess) < 6:
            print("tu es très proche.")
        elif (number - guess) < 11:
            print("Tu te rapproche.")
        print("Le nombre que tu cherches est plus grand.")

    elif guess > number:
        if (guess - number) < 6:
            print("Tu es très proche.")
        elif (guess - number) < 11:
            print("Tu te rapproche.")
        print("Le nombre est encore en dessous.")

    else:
        break
# Sortie de la boucle, le jeu est terminé
print("Excellent! " + name + "! Tu as vu juste.")
