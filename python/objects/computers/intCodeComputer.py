from abc import ABC, abstractmethod

class intCodeComputer(ABC):

    def __init__(self, program):
        self.program = { i : program[i] for i in range(0, len(program))}
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
        instruction = self.program.get(self.position, 0)
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
            output = self.getOutputLocation(self.position+3, A)
            self.program[output] = val1 + val2
            return 4

        elif opcode == 2:
            val1 = self.getParameter(self.position+1, C)
            val2 = self.getParameter(self.position+2, B)
            output = self.getOutputLocation(self.position+3, A)
            self.program[output] = val1 * val2
            return 4

        elif opcode == 3:
            inputCode = self.processInput()
            output = self.getOutputLocation(self.position+1, C)
            self.program[output] = inputCode
            return 2

        elif opcode == 4:
            outputProgram = self.getParameter(self.position+1, C)
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
            output = self.getOutputLocation(self.position+3, A)
            if val1<val2:
                self.program[output] = 1
            else:
                self.program[output] = 0
            return 4

        elif opcode == 8:
            val1 = self.getParameter(self.position+1, C)
            val2 = self.getParameter(self.position+2, B)
            output = self.getOutputLocation(self.position+3, A)
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
            return self.program.get(self.program.get(pos, 0), 0)
        if type==1:
            return self.program.get(pos, 0)
        if type==2:
            return self.program.get(self.relativeBase+self.program.get(pos, 0), 0)

    def getOutputLocation(self, pos, type):
        if type== 0:
            return self.program.get(pos, 0)
        if type==2:
            return self.program.get(pos, 0)+self.relativeBase

    """Should return the value inputted in the machine"""
    @abstractmethod
    def processInput(self):
        pass


    """Should process the output"""
    @abstractmethod
    def processOutput(self, output):
        pass