nb_lignes = int(input())

lignes = [input() for i in range(nb_lignes)]

for ligne in [lignes[i] for i in range(nb_lignes) if i % 2 == 0]:
    print(ligne)
