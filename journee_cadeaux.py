nb_habitants = int(input())

fortunes = sorted([int(input()) for i in range(nb_habitants)])

if nb_habitants % 2:  # impair
    print(fortunes[int((nb_habitants - 1) / 2)])
else:  # pair
    idx1, idx2 = int((nb_habitants - 1) / 2), int((nb_habitants + 1) / 2)
    print((fortunes[idx1] + fortunes[idx2]) / 2)

