import math

class chemical:

    def __init__(self, name, chemicalList):
        self.chemicalList = chemicalList
        self.name = name
        self.createdQuantity = 0
        self.stored = 0
        self.ingredients = list()

    def addIngredient(self, name, quantity):
        self.ingredients.append((name, quantity))

    def getComponent(self, amount):
        if self.name== "ORE":
            return amount
        oreUsed = 0
        if self.stored<amount:
            reactionsNeeded = math.ceil((amount-self.stored)/self.createdQuantity)
            for ing in self.ingredients:
                oreUsed += self.chemicalList.get(ing[0]).getComponent(ing[1]*reactionsNeeded)
            self.stored+=self.createdQuantity*reactionsNeeded
        self.stored -= amount
        return oreUsed