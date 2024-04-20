from afficher_matrice import afficher_matrice
from choix_fichier import choisir_fichier
from sommet_arc import sommet as sommet_fonc, nom_arc, trace_arc
from verif_ordo import verif_ordo, calculer_rangs, calculer_calendrier_au_plus_tot, calculer_calendrier_au_plus_tard, calculer_marges
from collections import defaultdict

def print_hi(name):
    print("\n                 PROJET - THEORIE DES GRAPHES\n\n")
    fichier = choisir_fichier()
    print("Vous avez choisi d'analyser le fichier :", fichier)

    sommets = sommet_fonc(fichier)
    noms_sommets = nom_arc(fichier)

    if noms_sommets is not None:
        print("\nVoici les différents sommets que vous avez :", noms_sommets)
        arcs = trace_arc(noms_sommets, fichier)
        print("Arcs du graphe d'ordonnancement :")
        for arc in arcs:
            print(f"{arc[0]} -> {arc[1]}")

        grille = afficher_matrice(fichier)
        print("Grille correspondante au graphe :\n")

        verif_result = verif_ordo(fichier)
        if verif_result:
            point_entree, point_sortie, is_ordonnancement = verif_result
            print(f"Est-ce un graph d'ordonnancement ?  {is_ordonnancement}")
            if is_ordonnancement:
                rangs = calculer_rangs(arcs)
                print("\nRangs des sommets :")
                for sommet in rangs:
                    print(f"Sommet {sommet}: Rang {rangs[sommet]}")

                graph = defaultdict(list)
                for arc in arcs:
                    graph[arc[0]].append(arc[1])

                durations = {tuple(arc[:2]): 1 for arc in arcs}
                early_start = calculer_calendrier_au_plus_tot(graph, durations, point_entree, point_sortie)
                
                late_finish = calculer_calendrier_au_plus_tard(graph, durations, point_sortie, early_start)
                marges = calculer_marges(early_start, late_finish)

                print("\nCalendrier au plus tôt:")
                for node, time in early_start.items():
                    print(f"{node}: Début au plus tôt à {time}")

                print("\nCalendrier au plus tard:")
                for node, time in late_finish.items():
                    print(f"{node}: Fin au plus tard à {time}")

                print("\nMarges:")
                for node, marge in marges.items():
                    print(f"{node}: Marge totale de {marge}")
            else:
                print("\nLe graphe n'est pas un graphe d'ordonnancement.")
        else:
            print("\nErreur lors de la vérification des propriétés.")
    else:
        print("Erreur lors de la lecture des noms de sommets.")

if __name__ == '__main__':
    print_hi('PyCharm')
