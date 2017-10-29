# -*- coding: utf-8 -*-


class movement:

    def __init__(self):
        #a 5X5 grid in which the map can be drawn
        self.mapgrid = []
        for i in range(0, 25):
            self.mapgrid.append('@')

    def drawmap(self):
            print " ".join(map(str, self.mapgrid[0:5]))
            print " ".join(map(str, self.mapgrid[5:10]))
            print " ".join(map(str, self.mapgrid[10:15]))
            print " ".join(map(str, self.mapgrid[15:20]))
            print " ".join(map(str, self.mapgrid[20:25]))

    def walk(self):
        currentPos = 12  # as a placeholder. 12 is the center
        self.mapgrid[currentPos] = '#'
        self.drawmap()

movement()
