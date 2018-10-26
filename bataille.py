jeu1 = input()
jeu2 = input()

egalites = 0
vainqueur = '='

for i in range(max(len(jeu1), len(jeu2))):
    if i >= len(jeu1):
        vainqueur = '2'
        break
    elif i >= len(jeu2):
        vainqueur = '1'
        break

    if jeu1[i] == jeu2[i]:
        egalites += 1

    if jeu1[i] < jeu2[i]:
        vainqueur = '1'
        break
    elif jeu1[i] > jeu2[i]:
        vainqueur = '2'
        break

print(vainqueur)
print(egalites)
