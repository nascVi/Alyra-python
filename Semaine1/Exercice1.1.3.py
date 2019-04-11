def estpalindrome( s ):

    s = s.replace(" ", "").lower()

    i = 0
    j = len(s) - 1

    while i < j:

        if s[i] != s[j]:

            return False

        i+=1
        j-=1

    return True


M = input("Entrez un palindrome (ou pas)\n")

if estpalindrome( M ):

    print("C'est un palindrome !")

else:

    print("Ce n'est pas un palindrome !")


