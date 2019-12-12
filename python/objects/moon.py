class moon:

    def __init__(self, data):
        self.dx = 0
        self.dy = 0
        self.dz = 0
        data = data[1:len(data)-1]
        coords = data.split(", ")
        self.x, self.y, self.z = [int(coord[2:]) for coord in coords]

    def kinetic(self):
        res = 0
        res += abs(self.dx)
        res += abs(self.dy)
        res += abs(self.dz)
        return res

    def potential(self):
        res = 0
        res += abs(self.x)
        res += abs(self.y)
        res += abs(self.z)
        return res

    def applyVelocity(self):
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

    @property
    def velocityZero(self):
        if self.dx ==0 and self.dy == 0 and self.dz == 0:
            return True
        return False

