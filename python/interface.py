import tkinter as tk
from tkinter import ttk
from functools import partial
from joueur import Joueur
from connexion import Connexion


class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Trivial Data")
        self.master.geometry('900x600')
        self.master.minsize(900, 600)
        self.master.configure(bg='Gray')

        label = tk.Label(self.master, font=('Helvetica', '50'),
                         fg='Blue', bg='Gray', text="Trivial Data")
        label.pack(fill='x', side='top')

        self.frame_joueurs = tk.Frame(self.master)
        self.frame_joueurs.pack()

        self.frame_question = tk.Frame(self.master, bg='Gray')
        self.frame_question.pack(pady=25)

        self.joueurs()

    def joueurs(self):
        self.label_nombre_joueur = tk.Label(self.frame_joueurs, text="Entrez le nombre de joueurs")
        self.label_nombre_joueur.pack()
        self.entry_nbr_joueur = tk.Entry(self.frame_joueurs)
        self.entry_nbr_joueur.pack()
        self.bouton_commencer = tk.Button(self.frame_joueurs, text="Commencer", command=self.entree_joueur)
        self.bouton_commencer.pack()

    def entree_joueur(self):
        
        self.label_nombre_joueur.pack_forget()
        self.entry_nbr_joueur.pack_forget()
        self.bouton_commencer.pack_forget()
        self.liste_couleur = ['red', 'blue', 'yellow', 'green']
        self.liste_joueur = []
        self.liste_bouton = []
        self.liste_entry = []
        self.liste_combobox = []
        nbr_joueur = int(self.entry_nbr_joueur.get())
        for w in range(nbr_joueur):
            label_joueur = tk.Label(self.frame_joueurs, text=f"Joueur {w+1}")
            label_joueur.pack()
            self.entry_joueur = tk.Entry(self.frame_joueurs)
            self.entry_joueur.pack()
            self.liste_entry.append(self.entry_joueur)
            postcommande = partial(self.update_couleur, w)
            self.menu_couleur = ttk.Combobox(self.frame_joueurs, values=self.liste_couleur, postcommand=postcommande, state="readonly") 
            self.menu_couleur.pack()
            self.liste_combobox.append(self.menu_couleur)
            commande = partial(self.confirmer, w)
            self.bouton_confirmation = tk.Button(self.frame_joueurs, text='Selectionner', command=commande)
            self.bouton_confirmation.pack()
            self.liste_bouton.append(self.bouton_confirmation)

        bouton_joueur = tk.Button(self.frame_joueurs, text='Jouer', command=self.fin_entree_joueur)
        bouton_joueur.pack()         

    def update_couleur(self, w):
        combobox = self.liste_combobox[w]
        combobox.configure(values=self.liste_couleur)

    def confirmer(self, w):
        try:
            entry = self.liste_entry[w]
            nom_joueur = entry.get()
            combobox = self.liste_combobox[w]
            couleur_joueur = combobox.get()
            self.liste_couleur.remove(couleur_joueur)
            objet = Joueur(nom_joueur, couleur_joueur)
            self.liste_joueur.append(objet)
        except:
            print('Joueur déjà sélectionné !')

    def fin_entree_joueur(self):
        print(self.liste_joueur)
        self.frame_joueurs.destroy()
        

    def afficher_question(self, question):
        libelle = question.libelle
        self.label_question = tk.Label(
            self.frame_question, text=libelle, bg='Gray', bd=0, font=('Helvetica', '20'))
        self.label_question.grid(row=0, columnspan=4, padx=10, ipady=50)

        reponses = question.reponses
        if len(reponses) > 1:
            for i in range(len(reponses)):
                commande = partial(self.check_reponse, reponses[i][1])
                boutton_reponse = tk.Button(self.frame_question, height=2, width=13, bg='White', bd=0, font=(
                    'Helvetica', '11'), text=reponses[i][0], command=commande)
                boutton_reponse.grid(row=1, column=i, padx=10, ipadx=10)
        else:
            self.entree_reponse = tk.Entry(
                self.frame_question, bg='white', width=20, justify='center', font=('Helvetica', '10'))
            self.entree_reponse.grid(row=1, columnspan=4, pady=50)
            boutton_reponse = tk.Button(self.frame_question, height=2, width=13, bg='White', bd=0, font=(
                'Helvetica', '11'), text='Valider', command=lambda: self.check_reponse_string(self.entree_reponse.get(), reponses[0][0]))
            boutton_reponse.grid(row=2, columnspan=4, padx=10, ipadx=10)

    def check_reponse(self, choix):
        if choix == 1:
            print("Bonne réponse")
            self.frame_question.configure(bg="Green")
            self.label_question.configure(bg="Green")
        else:
            print("Raté, la réponse est fausse")
            self.frame_question.configure(bg="Red")
            self.label_question.configure(bg="Red")

    def check_reponse_string(self, saisie, reponse):
        if saisie == reponse:
            print("Bonne réponse")
            self.frame_question.configure(bg="Green")
            self.label_question.configure(bg="Green")
        else:
            print("Raté, la réponse est fausse")
            self.frame_question.configure(bg="Red")
            self.label_question.configure(bg="Red")
