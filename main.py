from afficher_matrice import afficher_matrice
from choix_fichier import choisir_fichier
from sommet_arc import sommet as fct_sommet , nom_arc, lire_durees_et_arcs
from verif_ordo import verif_ordo, calculer_calendriers_et_marges, calculer_rangs, trouver_chemins_critiques


def print_hi(name):
    print("\n                 PROJET - THEORIE DES GRAPHES\n\n")
    fichier = choisir_fichier()
    print("Vous avez choisi d'analyser le fichier :", fichier)

    # Lecture du fichier txt pour obtenir les sommets et les arcs

    nb_sommets = fct_sommet(fichier)

    # Obtention des noms des sommets
    noms_sommets = nom_arc(fichier)

    if noms_sommets is not None:
        # Affichage des noms des sommets
        print("\n Voici les différents sommets que vous avez :", noms_sommets)

        # Affichage des arcs du graphe d'ordonnancement
        print("Arcs du graphe d'ordonnancement :")
        durees, arcs = lire_durees_et_arcs(fichier)
        # Affichage des arcs
        for arc in arcs:
            print(f"{arc[0]} -> {arc[1]} = {arc[0]}")

        # Affichage de la grille
        print("Grille correspondante au graphe :\n")
        grille = afficher_matrice(fichier)

        # Vérification d'ordonnancement et calcul des propriétés si le graphe est valide
        point_entree, point_sortie, est_ordonne = verif_ordo(fichier)

        # Afficher les résultats seulement si le graphe est un graphe d'ordonnancement
        if est_ordonne:
            # Calcul des rangs des sommets
            rangs = calculer_rangs(arcs)

            # Affichage des rangs des sommets
            print("\nRangs des sommets :")
            for i in range(len(noms_sommets)):
                print(f"Sommet {noms_sommets[i]}: {rangs.get(i)}")

            # Calcul des calendriers et marges
            est, lft, margins = calculer_calendriers_et_marges(arcs, durees)

            # Affichage des calendriers au plus tôt
            print("\nCalendriers au plus tôt :")
            for sommet in est:
                print(f"Calendrier au plus tôt pour le sommet {sommet} est {est[sommet]}")

            # Affichage des calendriers au plus tard
            print("\nCalendriers au plus tard :")
            for sommet in lft:
                print(f"Calendrier au plus tard pour le sommet {sommet} est {lft[sommet]}")

            # Affichage des marges de chaque tâche
            print("\nMarges de chaque tâche :")
            for sommet in margins:
                print(f"La marge pour le sommet {sommet} est de {margins[sommet]}")

            # Calcul et affichage des chemins critiques
            chemins_critiques = trouver_chemins_critiques(est, lft, durees, arcs)
            print("\nChemins critiques du projet:")
            for chemin in chemins_critiques:
                print(" -> ".join(map(str, chemin)))

        else:
            print("Le graphe ne satisfait pas les conditions pour être un graphe d'ordonnancement.")

    else:
        print("Erreur lors de la lecture des noms de sommets.")


if __name__ == '__main__':
    print_hi('PyCharm')
