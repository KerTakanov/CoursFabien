def m2p(m):
    return m / .3048


def g2l(g):
    return g * .002205


def dc2df(dc):
    return dc * 1.8 + 32


nb_conversions = int(input())

for i in range(nb_conversions):
    nb, unite = input().split()
    nb = float(nb)

    if unite == 'm':
        print(m2p(nb), 'p')
    elif unite == 'g':
        print(g2l(nb), 'l')
    elif unite == 'c':
        print(dc2df(nb), 'f')
