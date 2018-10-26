nb_deplacements = int(input())

deplacements = [int(input()) for i in range(nb_deplacements)]

for deplacement in reversed(deplacements):
    if deplacement == 5:
        print(4)
    elif deplacement == 4:
        print(5)
    elif deplacement == 1:
        print(2)
    elif deplacement == 2:
        print(1)
    else:
        print(deplacement)
