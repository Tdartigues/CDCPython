from CDCPython.Classe.Personne import Personne


class Etudiant(Personne):
    def __init__(self, nom, prenom, classe):
        super().__init__(nom, prenom)
        self.classe = classe
