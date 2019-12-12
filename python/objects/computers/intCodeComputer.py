from abc import ABC, abstractmethod

class intCodeComputer(ABC):

    def __init__(self, program):
        self.program = program
        self.position = 0
        self.relativeBase = 0

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
            inputCode = self.processInput()
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

    """Should return the value inputted in the machine"""
    @abstractmethod
    def processInput(self):
        pass


    """Should process the output"""
    @abstractmethod
    def processOutput(self, output):
        pass