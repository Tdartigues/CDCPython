class Ecole():
    def __init__(self, nom):
        self.nom = nom
        self.classes = []
        self.professeurs = []

    def add_classe(self, classe):
        self.classes.append(classe)

    def add_professeur(self, professeur):
        self.professeurs.append(professeur)
