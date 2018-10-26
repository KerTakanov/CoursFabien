nb_livres = int(input())
lg_min = int(input())

for i in range(nb_livres):
    livre = input()
    resume = input()

    if len(resume) < lg_min:
        print(livre)
