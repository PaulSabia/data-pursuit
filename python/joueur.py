import random

class Joueur:
    def __init__(self, nom, couleur):
        self.nom = nom
        self.points = 0
        self.couleur = couleur

    def ajouter_points(self, points):
        self.points += points

    def retirer_points(self, points):
        self.points -= points

    def jeter_des(self):
        des = random.randint(1,6)
        return des

def liste_joueurs():
    i=1
    joueur = list()
    finie = False
    Connexion.ouvrir_connexion(bdd)
    bdd.cursor.execute("""UPDATE `joueurs` SET `points_joueur`=0""")
    while !finie:
        joueur.append(input('Entrer le nom du joueur ' + i))
        present = False
        bdd.cursor.execute("""SELECT `nom_joueur` FROM `joueurs`""")
        lignes = bdd.cursor.fetchall()
        for ligne in lignes:
            if joueur[i-1] == ligne[0]:
                reference = (joueur[i-1],)
                present = True
            else:
                reference = (joueur[i-1], 0, NULL, 0)
                bdd.cursor.execute("""INSERT INTO Produits (`nom_joueur`, `points_joueur`, `couleur_joueur`, `record_joueur`) VALUES(%s, %s, %s, %s)""", reference)
    bdd.link.commit()
    Connexion.fermer_connexion(bdd)
    return joueur
