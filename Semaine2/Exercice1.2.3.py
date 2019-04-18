'''
Exercices Optionnels : Ecrire un algorithme
Exercice 1.2.3
Écrire un algorithme récursif de la fonction factorielle js, plus efficace que la version naïve ci-dessous

__

 function factorielRecursifNaif(n){
    if(n === 0) {
        return 1
    } else {
        return n * factorielRecursifNaif(n-1)
    }
 }

__
view rawfactorielRecursifNaif.js hosted with ❤ by GitHub

__
Pour aller plus loin
Il existe des algorithmes encore plus rapide des factorielles, notamment à partir de la décomposition en nombre premiers de n :

http://www.cecm.sfu.ca/personal/pborwein/PAPERS/P29.pdf

http://www.cs.berkeley.edu/~fateman/papers/factorial.pdf

https://gmplib.org/manual/Factorial-Algorithm.html

https://oeis.org/A000142/a000142.pdf
'''


def nivRecuFactorial(n):
    if n == 0:
        return 1
    else:
        return n * nivRecuFactorial(n-1)


def recuFactorial(n, initCall=True, pw=1):
    if n == 0:
        return 1
    elif n == 2:
        if initCall == True:
            return 2**pw
        return 1
    elif n % 2 == 0:
        if n > 4 and initCall == True:
            return recuFactorial(n-1, False, pw + int(n/2)) * recuFactorial(int(n/2), True, pw + int(n/2))
        elif n == 4:
            return recuFactorial(n-1, initCall, pw + 2)
        else:
            return recuFactorial(n-1, initCall, pw)
    else:
        return n * recuFactorial(n-1, initCall, pw)


def main():
    
    print("\n CALCULE DE LA FACTORIELLE D'UN ENTIER NATUREL")

    try:
        X = -1     
        while X < 0:
            X = input("\nVotre nombre doit être positif: ")
            X = int(X)
                        
        print("\nLa factorielle de " + str(X) + " est : " + str(recuFactorial(X)) + "\n")
    
    except ValueError:
        print("\n Saisie incorrecte ... \n")

main()
