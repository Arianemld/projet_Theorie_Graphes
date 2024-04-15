from collections import defaultdict

from sommet_arc import nom_arc, trace_arc


def verif_ordo(choix_fichier):
    sommets = nom_arc(choix_fichier)
    point_entree = sommets[0]
    point_sortie = sommets[-1]

    print("Il y a un seul point d'entrée :", point_entree)
    print("Il y a un seul point de sortie :", point_sortie)
    print()

    print("* Détection de circuit")
    print("* Méthode d’élimination des points d’entrée")
    #print("liste des sommets: ", sommets)
    print("Points d'entrée :", point_entree)
    print("Suppression des points d'entrée")

    #suppression du point d'entrée 0
    sommets.remove(point_entree)
    # Afficher la liste des sommets après suppression
    print("Liste des sommets après suppression du point d'entrée :", sommets)
    print()

    noms_sommets = nom_arc(choix_fichier)

    arcs = trace_arc(noms_sommets, choix_fichier)

    # Créer un dictionnaire pour stocker les valeurs de arc[1] pour chaque arc[0]
    arc_values = defaultdict(list)

    # Parcourir les arcs et stocker les valeurs de arc[1] pour chaque arc[0]
    for arc in arcs:
        arc_values[arc[0]].append(arc[1])



    # Afficher les valeurs pour chaque arc[0] et supprimer les valeurs de la liste
    for sommet, valeurs in arc_values.items():
        suppression_effectuee = False
        #print(f"Arcs partant de {sommet}: {', '.join(map(str, valeurs))}")
        # stocker les points supprimés
        points_supp = []
        for valeur in valeurs:
            if str(valeur) in sommets:
                sommets.remove(str(valeur))
                points_supp.append(valeur)
                suppression_effectuee = True
        if suppression_effectuee:
            print("Suppresion des points d'entrée:", sommets)
            print("Points supprimés:", ','.join(map(str, points_supp)))
        print()


    #suppresion du dernier élément
    if len(sommets) == 1 and sommets[0] == point_sortie:
        last_val = sommets[0]
        sommets.pop()
        print("Suppresion des points d'entrée:", sommets)
        print("Points supprimés:", last_val)
    print()









    return point_entree, point_sortie



