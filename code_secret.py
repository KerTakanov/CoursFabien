def valider_code():
    code = input("Entrez le code :\n")

    if code == '4242':
        return True

    return False


while not valider_code():
    pass
print('Encore une fois.')

while not valider_code():
    pass

print('Bravo.')

