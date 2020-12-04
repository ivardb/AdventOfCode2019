from objects.computers.intCodeComputer import intCodeComputer


class ASCII(intCodeComputer):

    def __init__(self, program, grid):
        self.grid = grid
        self.gridReaderX = 0
        self.gridReaderY = 0
        self.reading = True
        super().__init__(program)


    def processInput(self):
        self.reading = False
        return 0


    def processOutput(self, output):
        if self.reading:
            if output == 10:
                self.gridReaderY+=1
                self.gridReaderX=0
            else:
                self.grid[self.gridReaderY, self.gridReaderX] = chr(output)
                self.gridReaderX+=1
        else:
            print(output)

    def displayGrid(self):
        print('\n'.join(' '.join(str(x) for x in row) for row in self.grid))