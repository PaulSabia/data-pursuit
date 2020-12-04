import tkinter as tk
from tkinter import ttk
from functools import partial
from joueur import Joueur
from connexion import Connexion


class Interface(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Trivial Data")
        self.geometry('1080x600')
        self.minsize(1080, 600)
        self.configure(bg='Gray')

        label = tk.Label(self, font=('Helvetica', '50'), fg='Black', bg='Gray', text="Trivial Data")
        label.pack(fill='x', side='top')

        self.choix_reponse = None

    def nombre_joueurs(self):
        self.frame_joueurs = tk.Frame(self, bg='Gray')
        self.frame_joueurs.pack()
        
        self.label_nombre_joueur = tk.Label(self.frame_joueurs, text="Entrez le nombre de joueurs", font=('Helvetica', '20'), bg='Gray')
        self.label_nombre_joueur.grid(row=0, columnspan=4, padx=10, ipady=50)
        
        for i in range(1, 5):
            self.entry_nbr_joueur = tk.Button(self.frame_joueurs, height=2, width=13, bg='White', bd=0, font=('Helvetica', '11'), text=i, command=lambda i=i: self.saisir_joueurs(i))
            self.entry_nbr_joueur.grid(row=1, column=i-1, padx=10, ipadx=10)

    def saisir_joueurs(self, nombre):
        for widget in self.frame_joueurs.winfo_children():
            widget.grid_forget()

        self.couleurs = {'Rouge': '#F44336', 'Bleu': '#03A9F4', 'Vert': '#4CAF50', 'Jaune': '#FFEB3B',
             'Mauve': '#7E57C2', 'Rose': '#EC407A'}
        self.liste_couleurs = list(self.couleurs.keys())
        self.liste_joueur = []
        self.liste_entry = []
        self.liste_combobox = []
        
        for w in range(nombre):
            label_joueur = tk.Label(self.frame_joueurs, text=f"Joueur {w+1}", bg='Gray')
            label_joueur.grid(row=0, column=w, padx=10)

            self.entry_joueur = tk.Entry(self.frame_joueurs, width=28)
            self.entry_joueur.grid(row=1, column=w, padx=10)
            self.liste_entry.append(self.entry_joueur)

            postcommande = partial(self.update_couleur, w)
            self.menu_couleur = ttk.Combobox(self.frame_joueurs, values=self.liste_couleurs, postcommand=postcommande, width=25, state="readonly")
            commande = partial(self.confirmer, w)

            self.menu_couleur.set('Choisir une couleur')
            self.menu_couleur.bind('<<ComboboxSelected>>', commande) 
            self.menu_couleur.grid(row=2, column=w, padx=10)
            self.liste_combobox.append(self.menu_couleur)

        bouton_joueur = tk.Button(self.frame_joueurs, text='Jouer', height=2, width=25, bg='White', bd=0, font=('Helvetica', '11'), command=self.fin_entree_joueur)
        bouton_joueur.grid(row=3, columnspan=nombre, pady=(150, 0))         

    def update_couleur(self, w):
        combobox = self.liste_combobox[w]
        combobox.configure(values=self.liste_couleurs)

    def confirmer(self, w, *args):
        combobox = self.liste_combobox[w]
        couleur_joueur = combobox.get()
        self.liste_couleurs.remove(couleur_joueur)

    def fin_entree_joueur(self):
        for w in range(len(self.liste_entry)):
            entry = self.liste_entry[w]
            nom_joueur = entry.get()
            combobox = self.liste_combobox[w]
            couleur_joueur = combobox.get()
            objet = Joueur(nom_joueur, self.couleurs[couleur_joueur])
            self.liste_joueur.append(objet)
        self.destroy()


    def afficher_question(self, gameplay, question, joueur, liste_joueurs):
        self.info_question = tk.Frame(self, bg='Gray')
        self.info_question.pack(pady=50)
        
        self.label_joueur = tk.Label(self.info_question, text="C'est au tour de " + joueur.nom, bg='Gray', bd=0, font=('Helvetica', '20'))
        self.label_joueur.grid(rowspan=2, column=0)
        self.theme_question = tk.Label(self.info_question, text="Theme: " + question.theme, bg='Gray', bd=0, font=('Helvetica', '12'))
        self.theme_question.grid(row=0, column=1, padx=50)
        self.difficulte_question = tk.Label(self.info_question, text="Difficulté: " + str(question.difficulte), bg='Gray', bd=0, font=('Helvetica', '12'))
        self.difficulte_question.grid(row=1, column=1, padx=50)

        self.frame_question = tk.Frame(self, bg='Gray')
        self.frame_question.pack()

        text_question = self.check_lenght(question.libelle)

        self.label_question = tk.Label(self.frame_question, text=text_question, bg='Gray', bd=0, font=('Helvetica', '15'))
        self.label_question.grid(row=0, columnspan=4, padx=10, ipady=50)

        reponses = question.reponses
        if len(reponses) > 1:
            for i in range(len(reponses)):
                commande = partial(self.check_reponse, reponses[i][1])
                boutton_reponse = tk.Button(self.frame_question, height=2, width=25, bg='White', bd=0, font=('Helvetica', '9'), text=reponses[i][0], command=commande)
                boutton_reponse.grid(row=1, column=i, padx=10, ipadx=10)

        else:
            self.entree_reponse = tk.Entry(self.frame_question, bg='white', width=20, justify='center', font=('Helvetica', '10'))
            self.entree_reponse.grid(row=1, columnspan=4, pady=20)
            boutton_reponse = tk.Button(self.frame_question, height=2, width=20, bg='White', bd=0, font=('Helvetica', '11'), text='Valider', command=lambda: self.check_reponse_string(self.entree_reponse.get(), reponses[0][0]))
            boutton_reponse.grid(row=2, columnspan=4, padx=10, ipadx=10)

        self.frame_score = tk.Frame(self, bg='Gray')
        self.frame_score.pack(side='bottom')

        for i, joueur in enumerate(liste_joueurs, 0):
            label_joueur_score = tk.Label(self.frame_score, text=joueur.nom, bg=f"{joueur.couleur}", height=2, width=20)
            label_joueur_score.grid(row=0, column=i)
            label_score = tk.Label(self.frame_score, text=len(joueur.points), bg=f"{joueur.couleur}", height=2, width=20)
            label_score.grid(row=1, column=i)
        
        boutton_quitter = tk.Button(self.frame_score, height=2, width=13, bg='Red', bd=0, font=('Helvetica', '11'), text='Quitter', command=lambda: [self.quitter_jeu(gameplay), gameplay.victoire(None)])
        boutton_quitter.grid(row=0, rowspan=2, column=i+1, padx=170, ipadx=10)

    def check_lenght(self, question):
        if len(question) > 100:
            question = list(question)
            moitie = len(question)//2
            for i, _ in enumerate(question[moitie-10: moitie+10], moitie-10):
                if question[i] == ' ':
                    question[i] = '\n'
                    return ''.join(question)
        else:
            return question


    def check_reponse(self, choix):
        if choix == 1:
            self.choix_reponse = True
            self.destroy()
        else:
            self.choix_reponse = False
            self.destroy()

    def check_reponse_string(self, saisie, reponse):
        if saisie.lower() == reponse.lower():
            self.choix_reponse = True
            self.destroy()
        else:
            self.choix_reponse = False
            self.destroy()

    def ecran_victoire(self, joueur_victorieux, liste_joueurs, themes):
        self.frame_tableau = tk.Frame(self, bg='Gray')
        self.frame_tableau.pack(fill='both', padx=20)
        
        self.frame_victoire = tk.Frame(self.frame_tableau, bg='Gray')
        self.frame_victoire.pack(side='left')

        if joueur_victorieux == None:
            self.label_victoire = tk.Label(self.frame_victoire, text=f"La partie a été terminée avant la fin",  bg='Gray', bd=0, font=('Helvetica', '20'))
            self.label_victoire.grid(row=0, columnspan=2, pady=30)

        else:
            self.label_victoire = tk.Label(self.frame_victoire, text=f"{joueur_victorieux.nom} à gagné la partie !!",  bg='Gray', bd=0, font=('Helvetica', '20'))
            self.label_victoire.grid(row=0, columnspan=2, pady=30)

        self.label_classement = tk.Label(self.frame_victoire, text='Classement de partie', font=('Helvetica', '20'), bg='Gray')
        self.label_classement.grid(row=1, column=0, columnspan=2, ipadx=50, ipady=10)

        self.frame_classement = tk.Frame(self.frame_victoire, bg='Gray')
        self.frame_classement.grid(row=2, column=0)

        for i, joueur in enumerate(liste_joueurs, 1):
            label_chiffre = tk.Label(self.frame_classement, text=f"{i}.", font=('Helvetica', '20'), bg='Gray')
            label_chiffre.grid(row=i, column=1, ipadx=25, ipady=10)
            label_joueur = tk.Label(self.frame_classement, text=joueur, font=('Helvetica', '20'), fg=joueur.couleur, bg='Gray')
            label_joueur.grid(row=i, column=2, ipadx=100, ipady=10)
            frame_point = tk.Frame(self.frame_classement, width=25, height=2, bg='Gray')
            frame_point.grid(row=i, column=3)
            for j, point in enumerate(joueur.points):
                label_score = tk.Label(frame_point, font=('Helvetica', '10'), bg=point.couleur, height=1, width=3)
                label_score.grid(row=i, column=j)
        
        frame_legende = tk.Frame(self.frame_tableau, width=25, height=2, bg='Gray')
        frame_legende.pack(side='right')

        for k, theme in enumerate(themes):
            theme_nom = tk.Label(frame_legende, font=('Helvetica', '15'), text=theme.nom, bg='Gray', height=2, width=15)
            theme_nom.grid(row=k, column=0)
            theme_couleur = tk.Label(frame_legende, bg=theme.couleur, height=2, width=5)
            theme_couleur.grid(row=k, column=1)


    def quitter_jeu(self, gameplay):
        gameplay.fin_jeu = True
        self.destroy()