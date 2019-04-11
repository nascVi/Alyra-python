def estPalindrome( s ):

    s = s.replace(' ', '').lower()
    return s == s [::-1]

    i = 0
    j = len(s) - 1

    while i < j:

        if s[i] != s[j]:

            return False

        i+=1
        j-=1

    return True


M = input( "Checkez si palindrome \n " )

if estPalindrome( M ):

    print( "Est un palindrome !" )

else:

    print( "N'est pas palindrome !" )
