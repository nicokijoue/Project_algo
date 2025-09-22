import random


def affichage ():
    for nbr_ligne in tableau_affichage :
        print(nbr_ligne)


def aléatoire (tableau_data, nbr_mines):
    positions_prises = []
    while len(positions_prises) < nbr_mines:
        i = random.randint(0, 9)  
        j = random.randint(0, 9) 
        if (i, j) not in positions_prises:
            tableau_data[i][j] = 1
            positions_prises.append((i, j))


def victoire(nbr_mines):
    cases_cachées = 0
    
    for ligne in tableau_affichage:
        for case in ligne:
            if case == "?":
                cases_cachées += 1
    
    return cases_cachées == nbr_mines


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


def gameplay(tableau_data,nbr_mines):
    nbr_ligne = len(tableau_data)
    nbr_colonne = len(tableau_data[0])
    while True:
        ligne, colonne = coordonnée()
        counter = 0

        if tableau_affichage[ligne][colonne] != "?":
            print("Vous conaissez déjà la case voyons !")
            continue

        if tableau_data[ligne][colonne] == 1:
            print("Vous êtes tomber sur une Mine! pas de chance.")
            tableau_affichage[ligne][colonne] = "💣"
            affichage()
            break 
        else : 
            for i in range(-1, 2):  
                for j in range(-1, 2):  
                    if i == 0 and j == 0:  
                        continue

                    ligne_autour = ligne + i
                    colonne_autour = colonne + j
                
                    if (0 <= ligne_autour < nbr_ligne and 
                        0 <= colonne_autour < nbr_colonne and 
                        tableau_data[ligne_autour][colonne_autour] == 1):
                        counter += 1
            tableau_affichage[ligne][colonne] = counter
            affichage()

            if victoire(nbr_mines):
                print("Victoire !")
                break

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


# pour commencer le jeux
nbr_mines = 20
aléatoire(tableau_data, nbr_mines)
gameplay(tableau_data, nbr_mines)