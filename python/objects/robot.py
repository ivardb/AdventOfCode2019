class robot:
    def __init__(self, grid, position, program):
        self.grid = grid
        self.gridPosition = position
        self.position = 0
        self.program = program
        self.relativeBase = 0
        self.direction = 0
        self.painted = set()
        self.colourOutput = True

    def executeProgram(self):
        while True:
            advance = self.processCode()
            if advance == -1:
                return
            else:
                self.position+=advance

    def processCode(self):
        instruction = self.program[self.position]
        A = int(instruction/10000)
        instruction -= A * 10000
        B = int(instruction/1000)
        instruction -= B * 1000
        C = int(instruction/100)
        instruction -= C * 100
        opcode = instruction
        if opcode == 1:
            val1 = self.getParameter(self.position+1, C)
            val2 = self.getParameter(self.position+2, B)
            if A==2:
                output = self.program[self.position+3]+self.relativeBase
            else:
                output = self.program[self.position+3]
            self.program[output] = val1 + val2
            return 4
        elif opcode == 2:
            val1 = self.getParameter(self.position+1, C)
            val2 = self.getParameter(self.position+2, B)
            if A==2:
                output = self.program[self.position+3]+self.relativeBase
            else:
                output = self.program[self.position+3]
            self.program[output] = val1 * val2
            return 4
        elif opcode == 3:
            inputCode = self.grid.get(self.gridPosition, 0)
            if C==1:
                self.program[self.program[self.position + 1]] = inputCode
            else:
                self.program[self.program[self.position+1]+self.relativeBase] = inputCode
            return 2
        elif opcode == 4:
            par1 = self.program[self.position + 1]
            if C == 0:
                outputProgram = self.program[par1]
            elif C==1:
                outputProgram = par1
            else:
                outputProgram = self.program[self.relativeBase+par1]
            self.processOutput(outputProgram)
            return 2
        elif opcode == 5:
            val1 = self.getParameter(self.position+1, C)
            val2 = self.getParameter(self.position+2, B)
            if val1!=0:
                self.position = val2
                return 0
            else:
                return 3
        elif opcode == 6:
            val1 = self.getParameter(self.position+1, C)
            val2 = self.getParameter(self.position+2, B)
            if val1==0:
                self.position = val2
                return 0
            else:
                return 3
        elif opcode == 7:
            val1 = self.getParameter(self.position+1, C)
            val2 = self.getParameter(self.position+2, B)
            if A==2:
                output = self.program[self.position+3]+self.relativeBase
            else:
                output = self.program[self.position+3]
            if val1<val2:
                self.program[output] = 1
            else:
                self.program[output] = 0
            return 4
        elif opcode == 8:
            val1 = self.getParameter(self.position+1, C)
            val2 = self.getParameter(self.position+2, B)
            if A==2:
                output = self.program[self.position+3]+self.relativeBase
            else:
                output = self.program[self.position+3]
            if val1==val2:
                self.program[output] = 1
            else:
                self.program[output] = 0
            return 4
        elif opcode == 9:
            val1 = self.getParameter(self.position+1, C)
            self.relativeBase+=val1
            return 2
        elif opcode == 99:
            return -1

    def getParameter(self, pos, type):
        if type==0:
            return self.program[self.program[pos]]
        if type==1:
            return self.program[pos]
        if type==2:
            return self.program[self.relativeBase+self.program[pos]]

    def processOutput(self, output):
        if self.colourOutput:
            self.grid[self.gridPosition] = output
            self.painted.add(self.gridPosition)
            self.colourOutput = False
        else:
            if output==0:
                self.direction = (self.direction + 270)%360
            else:
                self.direction = (self.direction + 90)%360
            self.colourOutput = True
            self.move()

    def move(self):
        dx = {0: -1, 90: 0, 180: 1, 270:0}
        dy = {0: 0, 90: 1, 180: 0, 270:-1}
        newPosition = (self.gridPosition[0]+dx[self.direction], self.gridPosition[1]+dy[self.direction])
        self.gridPosition = newPosition

    def getPainted(self):
        return self.painted