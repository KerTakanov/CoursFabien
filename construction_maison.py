from math import ceil
# il faut préférer importer les modules de façon granulaire (1 par 1) plutôt que d'utiliser le wildcard (*)
# car lorsqu'on utilise le wildcard, on importe TOUTE la bibliothèque, même les fonctions inutiles !
# ça pèse lourd, et ça "pollue" l'espace de nom ( https://fr.wikipedia.org/wiki/Espace_de_noms )

qte_ciment = float(input())
prix_sac = 45
poids_sac = 60

print(ceil(qte_ciment / poids_sac) * prix_sac)
# on pourrait utiliser une variable intermédiaire ici, c'est d'ailleurs une bonne pratique de le faire, car le code
# est alors plus lisible (on affiche quelque chose avec un nom et pas un calcul comme ça!)
