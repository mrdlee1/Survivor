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
        error = False
        if direction == 'north':
            if currentPos > 5:
                currentPos = currentPos - 5
            else:
                print "Placeholder text."
                error = True
        elif direction == 'south':
            currentPos = currentPos + 5
        elif direction == 'east':
            currentPos = currentPos + 1
        elif direction == 'west':
            currentPos = currentPos - 1
        if error is False:
            return currentPos

mapControl()

