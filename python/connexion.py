import mysql.connector as mysql
from question import Question


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
            cls.cursor.execute(f"SELECT libelle_question, difficulte_question, nom_theme FROM questions JOIN theme on questions.theme_question = theme.id_theme WHERE id_question = {i}")
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
        cls.fermer_connexion()
        return themes

    @classmethod
    def sauvegarder_score(cls, joueurs):
        cls.ouvrir_connexion()
        for joueur in joueurs:
            cls.cursor.execute(f"INSERT INTO joueurs VALUES (NULL, '{joueur.nom}', {joueur.points}, '{joueur.couleur}')")
            cls.link.commit()
        cls.fermer_connexion()
        print('Réussi')

    @classmethod
    def effacer_score(cls):
        cls.ouvrir_connexion()
        cls.cursor.execute("TRUNCATE TABLE joueurs")
        cls.fermer_connexion()

