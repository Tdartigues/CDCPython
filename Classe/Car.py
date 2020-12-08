import Error

class Car():
    def __init__(self, nom, referent, limite):
        self.nom = nom
        self.referent = referent
        self.limite = limite
        self.classes = []
        self.eleves = []
        self.professeurs = []

    def ajout(self, eleve):
        if (len(self.eleves) < self.limite):
            if len(self.classes) > 2:
                raise Error.TooMuchClassesPerBusError
            else:
                self.eleves.append(eleve)
        else:
            raise Error.BusOverloadError

    def start(self):
        for classe in self.classes:
            if (len(classe) > 0):
                pass
            else:
                raise Error.BusIsEmptyError
        if ((len(self.professeurs) * 10 >= len(self.eleves))):
            raise Error.NotEnoughTeacherError