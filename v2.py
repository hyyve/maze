import random

# Classe qui génère le labyrinthe
class LabyrintheGenerateur:
    def __init__(self, taille):
        self.taille = taille  # Taille du labyrinthe (nombre de lignes et de colonnes)

    def generer(self):
        # Génère un labyrinthe sous forme de dictionnaire avec des cellules aléatoires
        colone = {}  # Crée un dictionnaire vide pour stocker les cellules du labyrinthe
        for i in range(self.taille):  # Boucle pour chaque ligne
            for n in range(self.taille):  # Boucle pour chaque colonne
                # Chaque cellule du labyrinthe reçoit une valeur aléatoire 0 (mur) ou 1 (espace vide)
                colone[(i, n)] = random.randint(0, 1)  # 1 pour un espace vide, 0 pour un mur
        return colone  # Retourne le dictionnaire représentant le labyrinthe

# Classe représentant le labyrinthe
class Labyrinthe:
    def __init__(self, taille):
        self.generateur = LabyrintheGenerateur(taille)  # Crée une instance de LabyrintheGenerateur
        self.labyrinthe = self.generateur.generer()  # Génère le labyrinthe

    def afficher(self):
        # Affiche le labyrinthe ligne par ligne
        for x in range(self.taille):  # Boucle pour chaque ligne du labyrinthe
            for y in range(self.taille):  # Boucle pour chaque cellule de la ligne
                if self.labyrinthe[(x, y)] == 1:
                    print(" ", end="")  # Affiche un espace pour un chemin vide
                else:
                    print("#", end="")  # Affiche un "#" pour un mur
            print()  # Nouvelle ligne après chaque ligne du labyrinthe

# Demander à l'utilisateur la taille du labyrinthe
taille = int(input("Entrez la taille du labyrinthe: "))  

# Créer une instance du labyrinthe et afficher le résultat
labyrinthe = Labyrinthe(taille)  
labyrinthe.afficher()  # Afficher le labyrinthe généré
