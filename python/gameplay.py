from connexion import Connexion
from joueur import Joueur
from question import Question
from interface import Interface
import random


class Gameplay:
    def __init__(self, joueurs):
        self.tour = True
        self.joueurs = joueurs
        self.themes = ['Ethique']
        self.questions = Connexion.get_questions()
        self.lancer_jeu()

    def tirer_question(self, theme, difficulte):
        for question in self.questions:
            if question.theme == theme and question.difficulte == difficulte:
                self.questions.remove(question)
                return question

    def lancer_jeu(self):
        while len(self.questions) > 0:
            print("Debut du jeu!")
            for joueur in self.joueurs:
                print("A toi:", joueur.nom)
                while True:
                    if joueur.points == 2:
                        print(joueur.nom, "a gagné")
                        return
                    else:
                        theme = random.choice(self.themes)
                        question = self.tirer_question(theme, 1)
                        fenetre_jeu = Interface()
                        fenetre_jeu.afficher_question(question)
                        fenetre_jeu.mainloop()
                        if fenetre_jeu.choix_reponse == True:
                            joueur.points += 1
                            print("Tu as:", joueur.points, "points!")
                        else:
                            break