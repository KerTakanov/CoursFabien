def min2(a, b):
    return a if a < b else b


nb_min = min2(int(input()), int(input()))
for i in range(4):
    nv_nb = min2(int(input()), int(input()))

    nb_min = min2(nb_min, nv_nb)

print(nb_min)
