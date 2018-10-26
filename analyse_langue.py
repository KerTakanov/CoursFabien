lettre_a_analyser = input()
nb_lignes = int(input())

compteur = 0
for ligne in [input() for i in range(nb_lignes)]:
    compteur += ligne.count(lettre_a_analyser)

print(compteur)
