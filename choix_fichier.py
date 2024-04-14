import os #Si vous voulez simplement lire ou écrire un fichier, voir open() , si vous voulez manipuler les chemins de fichiers,
import re #permet de rechercher et manipuler des chaînes de caractères de manière flexible et puissante

#pour que ca affiche dans l'ordre croissant les fichiers txt
def extract_numbers(s):
    # Utilisation d'une expression régulière pour extraire les nombres d'une chaîne
    return [int(x) if x.isdigit() else x for x in re.split(r'(\d+)', s)]

def lister_fichiers_dossier():
    fichiers = os.listdir()
    fichiers_txt = [fichier for fichier in fichiers if fichier.endswith('.txt')]
    return sorted(fichiers_txt, key=extract_numbers) #pour que ca s'affiche de façon ordonné croissant

def choisir_fichier():
    print("Fichiers disponibles dans le répertoire courant :\n")
    fichiers = lister_fichiers_dossier()
    for i, fichier in enumerate(fichiers, start=1):
        print(f"{i}. {fichier}")

    choix = input("\nVeuillez sélectionner un fichier à analyser (entrez le numéro) : ")
    choix = int(choix)

    if choix < 1 or choix > len(fichiers):
        print("Choix invalide. Veuillez sélectionner un numéro valide.")
        return choisir_fichier()
    else:
        fichier_choisi = fichiers[choix - 1]
        return fichier_choisi