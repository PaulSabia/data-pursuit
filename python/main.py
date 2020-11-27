from connexion import Connexion
from joueur import Joueur
from question import Question
from interface import Interface
import tkinter as tk
import random

questions = Connexion.get_questions()
random.shuffle(questions)

window = tk.Tk()
plateau = Interface(window)


def tirer_question(theme, difficulte):
    for question in questions:
        if question.theme == theme and question.difficulte == difficulte:
            questions.remove(question)
            plateau.afficher_question(question)
            break

tirer_question('Ethique', 1)

window.mainloop()
