nb_personnes = int(input())

for i in range(nb_personnes):
    nom, prenom = input().split(" ")
    print(prenom, nom)
