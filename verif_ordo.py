from sommet_arc import nom_arc, trace_arc

def verif_ordo(choix_fichier):
    sommets = nom_arc(choix_fichier)
    point_entree = sommets[0]
    point_sortie = sommets[-1]

    print("Point d'entrée :", point_entree)
    print("Point de sortie :", point_sortie)



    return point_entree, point_sortie
