livre = input()
auteur = input()

print(''.join([c for c in livre if c not in 'AEIOUY ']))
print(''.join([c for c in auteur if c not in 'AEIOUY ']))