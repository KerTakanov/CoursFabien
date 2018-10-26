prix_ingredients = [9, 5, 12, 15, 7, 42, 13, 10, 1, 20]

cout_total = 0
for i in range(10):
    cout_total += prix_ingredients[i] * int(input())

print(cout_total)
