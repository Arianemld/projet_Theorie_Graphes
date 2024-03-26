import os #Si vous voulez simplement lire ou écrire un fichier, voir open() , si vous voulez manipuler les chemins de fichiers,

def lister_fichiers_dossier():
    fichiers = os.listdir()
    fichiers_txt = [fichier for fichier in fichiers if fichier.endswith('.txt')]
    return fichiers_txt

def choisir_fichier():
    print("Fichiers disponibles dans le répertoire courant :")
    fichiers = lister_fichiers_dossier()
    for i, fichier in enumerate(fichiers, start=1):
        print(f"{i}. {fichier}")

    choix = input("Veuillez sélectionner un fichier à analyser (entrez le numéro) : ")
    choix = int(choix)

    if choix < 1 or choix > len(fichiers):
        print("Choix invalide. Veuillez sélectionner un numéro valide.")
        return choisir_fichier()
    else:
        fichier_choisi = fichiers[choix - 1]
        return fichier_choisi