from connexion import Connexion
from joueur import Joueur
from question import Question
from interface import Interface
from gameplay import Gameplay
import tkinter as tk
import random

def main():
    fenetre_joueur = Interface()
    fenetre_joueur.nombre_joueurs()
    fenetre_joueur.mainloop()

    liste_joueurs = Joueur.liste_joueurs
    trivial = Gameplay()

    for joueur in liste_joueurs:
        print(joueur.nom)
        question = trivial.tirer_question('Ethique', 1)
        fenetre_jeu = Interface()
        fenetre_jeu.afficher_question(question)
        fenetre_jeu.mainloop()

main()

