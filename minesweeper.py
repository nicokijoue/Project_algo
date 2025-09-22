import random


def affichage ():
    for ligne in tableau_affichage :
        print(ligne)


def aléatoire (tableau, nbr_mines):
    positions_prises = []
    while len(positions_prises) < nbr_mines:
        i = random.randint(0, 9)  
        j = random.randint(0, 9) 
        if (i, j) not in positions_prises:
            tableau[i][j] = 1
            positions_prises.append((i, j))


def coordonnée():
    while True:
        try:
            ligne = int(input("entrer une ligne entre 0-9 (0 et 9 comprit): "))
            colonne = int(input("enter une colonne entre 0-9 (0 et 9 comprit): "))
            if 0 <= ligne <= 9 and 0 <= colonne <= 9:
                return ligne, colonne
            else:
                print("veuillez mettre un nombre entre 0-9 (0 et 9 comprit)")
        except ValueError:
            print("veuillez enter un nombre et non autre chose.")


tableau_data = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

tableau_affichage = [
    ["?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?"]
]

affichage()
