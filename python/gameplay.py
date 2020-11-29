from connexion import Connexion
from joueur import Joueur
from question import Question
import time


class Gameplay:
    def __init__(self, plateau, joueurs, *args):
        self.fin_jeu = False
        self.tour = True
        self.questions = Connexion.get_questions()
        self.plateau = plateau
        self.themes = ['Ethique']
        self.joueurs = joueurs
        self.lancer_jeu()

    def tirer_question(self, theme, difficulte):
        for question in self.questions:
            if question.theme == theme and question.difficulte == difficulte:
                self.questions.remove(question)
                return question

    def lancer_jeu(self):
        while self.fin_jeu == False:
            for joueur in self.joueurs:
                print(joueur.nom)
                self.tour_joueur(self.joueurs)
            self.fin_jeu = True
    
    def tour_joueur(self, joueur):
        question = self.tirer_question('Ethique', 1)
        self.plateau.afficher_question(question)
        self.check_reponse()

    def check_reponse(self):
        if self.plateau.choix_reponse == False:
            self.tour = False
            print("A")
        else:
            print("B")
