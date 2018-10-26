nb_positions = int(input())
nb_changements_positions = int(input())

pos_personnes = [int(input()) for i in range(nb_positions)]

for i in range(nb_changements_positions):
    changement1 = int(input())
    changement2 = int(input())

    pos_personnes[changement1], pos_personnes[changement2] = pos_personnes[changement2], pos_personnes[changement1]

for pos in pos_personnes:
    print(pos)
