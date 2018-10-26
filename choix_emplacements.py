nb_emplacements = int(input())
num_marchand = [int(input()) for i in range(nb_emplacements)]

for num in sorted(num_marchand):
    print(num_marchand.index(num))
