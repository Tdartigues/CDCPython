class Classe():
    def __init__(self, nom, limite):
        self.nom = nom
        self.limite = limite
        self.eleves = []

    def add(self, eleve):
        self.eleves.append(eleve)
