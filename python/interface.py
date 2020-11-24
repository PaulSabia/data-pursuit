import tkinter as tk
from functools import partial


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

        self.frame_question = tk.Frame(self.master, bg='Gray')
        self.frame_question.pack(pady=25)

    def afficher_question(self, question):
        libelle = question.libelle
        label_question = tk.Label(
            self.frame_question, text=libelle, bg='Gray', bd=0, font=('Helvetica', '20'))
        label_question.grid(row=0, columnspan=4, padx=10, ipady=50)

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
        else:
            print("Raté, la réponse est fausse")

    def check_reponse_string(self, saisie, reponse):
        if saisie == reponse:
            print("Bonne réponse")
        else:
            print("Raté, la réponse est fausse")
