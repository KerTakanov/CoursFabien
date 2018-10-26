taxe = 1 + float(input()) / 100  # 1 + ... => plus simple à calculer l'inverse
nv_taxe = 1 + float(input()) / 100
prix_actuel = float(input())

prix_ht_actuel = prix_actuel * (1 / taxe)
prix_nv_taxe = prix_ht_actuel * nv_taxe

print(round(prix_nv_taxe, 2))
