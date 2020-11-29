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
    window_1 = tk.Tk()
   
    #On charge notre interface dans la fenêtre
    fenetre_joueur = Interface(window_1)
    fenetre_joueur.nombre_joueurs()
    window_1.mainloop()
    liste_joueurs = Joueur.liste_joueurs
    print(liste_joueurs)


    #On initialise notre gameplay
    jeu = Gameplay()
    window_2 = tk.Tk()
    fenetre_jeu = Interface(window_2)

    #On lance le jeu
    while jeu.fin_jeu == False:
        question = jeu.tirer_question(questions, 'Ethique', 1)
        fenetre_jeu.afficher_question(question)
        jeu.fin_jeu = True

    window_2.mainloop()

main()
