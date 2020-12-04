import mysql.connector as mysql
from question import Question, Theme


class Connexion:

    @classmethod
    def ouvrir_connexion(cls):
        cls.link = mysql.connect(
            user='root', password='root', host='localhost', port="8081", database='trivial')
        cls.cursor = cls.link.cursor()

    @classmethod
    def fermer_connexion(cls):
        cls.cursor.close()
        cls.link.close()

    @classmethod
    def get_questions(cls):
        cls.ouvrir_connexion()
        cls.cursor.execute("SELECT id_question from questions")
        ids = [item[0] for item in cls.cursor.fetchall()]
        questions = []
        for i in ids:
            cls.cursor.execute(f"SELECT libelle_question, difficulte_question, nom_theme FROM questions JOIN themes on questions.theme_question = themes.id_theme WHERE id_question = {i}")
            question = cls.cursor.fetchone()
            cls.cursor.execute(f"SELECT libelle_reponse, valeur_reponse FROM reponses WHERE id_question = {i}")
            reponses = cls.cursor.fetchall()

            objet = Question(question[0], reponses, question[1], question[2])
            questions.append(objet)
        cls.fermer_connexion()
        return questions

    @classmethod
    def get_themes(cls):
        cls.ouvrir_connexion()
        cls.cursor.execute("SELECT nom_theme from themes")
        themes = cls.cursor.fetchall()
        liste_themes = []
        for i in themes:
            theme = Theme(i)
            liste_themes.append(theme)
        cls.fermer_connexion()
        return liste_themes