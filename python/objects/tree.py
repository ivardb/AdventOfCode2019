import collections
import numpy as np

import days.config as c

class Tree:

    def __init__(self, grid, distance, position, keys, doors):
        self.grid = grid
        self.distance = distance
        self.position = position
        self.children = list()
        self.keys = keys
        self.doors = doors


    def createChildren(self):
        result = self.bfs(self.position, self.keys, self.doors)
        for object, dist, position in result:
            ckey = set(self.keys)
            cnode = set(self.doors)
            if object.islower():
                ckey.add(object)
            if object.isupper():
                cnode.add(object)
            cTree = Tree(self.grid, dist+self.distance, position, ckey, cnode)
            self.children.append(cTree)
            if len(cTree.keys) != c.amountOfKeys:
                if cTree.distance<c.minimum:
                    cTree.createChildren()
            else:
                if cTree.distance < c.minimum:
                    c.minimum = cTree.distance


    def bfs(self, position, keys, doors):
        seen = set()
        seen.add(position)
        queue = collections.deque()
        queue.append(position)
        result = list()
        distances = np.zeros(self.grid.shape)
        while queue:
            current = queue.popleft()
            x = current[0]
            y = current[1]
            for newX, newY in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                value = self.grid[newY, newX]
                if value != '#' and (newX, newY) not in seen:
                    distances[newY, newX] = distances[y, x] + 1
                    seen.add((newX, newY))
                    if value=='.' or value=='@':
                        queue.append((newX, newY))
                    elif value.islower():
                        if value not in keys:
                            result.append((value, distances[newY, newX], (newX, newY)))
                        else:
                            queue.append((newX, newY))
                    elif value.isupper():
                        if value not in doors:
                            if value.lower() in keys:
                                result.append((value, distances[newY, newX], (newX, newY)))
                        else:
                            queue.append((newX, newY))
        return result