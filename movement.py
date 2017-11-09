# -*- coding: utf-8 -*-


class mapControl:

    def __init__(self):
        #a 5X5 grid in which the map can be drawn
        self.mapgrid = []
        for i in range(0, 25):
            self.mapgrid.append('@')

    def drawmap(self, currentPos):
            self.mapgrid[currentPos] = '#'
            a = " ".join(map(str, self.mapgrid[0:5]))
            b = " ".join(map(str, self.mapgrid[5:10]))
            c = " ".join(map(str, self.mapgrid[10:15]))
            d = " ".join(map(str, self.mapgrid[15:20]))
            e = " ".join(map(str, self.mapgrid[20:25]))
            printableMap = a + '\n' + b + '\n' + c + '\n' + d + '\n' + e
            return printableMap

    def walk(self, direction, currentPos):
        if direction == 'north':
            if currentPos > 5:
                currentPos = currentPos - 5
            else:
                currentPos = currentPos + 20
        elif direction == 'south':
            if currentPos < 20:
                currentPos = currentPos + 5
            else:
                currentPos = currentPos - 20
        elif direction == 'east':
            if currentPos in (4, 9, 14, 19, 24):
                currentPos = currentPos - 4
            else:
                currentPos = currentPos + 1
        elif direction == 'west':
            if currentPos in (0, 5, 10, 15, 20):
                currentPos = currentPos + 4
            else:
                currentPos = currentPos - 1
        return currentPos

mapControl()

