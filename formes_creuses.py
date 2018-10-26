nb_x = int(input())
nb_lignes_rect = int(input())
nb_col_rect = int(input())
nb_lignes_triangle = int(input())


def afficher_ligne(nb, ch):
    print(ch * nb)


def afficher_col(taille, ch):
    if taille == 1:
        print(ch)
    else:
        print(ch, ' ' * (taille - 2), ch, sep='')


def rectangle(l, c, ch):
    afficher_ligne(l, ch)
    for i in range(c - 2):
        afficher_col(l, ch)
    afficher_ligne(l, ch)


def triangle(l, ch):
    print(ch)
    for i in range(2, l):
        afficher_col(i, ch)
    afficher_ligne(l, ch)


afficher_ligne(nb_x, 'X')
print()
rectangle(nb_col_rect, nb_lignes_rect, '#')
print()
triangle(nb_lignes_triangle, '@')