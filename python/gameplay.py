class Gameplay:
    def __init__(self):
        self.fin_jeu = False

    def tirer_question(self, liste_questions, theme, difficulte):
        for question in liste_questions:
            if question.theme == theme and question.difficulte == difficulte:
                liste_questions.remove(question)
                return question