from objects.computers.intCodeComputer import intCodeComputer

class TESTComputer(intCodeComputer):

    def __init__(self, program):
        self.inputCode = 0
        super().__init__(program)

    def processInput(self):
        return self.inputCode

    def processOutput(self, output):
        if output != 0:
            print(output)

    def setInput(self, input):
        self.inputCode = input
