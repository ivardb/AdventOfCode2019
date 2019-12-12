from objects.computers.intCodeComputer import intCodeComputer

class BOOSTComputer(intCodeComputer):
    def __init__(self, program):
        self.inputCode = 0
        super().__init__(program)

    def processInput(self):
        return self.inputCode

    def processOutput(self, output):
        print(output)

    def setInput(self, input):
        self.inputCode = input