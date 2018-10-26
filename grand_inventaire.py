nb_operations = int(input())

qte_ingredients = [0 for i in range(10)]

for i in range(nb_operations):
    num_ingredient, qte_ingredient = int(input()), int(input())
    qte_ingredients[num_ingredient - 1] += qte_ingredient

for qte in qte_ingredients:
    print(qte)
