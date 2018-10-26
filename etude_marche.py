nb_produits, nb_personnes = int(input()), int(input())

preferences = [0] * nb_produits

for i in range(nb_personnes):
    preferences[int(input())] += 1

for preference in preferences:
    print(preference)
