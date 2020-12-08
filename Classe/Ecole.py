class Ecole():
    def __init__(self, nom):
        self.nom = nom
        self.classes = []

    def ajout(self, classe):
        self.classes.append(classe)
