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

print("Bienvenue au jeu du Morpion !")
