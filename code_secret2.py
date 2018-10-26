def valider_code(bon_code):
    code = input("Entrez le code :\n")

    if code == bon_code:
        return True

    return False


while not valider_code('4242'):
    pass
print('Premier code bon.')

while not valider_code('2121'):
    pass

print('Bravo.')

