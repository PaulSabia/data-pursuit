class Joueur:
    def __init__(self, nom, couleur):
        self.nom = nom
        self.points = 0
        self.couleur = couleur

    def ajouter_points(self, points):
        self.points += points

    def retirer_points(self, points):
        self.points -= points
