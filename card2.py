"""
Module card2.

Definit une classe Card et un petit cas-test qui demontre son utilite.

TODO:
OK  - coder la fonction str
OK  - le init qui prend 0 ou 2 parametres (indication : chercher sur StackOverflow "python optional arguments in initializer of python class")
  - coder points ; d'ailleurs, est-ce une fonction ou un attribut ?
  - corriger le bug : qui est que le 10 est plus fort que Dame Roi Valet (7 8 9 V D R 10 As)
  - bonus : ajouter les atouts
  - bonus : ajouter un setter qui empeche couleur = "VERTE"
"""
valeur_sign={7:"7",8:"8",9:"9",10:"10",11:"Valet",12:"Dame",13:"Roi",14:"As"}

COEUR, CARREAU, PIQUE, TREFLE = (0, 1, 2, 3)
#valeur : 7, 8, 9, 10, 11, 12, 13, 14

class Card:
    def __init__(self, couleur=None, valeur=None): #les paramètres non renseignés vaudront none
        self.couleur = couleur
        self.valeur = valeur
        self.points = 0
#PAS TOUCHE A CETTE LIGNE
    def __str__(self):
        if self.couleur == 0:
            s = "COEUR"
        elif self.couleur == 1:
            s = "CARREAU"
        elif self.couleur == 2:
            s = "PIQUE"
        elif self.couleur == 3:
            s = "TREFLE"
        return s

    def calcul_points(self):
        if self.valeur in [7,8,9]:
            self.points = 0
        elif self.valeur==10:
            self.points = 10
        elif self.valeur==11:
            self.points = 2
        elif self.valeur==12:
            self.points = 3
        elif self.valeur==13:
            self.points = 4
        elif self.valeur==14:
            self.points = 11


# card1 = Card(10, COEUR)

card1 = Card()
card1.couleur = COEUR
card1.valeur = 10
card1.calcul_points()
# card1.couleur = "VERTE"


card2 = Card()
card2.valeur = 9
card2.couleur = TREFLE
card2.calcul_points()
#
print("Le joueur 1 joue la carte", card1)
print("Le joueur 2 joue la carte", card2)
print("qui a la meilleure carte ?")

## maintenant on compare des cartes
# atout ?

if card1.couleur == card2.couleur:
    if card1.points > card2.points :
        print("C'est J1 qui gagne avec", card1)
    else:
        print("C'est J2 qui gagne avec", card2)
else:
    print("Error : Il manque le cas atout")


print("Et va vaut ", card1.points + card2.points)

## test perso

