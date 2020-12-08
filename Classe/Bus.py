from .Error import *


class Bus():
    def __init__(self, referent, limite):
        self.referent = referent
        self.limite = limite
        self.classes = []
        self.eleves = []
        self.professeurs = []

    def add(self, person, isStudent):
        if isStudent :
            

        if (len(self.eleves) + len(self.professeurs)) < self.limite:
            if len(self.classes) > 3:
                raise TooMuchClassesPerBusError
            else:
                if isStudent :
                    self.eleves.append(person)
                else : 
                    self.professeurs.append(person)
        else:
            raise BusOverloadError

    def start(self):
        for e in eleves:
            if self.classes.count(e.classe) == 0 :
                if len(self.classes) > 2:
                    self.classes.clear
                    raise TooMuchClassesPerBusError
                else:
                    self.classes.append(e.classe)

        for classe in self.classes:
            if len(classe) > 0:
                pass
            else:
                raise BusIsEmptyError
        if (len(self.professeurs) * 10 >= len(self.eleves)):
            raise NotEnoughTeacherError
        
        print("On est partie")
