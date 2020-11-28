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
                         fg='Black', bg='Gray', text="Trivial Data")
        label.pack(fill='x', side='top')

        self.frame_joueurs = tk.Frame(self.master, bg='Gray')
        self.frame_joueurs.pack(pady=75)

        self.frame_question = tk.Frame(self.master, bg='Gray')
        self.frame_question.pack()

        self.nombre_joueurs()

    def nombre_joueurs(self):
        self.label_nombre_joueur = tk.Label(self.frame_joueurs, text="Entrez le nombre de joueurs", font=('Helvetica', '20'), bg='Gray')
        self.label_nombre_joueur.grid(row=0, columnspan=4, padx=10, ipady=50)
        
        for i in range(1, 5):
            self.entry_nbr_joueur = tk.Button(self.frame_joueurs, height=2, width=13, bg='White', bd=0, font=('Helvetica', '11'), text=i, command=lambda i=i: self.saisir_joueurs(i))
            self.entry_nbr_joueur.grid(row=1, column=i-1, padx=10, ipadx=10)



    def saisir_joueurs(self, nombre):
        for widget in self.frame_joueurs.winfo_children():
            widget.grid_forget()

        self.liste_couleur = ['red', 'blue', 'yellow', 'green']
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
            self.menu_couleur = ttk.Combobox(self.frame_joueurs, values=self.liste_couleur, postcommand=postcommande, width=25, state="readonly")
            commande = partial(self.confirmer, w)
            self.menu_couleur.set('Choisir une couleur')
            self.menu_couleur.bind('<<ComboboxSelected>>', commande) 
            self.menu_couleur.grid(row=2, column=w, padx=10)
            self.liste_combobox.append(self.menu_couleur)

        bouton_joueur = tk.Button(self.frame_joueurs, text='Jouer', height=2, width=25, bg='White', bd=0, font=('Helvetica', '11'), command=self.fin_entree_joueur)
        bouton_joueur.grid(row=3, columnspan=nombre, pady=(150, 0))         

    def update_couleur(self, w):
        combobox = self.liste_combobox[w]
        combobox.configure(values=self.liste_couleur)

    def confirmer(self, w, *args):
        combobox = self.liste_combobox[w]
        couleur_joueur = combobox.get()
        self.liste_couleur.remove(couleur_joueur)


    def fin_entree_joueur(self):
        for w in range(len(self.liste_entry)):
            entry = self.liste_entry[w]
            nom_joueur = entry.get()
            combobox = self.liste_combobox[w]
            couleur_joueur = combobox.get()
            objet = Joueur(nom_joueur, couleur_joueur)
            self.liste_joueur.append(objet)
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
