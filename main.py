# implémenter le score

def nouvelle_grille() :
    grille = [None] * 3
    for i in range(3):
        grille[i] = [""] * 3
    return grille

def nom_joueur():
    nom = input(f"Entrez le nom du joueur :")
    print("")
    return nom

def choix_symbole():
    print("choisissez un symbole : 1 pour X, 2 pour O")
    symboles = ["X", "O"]
    nombre = input()
    while not str(nombre).isnumeric() or int(nombre) not in (1, 2):
        print("veuillez renter un nombre égal à 1 ou 2")
        nombre = input()
    nombre = int(nombre)
    return symboles[nombre-1]

print("Bienvenue au jeu du Morpion !")
