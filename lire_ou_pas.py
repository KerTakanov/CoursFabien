nb_livres = int(input())

precedent = ""
for i in range(nb_livres):
    livre = input()

    if len(livre) > len(precedent):
        print(livre)
        precedent = livre
