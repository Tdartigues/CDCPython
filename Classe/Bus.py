class Bus():
    def __init__(self, nom, referent, limite):
        self.nom = nom
        self.referent = referent
        self.limite = limite
        self.classes = []
        self.eleves = []

    def add(self, eleve):
        self.eleves.append(eleve)
