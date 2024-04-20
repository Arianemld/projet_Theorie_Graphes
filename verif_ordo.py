from collections import defaultdict, deque
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
        print("sommets restant : aucun")
    #print()

    #circuit ou non
    if len(sommets) == 0:
        print("Il n'y a pas de circuit")
    else:
        print("Il y a un circuit")

    #arc négatif
    arcs_negatifs = False

    for arc in arcs:
        if any(val<0 for val in arc):
            arcs_negatifs = True
            break

    if arcs_negatifs:
        print("Il y a des arcs négatifs")
    else:
        print("Pas d'arc négatif")


    #graphe d'ordonnancement ou non
    if len(sommets) == 0 and not arcs_negatifs:
        return point_entree, point_sortie, True
    else:
        return point_entree, point_sortie, False

    
def calculer_rangs(arcs):
    # Obtention de tous les sommets mentionnés dans les arcs
    tous_les_sommets = set()
    for arc in arcs:
        tous_les_sommets.add(arc[0])
        tous_les_sommets.add(arc[1])

    # Initialisation des rangs de tous les sommets à zéro
    ranks = {sommet: 0 for sommet in tous_les_sommets}

    in_degree = defaultdict(int)
    graph = defaultdict(list)

    # Construction du graphe à partir des arcs
    for arc in arcs:
        graph[arc[0]].append(arc[1])  # arc[1] dépend de arc[0]
        in_degree[arc[1]] += 1

    # Tâches sans prédécesseurs
    sources = [node for node in graph if in_degree[node] == 0]

    # Tri topologique et affectation des rangs
    while sources:
        next_sources = []
        for node in sources:
            for neighbor in graph[node]:
                ranks[neighbor] = max(ranks[neighbor], ranks[node] + 1)
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    next_sources.append(neighbor)
        sources = next_sources

    return ranks



def calculer_calendrier_au_plus_tot(graph, durations, point_entree, point_sortie):
    """
    Cette fonction calcule le calendrier au plus tôt pour chaque tâche dans le graphe d'ordonnancement.

    Args:
        graph (dict): Le graphe d'ordonnancement représenté sous forme de dictionnaire.
        durations (dict): Dictionnaire des durées de chaque arc.
        point_entree (int): Le point d'entrée du graphe.
        point_sortie (int): Le point de sortie du graphe.

    Returns:
        dict: Un dictionnaire contenant les heures de début au plus tôt pour chaque tâche.
    """
    # Initialisation du dictionnaire des heures de début au plus tôt
    early_start = {point_entree: 0}
    
    # File d'attente pour le parcours du graphe
    queue = [point_entree]

    # Parcours du graphe en largeur
    while queue:
        current = queue.pop(0)
        successors = graph[current]

        # Parcours des successeurs du sommet courant
        for successor in successors:
            # Mise à jour de l'heure de début au plus tôt pour le successeur
            if successor not in early_start:
                early_start[successor] = early_start[current] + durations[(current, successor)]
            else:
                early_start[successor] = max(early_start[successor], early_start[current] + durations[(current, successor)])
            
            # Ajout du successeur à la file d'attente
            queue.append(successor)
    
    return early_start






def calculer_calendrier_au_plus_tard(graph, durations, point_sortie, early_start):
    # Initialisation du calendrier au plus tard avec la valeur du calendrier au plus tôt pour le point de sortie
    late_finish = {node: float('inf') for node in graph}

    # Tâches sans successeurs (le point de sortie)
    targets = {node for successors in graph.values() for node in successors}
    targets.add(point_sortie)

    # Parcours du graphe en profondeur (DFS) à partir du point de sortie
    def dfs(node):
        if node not in targets:
            return
        for predecessor, successors in graph.items():
            if node in successors:
                late_finish[node] = min(late_finish[node], late_finish[predecessor] - durations[(predecessor, node)])
                dfs(predecessor)

    # Déclencher DFS à partir du point de sortie
    dfs(point_sortie)

    return late_finish








def calculer_marges(early_start, late_finish):
    total_floats = {}
    for node in early_start:
        total_float = late_finish[node] - early_start[node]
        total_floats[node] = total_float
    return total_floats











