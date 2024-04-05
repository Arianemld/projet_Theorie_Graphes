from sommet_arc import trace_arc, nom_arc


def afficher_matrice(choix_fichier):
    # Obtenir les dimensions de la grille à partir des données du fichier
    sommets = nom_arc(choix_fichier)
    nb_sommets = len(sommets)

    # Créer une grille vide
    grille = [['*'] * (nb_sommets + 1) for _ in range(nb_sommets + 1)]

    # Remplir la première ligne avec les numéros de sommets
    grille[0][0] = ' '
    for i in range(nb_sommets):
        grille[0][i + 1] = grille[i + 1][0] = str(i)

    # Remplir la grille avec les données des arcs
    arcs = trace_arc(sommets, choix_fichier)
    for arc in arcs:
        ligne, colonne = arc
        grille[ligne + 1][colonne + 1] = str(ligne)

    # Afficher la grille
    for ligne in grille:
        for element in ligne:
            print(f"{element:>2}", end=" ")  # Espacement uniforme de 2 caractères, aligné à droite
        print()  # Nouvelle ligne après chaque ligne de la grille

    return grille


