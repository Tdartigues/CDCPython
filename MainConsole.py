from CDCPython.Classe.Ecole import Ecole
from CDCPython.Classe.Classe import Classe
from CDCPython.Classe.Etudiant import Etudiant
from CDCPython.Classe.Professeur import Professeur

print("Initialisation des données.")

initilisation = True
nom_ecole = input("Veuillez saisir votre école : ")
ecole = Ecole(nom_ecole)

while initilisation:
    print("Votre choix : ")
    print("\t1-Créer des professeurs")
    print("\t2-Créer des classes et élèves")
    print("\t3-Arrêter")
    choix = int(input())
    if choix == 1:
        ajoutProfesseur = True
        while ajoutProfesseur:
            nom_professeur = input("Nom du professeur : ")
            prenom_professeur = input("Prénom du professeur : ")
            professeur = Professeur(nom_professeur, prenom_professeur)
            ecole.add_professeur(professeur)
            print("Votre choix : ")
            print("\t1-Créer un autre professeur")
            print("\t2-Retour au menu initialisation")
            choix = int(input())
            if choix == 1:
                print('---------')
            elif choix == 2:
                ajoutProfesseur = False
            else:
                print('Veuillez taper 1 ou 2.')
    elif choix == 2:
        ajoutClasse = True
        while ajoutClasse:
            nom_classe = input("Nom de la classe : ")
            limite = int(input("Limite du nombre d'étudiants : "))
            classe = Classe(nom_classe, limite)
            nbEtudiant = 0
            ajoutEtudiant = True
            while nbEtudiant < limite and ajoutEtudiant:
                nom_etudiant = input("Nom de l'élève : ")
                prenom_etudiant = input("Prénom de l'élève : ")
                eleve = Etudiant(nom_etudiant, prenom_etudiant, nom_classe)
                classe.add(eleve)
                nbEtudiant += 1
                if nbEtudiant == limite:
                    ajoutEtudiant = False
                else:
                    print("Votre choix : ")
                    print("\t1-Créer un autre étudiant")
                    print("\t2-Retour au menu initialisation")
                    choix = int(input())
                    if choix == 1:
                        print('---------')
                    elif choix == 2:
                        ajoutEtudiant = False
                    else:
                        print('Veuillez taper 1 ou 2.')
            ecole.add_classe(classe)
            print("Votre choix : ")
            print("\t1-Créer une autre classe")
            print("\t2-Retour au menu initialisation")
            choix = int(input())
            if choix == 1:
                print('---------')
            elif choix == 2:
                ajoutClasse = False
            else:
                print('Veuillez taper 1 ou 2.')
    elif choix == 3:
        initilisation = False
    else:
        print('Veuillez taper 1 ou 2.')

print(ecole.nom)
for i in range(len(ecole.classes)):
    print(ecole.classes[i].nom)
    for j in range(len(ecole.classes[i].eleves)):
        print(ecole.classes[i].eleves[j].nom + ' ' + ecole.classes[i].eleves[j].prenom)

for i in range(len(ecole.professeurs)):
    print(ecole.professeurs[i].nom + ' ' + ecole.professeurs[i].prenom)


