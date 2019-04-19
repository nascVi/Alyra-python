'''
On étudie des offres d’achat/vente dans une plateforme d'échange de cryptocurrencies.

On y trouve les ordres (en attente) suivants:

84 Doge -> 32 LTC (1 Doge = 0.381 LTC)

29 Doge -> 80 ETH (1 Doge = 2.75 ETH)

300 ETH ->  62 BTC (1 ETH = 0.206 BTC)

288 LTC -> 2304 ETH (1 LTC = 8 ETH)

27 BTC -> 46 Doge (1 BTC = 1.7 Doge)

33 BTC -> 16 LTC (1 BTC = 0.48 LTC)

Il est parfois possible, dans un marché non régulé, d’échanger un montant d’une crypto A contre une crypto B, puis d’échanger ce résultat contre une Crypto C, et de continuer jusqu’a revenir à la crypto A. Parfois, quand on à de la chance, ou un bon algorithme, on gagne de l’argent.

Recherchez une méthode à partir des taux ci-dessus pour détecter les gains potentiels.

Discutons en ensemble sur le forum:
https://forum.alyra.fr/t/exercices-optionnels-ecrire-un-algorithme/73
'''

from itertools import permutations

deals = [
            [['Doge', 84],['LTC', 32],0.381],
            [['Doge', 29],['ETH', 80],2.75],
            [['ETH', 300],['BTC', 62],0.206],
            [['LTC', 288],['ETH', 2304],8],
            [['BTC', 27],['Doge', 46],1.7],
            [['BTC', 33],['LTC', 16],0.48],                                    
         ]

matchableD = []
for i in range(3, len(deals)+1):
    for xchange in permutations(deals, i):
        positiveX = True
        
        # None corresponding from a currency to another after an exhange
        if xchange[0][0][0] != xchange[-1][1][0]:
            continue
        
        for j in range(0,len(xchange)-1):
            
            # None corresponding money to exchange handle
            if xchange[j][1][0] != xchange[j+1][0][0]:
                positiveX = False
                break
        
        if positiveX:
            matchableD.append(xchange)

for deal in matchableD:
    print(str(deal))