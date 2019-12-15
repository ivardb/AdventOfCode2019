from objects.computers.intCodeComputer import intCodeComputer
from collections import deque
from matplotlib import pyplot as plt

class repairDrone(intCodeComputer):

    def __init__(self, program, grid, position):
        self.grid = grid
        self.x = position[0]
        self.y = position[1]
        self.grid[self.y,self.x] = '4'
        self.direction = 0
        self.dx = {1:0, 2:0, 3:-1, 4:1}
        self.dy = {1:-1, 2:1, 3:0, 4:0}
        self.stack = deque()
        self.opposites = {1:2,2:1,3:4,4:3}
        self.displayCounter = 0
        super().__init__(program)

    def processInput(self):
        neighbours = self.getNeighbours()
        validNeighbours = [x for x in neighbours.keys() if neighbours.get(x) == 0]
        if len(validNeighbours) > 0:
            self.direction = validNeighbours[0]
            self.stack.append(validNeighbours[0])
            return validNeighbours[0]
        else:
            newDir = self.opposites.get(self.stack.pop())
            self.direction = newDir
            return newDir

    def processOutput(self, output):
        if output==0:
            self.stack.pop()
            self.grid[self.y+self.dy.get(self.direction), self.x+self.dx.get(self.direction)] = '3'
        elif output==1:
            self.x+=self.dx.get(self.direction)
            self.y+= self.dy.get(self.direction)
            self.grid[self.y,self.x] = '2'
        elif output==2:
            self.x+=self.dx.get(self.direction)
            self.y+= self.dy.get(self.direction)
            self.grid[self.y,self.x] = '1'
        if self.displayCounter%40==0:
            self.display()
        self.displayCounter+=1


    def getNeighbours(self):
        res = dict()
        for i in range(1,5):
            res[i] = self.grid[self.y+self.dy.get(i), self.x+self.dx.get(i)]
        return res

    def display(self):
        plt.figure()
        plt.imshow(self.grid)
        plt.show()
