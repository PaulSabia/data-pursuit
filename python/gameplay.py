from connexion import Connexion
from joueur import Joueur
from question import Question
from interface import Interface
import random


class Gameplay:
    def __init__(self, joueurs):
        self.fin_jeu = False
        self.joueurs = joueurs
        # self.themes = Connexion.get_themes()
        self.themes = ['Ethique', 'IA', 'Python']
        self.questions = Connexion.get_questions()
        self.questions = self.questions * 5
        if len(self.joueurs) > 0:
            self.lancer_jeu()

    def lancer_jeu(self):
        while self.fin_jeu == False:
            print("Debut du jeu!")
            for joueur in self.joueurs:
                print("A toi:", joueur.nom)
                while self.fin_jeu == False:
                    if len(joueur.points) == 5:
                        print(joueur.nom, "a gagné")
                        return
                    else:
                        theme = random.choice(self.themes)
                        difficulte = self.get_difficulte(len(joueur.points))
                        print("La difficulté est de", difficulte)
                        question = self.tirer_question(theme, difficulte)
                        fenetre_jeu = Interface()
                        fenetre_jeu.afficher_question(self, question, joueur)
                        fenetre_jeu.mainloop()
                        if fenetre_jeu.choix_reponse == True:
                            joueur.ajouter_points(theme)
                            print(joueur.points)
                        else:
                            break

    def tirer_question(self, theme, difficulte):
        for question in self.questions:
            if question.theme == theme and question.difficulte == difficulte:
                self.questions.remove(question)
                return question

    #=====Christelle=====
    def get_difficulte(self, points):
        # if points < 2:
        #     return  1
        # elif points <3:
        #     return 2
        # else :
        #     return 3
        return 1
    #=====================