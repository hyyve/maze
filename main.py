import constant
import Maze
import MazeGenerator

def main():
    x = int(input("Enter the width : "))
    y= int(input("Enter the height : "))
    maze = Maze.Maze(x,y)
    print(maze.str())

if __name__ == "__main__":
    main()