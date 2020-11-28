from connexion import Connexion
from joueur import Joueur
from question import Question
from interface import Interface
from gameplay import Gameplay
import tkinter as tk
import random

def main():
    # On récupère les questions dans la BDD
    questions = Connexion.get_questions()
    # On mélange les questions
    random.shuffle(questions)

    #On créer la fenêtre de jeu
    window = tk.Tk()
    #On charge notre interface dans la fenêtre
    plateau = Interface(window)

    #On initialise notre gameplay
    jeu = Gameplay()

    #On lance le jeu
    while jeu.fin_jeu == False:
        question = jeu.tirer_question(questions, 'Ethique', 1)
        plateau.afficher_question(question)
        jeu.fin_jeu = True

    window.mainloop()
    liste_joueurs = Joueur.liste_joueurs
    print(liste_joueurs)

main()
