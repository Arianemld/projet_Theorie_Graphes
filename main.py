from choix_fichier import choisir_fichier


def print_hi(name):
    print("\n                 PROJET - THEORIE DES GRAPHES\n\n")
    fichier = choisir_fichier()
    print(f"Vous avez choisi d'analyser le fichier : {fichier}")



if __name__ == '__main__':
    print_hi('PyCharm')


