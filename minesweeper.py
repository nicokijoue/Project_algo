import random


def affichage ():
    for row in tableau_affichage :
        print(row)


def aléatoire (tableau, nbr_mines):
    positions_prises = []
    while len(positions_prises) < nbr_mines:
        i = random.randint(0, 9)  
        j = random.randint(0, 9) 
        if (i, j) not in positions_prises:
            tableau[i][j] = 1
            positions_prises.append((i, j))

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
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

affichage()
