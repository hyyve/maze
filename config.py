EMPTY = 0
WALL = 1

class Coord:
    def __init__(self, x: int, y: int) -> tuple:
        self.x=x
        self.y = y

    #permet de print cette classe, car sinon ca renvoie l'emplacement dans la mémorie ?
    def print(self)->str:
        print((self.x,self.y))

