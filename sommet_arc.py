import choix_fichier

#sommet
def sommet(choix_fichier):
    with open(choix_fichier, 'r') as fichier:

        #calcul du nb de sommet
        nb_sommet = 2 #on commence à 2 car nous avons alpha et omega pour entree et sortie

        for ligne in fichier:
            nb_sommet += 1

    print("Sommet :", nb_sommet)

#arc
def nom_arc(choix_fichier):
    nom_sommet=[0]

    with open(choix_fichier, 'r') as file:
        for ligne in file:
            valeurs = ligne.split()
            premier_val = valeurs[0]

            nom_sommet.append(premier_val)

        # Ajouter n+1 à la liste
        dernier_sommet = len(nom_sommet)
        nom_sommet.append(dernier_sommet)

    return nom_sommet


def trace_arc(nom_sommet, choix_fichier):
    arcs = []
    with open(choix_fichier, 'r') as file:
        for i, ligne in enumerate(file, start=1):  # On parcourt chaque ligne du fichier txt
            valeurs = ligne.split()
            # Pour le cas où il y a deux valeurs sur la ligne
            if len(valeurs) == 2:
                deuxieme_val = valeurs[1]
                arc = (nom_sommet[0], int(deuxieme_val))
                arcs.append(arc)
                #print(f"{nom_sommet[0]} -> {deuxieme_val}")
            elif len(valeurs) > 2:
                sommet_depart = int(valeurs[0])
                for valeur in valeurs[1:]:
                    sommet_arrivee = int(valeur)
                    if sommet_depart < sommet_arrivee:
                        arc = (sommet_depart, sommet_arrivee)
                    else:
                        arc = (sommet_arrivee, sommet_depart)
                    if arc[0] == arc[1]:  # Vérifier si arc[0] est égal à arc[1]
                        arc = (arc[0], len(nom_sommet) - 1)  # Remplacer arc[1] par sommet_n_plus_1
                    arcs.append(arc)


    # Tri des arcs par sommet de départ
    arcs.sort(key=lambda x: x[0])

    # Affichage des arcs
    for arc in arcs:
        print(f"{arc[0]} -> {arc[1]}")

    return arcs


