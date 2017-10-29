# -*- coding: utf-8 -*-


class mapControl:

    def __init__(self):
        #a 5X5 grid in which the map can be drawn
        self.mapgrid = []
        self.currentPos = 12  # as a placeholder. 12 is the center
        for i in range(0, 25):
            self.mapgrid.append('@')

    def drawmap(self):
            print " ".join(map(str, self.mapgrid[0:5]))
            print " ".join(map(str, self.mapgrid[5:10]))
            print " ".join(map(str, self.mapgrid[10:15]))
            print " ".join(map(str, self.mapgrid[15:20]))
            print " ".join(map(str, self.mapgrid[20:25]))

    def walk(self, direction):
        error = False
        if direction == 'north':
            if self.currentPos > 5:
                self.currentPos = self.currentPos - 5
            else:
                print "Placeholder text."
                error = True
        elif direction == 'south':
            self.currentPos = self.currentPos + 5
        elif direction == 'east':
            self.currentPos = self.currentPos + 1
        elif direction == 'west':
            self.currentPos = self.currentPos - 1
        self.mapgrid[self.currentPos] = '#'
        if error is False:
            self.drawmap()

mapControl()
