from afficher_matrice import afficher_matrice
from choix_fichier import choisir_fichier
from sommet_arc import sommet, nom_arc, trace_arc


def print_hi(name):
    print("\n                 PROJET - THEORIE DES GRAPHES\n\n")
    fichier = choisir_fichier()
    print("Vous avez choisi d'analyser le fichier :", fichier)

    # Lecture du fichier txt pour obtenir les sommets et les arcs

    sommets = sommet(fichier)

    # Obtention des noms des sommets
    noms_sommets = nom_arc(fichier)

    if noms_sommets is not None:
        # Affichage des noms des sommets
        print("Voici les différents sommets que vous avez :", noms_sommets)

        # Affichage des arcs du graphe d'ordonnancement
        print("Arcs du graphe d'ordonnancement :")
        arcs = trace_arc(noms_sommets, fichier)
        # Affichage des arcs
        for arc in arcs:
            print(f"{arc[0]} -> {arc[1]} = {arc[0]}")

        #affichage de la grille
        print("Grille correspondante au graphe :")
        grille = afficher_matrice(fichier)








    else:
        print("Erreur lors de la lecture des noms de sommets.")













if __name__ == '__main__':
    print_hi('PyCharm')


