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
        print("Sommets restants : aucun")
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



def calculer_calendriers_et_marges(arcs, durees):
  # Construction du graphe et calcul du tri topologique
  graph = defaultdict(list)
  in_degree = defaultdict(int)
  for start, end in arcs:
      graph[start].append(end)
      in_degree[end] += 1

  # Liste des sommets sans prédécesseurs (sources)
  queue = deque([v for v in durees.keys() if in_degree[v] == 0])
  est = {v: 0 for v in durees.keys()}  # Temps de début au plus tôt
  lft = {}  # Temps de fin au plus tard

  # Calcul du calendrier au plus tôt
  while queue:
      node = queue.popleft()
      current_end_time = est[node] + durees[node]
      for successor in graph[node]:
          est[successor] = max(est.get(successor, 0), current_end_time)
          in_degree[successor] -= 1
          if in_degree[successor] == 0:
              queue.append(successor)

  # Définir le temps de fin au plus tard du dernier nœud
  max_completion_time = max(est[v] + durees[v] for v in est)
  lft = {v: max_completion_time for v in est.keys()}

  # Calcul du calendrier au plus tard
  for node in reversed(sorted(est, key=est.get)):
      for predecessor in graph:
          if node in graph[predecessor]:
              lft[predecessor] = min(lft[predecessor], lft[node] - durees[predecessor])

  # Calcul des marges
  margins = {v: lft[v] - est[v]  for v in est.keys()}

  return est, lft, margins


def trouver_chemins_critiques(est, lft, durees, arcs):
    # Identifier les sommets avec une marge de zéro
    sommets_critiques = {sommet for sommet, marge in ((v, lft[v] - est[v]) for v in est) if marge == 0}

    # Créer un graphe pour faciliter la recherche des chemins
    graph = defaultdict(list)
    for start, end in arcs:
        if start in sommets_critiques and end in sommets_critiques:
            graph[start].append(end)

    # Fonction récursive pour explorer tous les chemins critiques
    def explorer_chemin(chemin, node):
        if not graph[node]:  # Si aucun successeur, chemin terminé
            chemins_critiques.append(chemin + [node])
        else:
            for successeur in graph[node]:
                explorer_chemin(chemin + [node], successeur)

    # Lancer l'exploration à partir des sommets sans prédécesseurs dans le sous-ensemble critique
    chemins_critiques = []
    sources_critiques = [node for node in sommets_critiques if all(pred not in sommets_critiques for pred, succ in arcs if succ == node)]
    for source in sources_critiques:
        explorer_chemin([], source)

    return chemins_critiques


