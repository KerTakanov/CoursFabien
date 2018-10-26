nb_participants = int(input())
entier_choisi = sorted([int(input()) for i in range(nb_participants)])

for i in range(nb_participants // 2):
    print(entier_choisi[i], entier_choisi[nb_participants - i - 1])
