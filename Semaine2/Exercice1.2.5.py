"""
Dans le langage de programmation de votre choix :

Définir la méthode pour trouver une valeur donnée dans un arbre binaire de recherche

Écrire la méthode pour afficher l’arbre selon un parcours infixe

Écrire la méthode pour supprimer un noeud donné en distinguant trois cas :

Le noeud est une feuille -> suppression simple

Le noeud a un seul enfant -> il est remplacé par lui

Le noeud à deux enfants, on le remplace alors par le noeud le plus proche, c’est à dire le noeud le plus à droite de l’arbre gauche ou le plus à gauche de l'arbre droit.



Une autre solution consiste à définir l’arbre sur un tableau. La première case, d’indice 0, est la racine de l'arbre. Pour un noeud donné, son fils à gauche est à la position 2n+1 et son fils de droite à la position 2N+2. L'absence d'un noeud
doit être représenté par un symbole spécial (Null, undefined ... ) mais la case doit être allouée. Le père d’un noeud donné se retrouve avec l’arrondi inférieur de l’indice de n divisé par 2


Discutons en ensemble sur le forum:
https://forum.alyra.fr/t/exercice-1-2-5-explorer-un-arbre/74

souce:
https://www.enseignement.polytechnique.fr/profs/informatique/Jean-Eric.Pin/PDF/XC7.pdf

"""


class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.value = v


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.value:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def search(self, val):
        if self.root.value is not None:
            return self._search(self.root, val)

    def _search(self, node, val):
        fin = None
        if node.left is not None:
            fin = self._search(node.left, val)
        if node.right is not None and fin is None:
            fin = self._search(node.right, val)
        if val == node.value:
            fin = node
        return fin

    def shell(self):
        if self.root.value is not None:
            self._shell(self.root)

    def _shell(self, node):
        if node.left is not None:
            self._shell(node.left)
        print(node.value)
        if node.right is not None:
            self._shell(node.right)

    def remove(self, node):
        if self.root == node:
            self.root = None
        else:
            self._remove(self.root, node)

    def _remove(self, node, nodRem):
        find = False
        if node.left is not None:
            find = self._remove(node.left, nodRem)
            if find == False and node.left.value == nodRem.value:
                if node.left.left is None and node.left.right is None:
                    node.left = None
                elif node.left.left is None or node.left.right is None:
                    if node.left.left is None:
                        node.left = node.left.right
                    else:
                        node.left = node.left.left
                else:
                    nodRep = node.left.left
                    while nodRep.right is not None:
                        nodRep = nodRep.right
                    nodRep.right = node.left.right
                    node.left = nodRep
                find = True
        if node.right is not None and find == False:
            find = self._remove(node.right, nodRem)
            if find == False and node.right.value == nodRem.value:
                if node.right.left is None and node.right.right is None:
                    node.right = None
                elif node.right.left is None or node.right.right is None:
                    if node.right.left is None:
                        node.right = node.right.right
                    else:
                        node.right = node.right.left
                else:
                    nodRep = node.right.right
                    while nodRep.left is not None:
                        nodRep = nodRep.left
                    nodRep.left = node.droit.left
                    node.right = nodRep
                find = True
        return find


tree = Tree()
tree.add('Tokyo')
tree.add('Shanghai')
tree.add('San Francisco')
tree.add('Rio')
tree.add('London')
tree.add('Paris')
print('Arbre initial')
tree.shell()
print('Le noeud Shanghai trouvé a deux enfants, soit Rio et Paris en suivant un parcours infixe')
node = tree.search('Shanghai')
tree.remove(node)
tree.shell()
print('Le noeud Rio a dès lors un seul enfant San Francisco, qui le remplace.')
node = tree.search('Rio')
tree.remove(node)
tree.shell()
print('San Francisco est une feuille. La suppression est simple')
node = tree.search('San Francisco')
tree.remove(node)
tree.shell()

