nb = int(input())

while nb != 1:
    if nb % 2 == 0:
        nb //= 2
    else:
        nb = nb * 3 + 1
    print(nb, end=' ')
