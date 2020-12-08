class Error(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'Erreur, {0} '.format(self.message)
        else:
            return 'Erreur.'

class BusOverloadError(Exception):
     def __init__(self, message="Le bus n'a plus de place (Trop de passagers)."):
        self.message = message
        super().__init__(self.message)

class NotEnoughTeacherError(Exception):
     def __init__(self, message="Un car ne peut pas partir s’il n’y a pas au moins un prof pour 10 lycéens maximum."):
        self.message = message
        super().__init__(self.message)

class TooMuchClassesPerBusError(Exception):
     def __init__(self, message="Il ne peut pas y avoir plus de 3 classes différentes dans un car."):
        self.message = message
        super().__init__(self.message)

class BusIsEmptyError(Exception):
     def __init__(self, message="Un car ne part pas à vide (il n’y a personne dedans)."):
        self.message = message
        super().__init__(self.message)

class StudentHasNoClassError(Exception):
     def __init__(self, message="Un lycéen a obligatoirement un nom de classe."):
        self.message = message
        super().__init__(self.message)

class MissingStudent(Exception):
     def __init__(self, message="Un car ne part pas si l’appel n’est pas fait ou si des lycéens sont absents.."):
        self.message = message
        super().__init__(self.message)