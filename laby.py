import random

def labyrinthe(taille):
    #generation aleatoire de la liste qui contient le labyrinth(à changer car ca fait des labyrinthe bizarre)
    colone = {}
    for i in range(taille):
        for n in range(taille):
            colone[(i,n)]= random.randint(0,1)
    #affichage du labyrinthe
    for x in range(taille):
        for y in range(taille):
            if colone[(x,y)]==1:
                print(" ", end="")
            else:
                print("█",end="")
        print()

taille = int(input("zaert"))
labyrinthe(taille)