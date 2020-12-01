from connexion import Connexion
from joueur import Joueur
from interface import Interface
from gameplay import Gameplay
import tkinter as tk



def main():
    fenetre_joueur = Interface()
    fenetre_joueur.nombre_joueurs()
    fenetre_joueur.mainloop()

    liste_joueurs = Joueur.liste_joueurs
    Gameplay(liste_joueurs)


main()