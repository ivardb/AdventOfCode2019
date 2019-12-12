class amplifier:

    def __init__(self, program, phase, name):
        self.program = program
        self.position = 0
        self.phase = phase
        self.name = name
        self.input = -1
        self.firstInput = True
        self.next = None

    def process(self):
        while True:
            advance = self.processCode()
            if advance == -1:
                if self.name == "E":
                    return
                return self.next.process()
            elif advance == -2:
                self.next.process()
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
            if C == 0:
                val1 = self.program[self.program[self.position + 1]]
            else:
                val1 = self.program[self.position + 1]
            if B == 0:
                val2 = self.program[self.program[self.position + 2]]
            else:
                val2 = self.program[self.position + 2]
            output = self.program[self.position + 3]
            self.program[output] = val1 + val2
            return 4
        elif opcode == 2:
            if C == 0:
                val1 = self.program[self.program[self.position + 1]]
            else:
                val1 = self.program[self.position + 1]
            if B == 0:
                val2 = self.program[self.program[self.position + 2]]
            else:
                val2 = self.program[self.position + 2]
            output = self.program[self.position + 3]
            self.program[output] = val1 * val2
            return 4
        elif opcode == 3:
            if self.firstInput:
                self.program[self.program[self.position + 1]] = self.phase
            else:
                if self.input == -1:
                    return -2
                self.program[self.program[self.position + 1]] = self.input
                self.input = -1
            self.firstInput = False
            return 2
        elif opcode == 4:
            par1 = self.program[self.position + 1]
            if C == 0:
                self.next.input = self.program[par1]
            else:
                self.next.input = par1
            return 2
        elif opcode == 5:
            if C == 0:
                val1 = self.program[self.program[self.position + 1]]
            else:
                val1 = self.program[self.position + 1]
            if B == 0:
                val2 = self.program[self.program[self.position + 2]]
            else:
                val2 = self.program[self.position + 2]
            if val1!=0:
                self.position = val2
                return 0
            else:
                return 3
        elif opcode == 6:
            if C == 0:
                val1 = self.program[self.program[self.position + 1]]
            else:
                val1 = self.program[self.position + 1]
            if B == 0:
                val2 = self.program[self.program[self.position + 2]]
            else:
                val2 = self.program[self.position + 2]
            if val1==0:
                self.position = val2
                return 0
            else:
                return 3
        elif opcode == 7:
            if C == 0:
                val1 = self.program[self.program[self.position + 1]]
            else:
                val1 = self.program[self.position + 1]
            if B == 0:
                val2 = self.program[self.program[self.position + 2]]
            else:
                val2 = self.program[self.position + 2]
            output = self.program[self.position+3]
            if val1<val2:
                self.program[output] = 1
            else:
                self.program[output] = 0
            return 4
        elif opcode == 8:
            if C == 0:
                val1 = self.program[self.program[self.position + 1]]
            else:
                val1 = self.program[self.position + 1]
            if B == 0:
                val2 =self.program[self.program[self.position + 2]]
            else:
                val2 = self.program[self.position + 2]
            output = self.program[self.position+3]
            if val1==val2:
                self.program[output] = 1
            else:
                self.program[output] = 0
            return 4
        elif opcode == 99:
            return -1