"""
Exercice optionnel : Explorer un arbre en utilisant un tableau
Exercice 1.2.6 (optionnel)

Écrire une implémentation d'un arbre binaire de recherche utilisant un tableau

Discutons en ensemble sur le forum:

https://forum.alyra.fr/t/exercice-optionnel-explorer-un-arbre-en-utilisant-un-tableau/75
"""


class Tree:
    def __init__(self, maxVal=100):
        self.tree = [None] * maxVal

    def add(self, val):
        if self.tree[0] is None:
            self.tree[0] = val
        else:
            self._add(val, 0)

    def _add(self, val, N):
        if val < self.tree[N]:
            if self.tree[2 * N + 1] is not None:
                self._add(val, 2*N+1)
            else:
                ancre = 2*N+1
                self.tree[ancre] = val

        else:
            if self.tree[2 * N + 2] is not None:
                self._add(val, 2*N+2)
            else:
                ancre = 2*N+2
                self.tree[ancre] = val

    def remove(self, val):
        if self.tree[0] == val:
            self.tree[0] is None
        else:
            self._remove(val, 0)

    def _remove(self, val, N):
        if val < self.tree[N]:
            if self.tree[2*N+1] is not None:
                self._remove(val, 2*N+1)
            else:
                undefined = (2*N+1)/2
                self.tree[2*N+1] = undefined

        else:
            if self.tree[2*N+2] is not None:
                self._remove(val, 2*N+2)
            else:
                undefined = (2*N+2)/2
                self.tree[2*N+2] = undefined


    def infixMap(self):
        print("Parcours Infixe : ")
        if self.tree[0] is not None:
            self._infixMap(0)

    def _infixMap(self, N, depth=1):
        if self.tree[2 * N + 1] is not None:
            self._infixMap(2*N+1, depth + 1)

        print("Node: " + str(self.tree[N]) + ' / expended to : ' + str(depth))
        
        if self.tree[2 * N + 2] is not None:
            self._infixMap(2*N+2, depth + 1)

        print(self.tree[2*N+2])


def main():
    print("\n")
    tree = Tree()
    tree.add(15)

    tree.add(28)
    tree.add(14)
    tree.add(5)
    tree.add(48)
    tree.add(22)
    tree.add(33)

    tree.infixMap()
    print("\n")

    tree.remove(14)

    tree.infixMap()
    print("\n")

    print()
main()


