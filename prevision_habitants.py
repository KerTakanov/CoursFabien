from math import floor

nb_habs = int(input())
croissance = float(input()) / 100
# la croissance est donnée en %age sur 100 plutôt que sur 1, on doit donc diviser par 100 pour faciliter les calculs

print(floor(nb_habs * (1 + croissance)))
#  pour ajouter un %age à une valeur, on multiplie cette valeur par 1 + pourcentage
