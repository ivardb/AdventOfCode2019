from objects.computers.intCodeComputer import intCodeComputer

class arcadeCabinet(intCodeComputer):

    def __init__(self, program, grid):
        self.x = 0
        self.y = 0
        self.grid = grid
        self.outputCounter = 0
        self.ballX = 0
        self.paddleX = 0
        self.score = 0
        super().__init__(program)

    def processInput(self):
        if self.ballX>self.paddleX:
            return 1
        elif self.ballX==self.paddleX:
            return 0
        else:
            return -1

    def processOutput(self, output):
        if self.outputCounter==0:
            self.x = output
        elif self.outputCounter==1:
            self.y = output
        elif self.outputCounter==2:
            if self.x==-1 and self.y==0:
                self.score = output
            elif output == 3:
                self.paddleX = self.x
            elif output == 4:
                self.ballX = self.x
            self.grid[self.y, self.x] = output
        self.outputCounter = (self.outputCounter+1)%3
