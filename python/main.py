from connexion import Connexion
from joueur import Joueur
from question import Question
from interface import Interface
from gameplay import Gameplay
import tkinter as tk
import random

def main():
    #On créer la fenêtre de jeu
    fenetre_joueur = Interface()
    fenetre_joueur.nombre_joueurs()
    fenetre_joueur.mainloop()

    liste_joueurs = Joueur.liste_joueurs

    fenetre_jeu = Interface()

    Gameplay(fenetre_jeu, liste_joueurs)

    fenetre_jeu.mainloop()

main()

