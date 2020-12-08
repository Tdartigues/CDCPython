from CDCPython.Classe.Personne import Personne


class Professeur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
