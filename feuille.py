epaisseur = 0.0110  # epaisseur initiale en cm

# on boucle de 0 à 15 (non inclus !) car on plie 15 fois la feuille
for i in range(15):
    epaisseur *= 2  # *= permet de multiplier la variable de gauche par l'expression de droite

print(epaisseur)
