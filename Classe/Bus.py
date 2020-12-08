class Bus():
    def __init__(self, referent, limite):
        self.referent = referent
        self.limite = limite
        self.classes = []
        self.eleves = []

    def add(self, eleve):
        self.eleves.append(eleve)
