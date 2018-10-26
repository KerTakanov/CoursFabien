nb_lignes, nb_mots = [int(inp) for inp in input().split(" ")]

longueurs = [0] * 101

for ligne in [input() for i in range(nb_lignes)]:
    for mot in ligne.split(" "):
        longueurs[len(mot)] += 1

for i in range(len(longueurs)):
    if longueurs[i] > 0:
        print("{} : {}".format(i, longueurs[i]))
