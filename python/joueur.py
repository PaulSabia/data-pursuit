class Joueur:
    liste_joueurs = []

    def __init__(self, nom, couleur):
        self.nom = nom
        self.points = set()
        self.couleur = couleur
        self.liste_joueurs.append(self)

    def __str__(self):
        return self.nom

    def ajouter_points(self, theme):
        self.points.add(theme)
    