nb_legumes = int(input())  # on récupère le nombre de légumes, que l'on converti en entier

for i in range(nb_legumes):  # on boucle nb_legumes fois afin de récupérer les informations de chaque légume
    poids, age, prix_vente = float(input()), float(input()), float(input())  # on récupère les trois informations
    """
    L'écriture a, b, ... n = expr1, expr2, ... exprn est une écriture un peu spéciale qui reviendrait à écrire ceci:
    a = expr1
    b = expr2
    ...
    n = exprn
    
    C'est une façon plus compacte de l'écrire qui utilise certains mécanismes de Python
    """

    print(prix_vente / poids)
