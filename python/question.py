class Question:
    def __init__(self, libelle, reponses, difficulte, theme):
        self.libelle = libelle
        self.reponses = reponses
        self.difficulte = difficulte
        self.theme = theme

class Theme:
    couleurs = ['#F44336', '#03A9F4', '#4CAF50', '#FFEB3B', '#EC407A']
    
    def __init__(self, nom):
        self.nom = nom
        self.couleur = self.couleurs[0]
        self.couleurs.remove(self.couleur)