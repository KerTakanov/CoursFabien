nb_notes = int(input())
somme_notes = 0
"""
Pour calculer la moyenne, on va devoir faire la somme des notes, puis diviser par le nombre de notes.
On doit donc initialiser une variable qui vaut zéro pour pouvoir faire la somme
"""

for i in range(nb_notes):
    somme_notes += int(input())  # on ajoute la note à la somme

print(somme_notes / nb_notes)  # puis on affiche la moyenne
