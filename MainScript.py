from Classe.Ecole import Ecole
from Classe.Classe import Classe
from Classe.Etudiant import Etudiant
from Classe.Professeur import Professeur
from Classe.Bus import Bus

#Init Ecole
ecole = Ecole("EPSI")
print(ecole.nom)
classe1 = Classe("Classe1",30)
print(classe1.nom)
ecole.add_classe(classe1)

for i in range(1,31):
    eleve = Etudiant(f"Etudiant{i}",f"Etudiant{i}",classe1.nom)
    print(eleve.nom)
    classe1.add(eleve)

classe2 = Classe("Classe2",30)
print(classe2.nom)
ecole.add_classe(classe2)

for i in range(1,21):
    eleve = Etudiant(f"Etudiant{i}",f"Etudiant{i}",classe2.nom)
    print(eleve.nom)
    classe2.add(eleve)

for i in range (1,6):
   prof = Professeur(f"Professeur{i}",f"Professeur{i}")
   ecole.add_professeur(prof)
   print(prof.nom)

#Test taille limite classe
nEleve1 = Etudiant("Dupond","Thierry",classe1)
classe1.add(nEleve1)

nEleve2 = Etudiant("Dupont","Micheline",classe2)
classe2.add(nEleve2)

#Init Bus
bus1 = Bus(ecole.professeurs[0], 50)
bus2 = Bus(ecole.professeurs[1], 50)

for e in classe1.eleves :
    bus1.add(e,True)

bus1.add(bus1.referent,False)
bus1.add(ecole.professeurs[2],False)
bus1.add(ecole.professeurs[3],False)

for e in classe2.eleves :
    bus2.add(e,True)

bus2.add(bus2.referent,False)

#Test Bus
bus1.start()
bus2.start()


