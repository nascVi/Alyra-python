
# call for the appropriate library
import random

# Distinct function to compare the user number to the interface estimation
def comparaison(estimation, solution, min, max):

    if estimation < solution:
        return(estimation, max)

    elif estimation - solution:
        return(min, estimation)

    else:
        return(estimation, estimation)

# Distinct function initiating the user number entry research
def recherche(estimation, solution, min, max):

    while min != max:

        print("%d? ..." % estimation)
        (min, max) = comparaison(estimation, solution, min, max)

        split_dif = int(min + (max - min) / 2)

        if estimation == split_dif:
            estimation = split_dif + 1

        else:
            estimation = split_dif

    return min

# Welcoming message from ui
print("Hello! Je vais deviner un nombre entre 1 et 100 en moins d'une seconde. Vous Jouez ?!")

# Handle the rehearsing to keep the number search and errors like non int inputs or number out scope
while True:
    solution = input("Entrez le nombre de votre choix! ")

    try:
        solution = int(solution)

        if solution < 1 or solution > 100:
            print("Ma vision est étendue entre 1 et 100. Attention!")
        else:
            break

    except ValueError:
        print("Ce doit être un nombre :)))")

# estimation intiated to a random number between 1 and 100
estimation = random.randrange(1, 101)

# r or the result of inner scope the research
r = recherche(estimation, solution, 1, 100)

# The user number is given the interface. Loop is over
print("Votre nombre est bien %d, n'est ce pas?!" % r)



