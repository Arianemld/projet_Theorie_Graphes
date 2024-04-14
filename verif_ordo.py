from sommet_arc import nom_arc, trace_arc

def verif_ordo(choix_fichier):
    sommets = nom_arc(choix_fichier)
    point_entree = sommets[0]
    point_sortie = sommets[-1]

    print("Point d'entrée :", point_entree)
    print("Point de sortie :", point_sortie)

    sommets_restants = list(range(point_entree, point_sortie + 1))
    print("Sommets restants :", ' '.join(map(str, sommets_restants)))

    while len(sommets_restants) > 0:
        print("\nPoints d'entrée :", ' '.join(map(str, sommets_restants)))
        print("Suppression des points d'entrée")
        arcs = trace_arc(sommets, choix_fichier)  # Correction ici
        voisins = set()
        for arc in arcs:
            if arc[0] in sommets_restants:
                voisins.add(arc[1])
        sommets_restants = list(voisins)
        print("Sommets restants :", ' '.join(map(str, sommets_restants)))

    if point_sortie in sommets_restants:
        print("-> Il n’y a pas de circuit")
    else:
        print("-> Il y a un circuit")

    print("Il n’y a pas d’arcs négatifs")
    print("-> C’est un graphe d’ordonnancement")

    return point_entree, point_sortie
