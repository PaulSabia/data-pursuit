from connexion import Connexion
from joueur import Joueur
from question import Question, Theme
from interface import Interface
import random


class Gameplay:
    def __init__(self, joueurs):
        self.fin_jeu = False
        self.joueurs = joueurs
        self.themes = Connexion.get_themes()
        # self.themes = [Theme('IA'), Theme('Ethique'), Theme('Python')]
        self.questions = Connexion.get_questions()
        self.questions = self.questions * 5
        if len(self.joueurs) > 0:
            self.lancer_jeu()

    def lancer_jeu(self):
        while self.fin_jeu == False:
            for joueur in self.joueurs:
                while self.fin_jeu == False:
                    if len(joueur.points) == 3:
                        self.joueurs.sort(key=lambda x: len(x.points), reverse=True)
                        for i in self.joueurs:
                            print(i.nom, i.points)
                        self.victoire(joueur)
                        return
                    else:
                        theme = random.choice(self.themes)
                        difficulte = self.get_difficulte(len(joueur.points))
                        question = self.tirer_question(theme.nom, difficulte)
                        fenetre_jeu = Interface()
                        fenetre_jeu.afficher_question(self, question, joueur, self.joueurs)
                        fenetre_jeu.mainloop()
                        if fenetre_jeu.choix_reponse == True:
                            joueur.ajouter_points(theme)
                        else:
                            break

    def tirer_question(self, theme, difficulte):
        random.shuffle(self.questions)
        for question in self.questions:
            if question.theme == theme and question.difficulte == difficulte:
                self.questions.remove(question)
                return question

    #=====Christelle=====
    def get_difficulte(self, points):
        if points < 2:
            return  1
        elif points <3:
            return 2
        else :
            return 3
        # return 1
    #=====================

    def victoire(self, joueur):
        fenetre_victoire = Interface()
        fenetre_victoire.ecran_victoire(joueur, self.joueurs, self.themes)
        fenetre_victoire.mainloop()