from collections import defaultdict, deque
from sommet_arc import nom_arc, trace_arc

def verif_ordo(choix_fichier):
    sommets = nom_arc(choix_fichier)
    arcs = trace_arc(sommets, choix_fichier)

    # Création du graphe et initialisation des prédécesseurs pour tous les sommets concernés
    graph = defaultdict(list)
    in_degree = defaultdict(int)  # Utilisation de defaultdict pour éviter les KeyError

    for origine, destination in arcs:
        graph[origine].append(destination)
        in_degree[destination] += 1

    # Points d'entrée pour l'algorithme (sommets sans prédécesseurs)
    queue = deque([s for s in sommets if in_degree[s] == 0])
    visited_count = 0

    while queue:
        current = queue.popleft()
        visited_count += 1
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Vérification de la présence de circuit
    if visited_count == len(sommets):
        print("Pas de circuit détecté, le graphe peut être ordonnancé.")
        return False  # Pas de circuit
    else:
        print("Un circuit a été détecté, vérification impossible.")
        remaining_nodes = [s for s, degree in in_degree.items() if degree > 0]
        print(f"Sommets restant avec des prédécesseurs non supprimés : {remaining_nodes}")
        return True  # Présence d'un circuit

    
def calculer_rangs(grille):
    nb_sommets = len(grille)  # suppose que grille est carrée
    in_degree = [0] * nb_sommets
    graph = defaultdict(list)

    # Construction du graphe à partir de la grille
    for i in range(nb_sommets):
        for j in range(nb_sommets):
            if grille[i][j] != '*' and grille[i][j] != '0':
                graph[i].append(j)  # i dépend de j
                in_degree[j] += 1

    # Tâches sans prédécesseurs
    sources = deque([i for i in range(nb_sommets) if in_degree[i] == 0])
    ranks = {}
    current_rank = 0

    # Tri topologique et affectation des rangs
    while sources:
        next_sources = deque()
        for node in sources:
            ranks[node] = current_rank
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    next_sources.append(neighbor)
        sources = next_sources
        current_rank += 1

    return ranks












