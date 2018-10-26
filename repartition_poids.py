nb_charrettes = int(input())

poids_charettes = [float(input()) for i in range(nb_charrettes)]
moyenne_poids = sum(poids_charettes) / nb_charrettes

poids_ajouter = [moyenne_poids - poids for poids in poids_charettes]

for poids in poids_ajouter:
    print(poids)
