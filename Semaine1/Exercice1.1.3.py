def estPalindrome( s ):
    s = s.replace(' ', '')
    return s == s [::-1]


M = input( "Checkez si palindrome \n " )

if estPalindrome( M ):

    print( "Est un palindrome !" )

else:

    print( "N'est pas palindrome !" )
