# -*- coding: utf-8 -*-
from os import system


class mapControl:

    def __init__(self):
        #a 5X5 grid in which the map can be drawn
        self.mapgrid = []
        for i in range(0, 25):
            self.mapgrid.append('@')

    def drawmap(self, currentPos):
            system('clear')
            self.mapgrid[currentPos] = '#'
            print " ".join(map(str, self.mapgrid[0:5]))
            print " ".join(map(str, self.mapgrid[5:10]))
            print " ".join(map(str, self.mapgrid[10:15]))
            print " ".join(map(str, self.mapgrid[15:20]))
            print " ".join(map(str, self.mapgrid[20:25]))

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

