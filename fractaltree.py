import pygame as pg
import settings
import math
import random


class FractalTree:
    def __init__(self, display, angle, prob):
        self.recursion = 0
        self.trunks = 1
        self.R = 0
        self.G = 0
        self.B = 255
        self.color = (self.R, self.G, self.B)
        self.angle = angle
        self.probability = prob
        self.trunkwidth = 10
        self.trunkheight = 100
        self.display = display
        self.recursioncomplete = False
        self.endoftrunkx = settings.width / 2
        self.endoftrunky = settings.height - self.trunkheight
        self.heightofbranch = 150
        self.branchlist = []

    def redrawtree(self, angle, prob, color):

        if self.angle != angle or self.probability != prob or self.color != color:
            self.angle = angle
            self.probability = prob
            self.color = color
            self.recursioncomplete = False
            return False

        elif self.angle == angle and self.probability == prob and self.color == color:
            self.recursioncomplete = True
            return True

    def splitprobcalculation(self):

        prob = self.probability/37*10
        if random.randrange(-10, 10, 1) < prob:
            return True
        if random.randrange(-10, 10, 1) > prob:
            return False

        # do stuff
    def setcolor(self, pos, R,G,B):
        if pos > 255:
            pos = 255
        if pos < -255:
            pos = -255
        if pos >= 0:
            if R == 0 and G < 255 and B == 255:
                G = G + pos
            if G >= 255 and B == 255:
                G = 255
                B = B - pos
            if B == 0 and G == 255:
                R = R + pos
            if B == 0 and R >= 255:
                B = 255
                R = 0
                B = 0
            return R, G, B
        if pos < 0 :
            if R == 0 and 0 < G <= 255 and B == 255:
                G = G + pos
            if G <= 0 and B == 255:
                G = 0
                R = self.R - pos
            if R == 255 and self.G == 0:
                B = B + pos
            if B == 0 and R >= 255:
                B = 255
                R = 0
                G = 0
            return R, G, B
    def drawbranches(self, startx, starty, height, angle, width, color):
        oldangle = angle

        if height > 2:
            newx = math.sin(math.radians(angle)) * height + startx
            newy = starty - math.cos(math.radians(angle)) * height
            if height == self.heightofbranch:
                return self.drawbranches(startx, starty, height - 1,angle, int(width), color), \
                self.drawbranches(startx, starty, height - 1, -angle , int(width), color)
            line = pg.draw.line(self.display, self.setcolor(color,self.R, self.G, self.B), (startx, starty),
                                (math.sin(math.radians(angle)) * height + startx, starty -
                                 math.cos(math.radians(angle)) * height), width)

            if height != self.heightofbranch:
                if int(width*2/3) >= 1:
                    return self.drawbranches(newx, newy, height*3/4,oldangle - 20 - 10*(angle /90), int(width*2/3),color + 10), \
                           self.drawbranches(newx, newy, height*3/4, oldangle + 20 - 10*(angle /90), int(width*2/3), color + 10)
                else :
                    return self.drawbranches(newx, newy, height * 3 / 4, oldangle - 20 - 10*(angle /90), 1, color +10 ), \
                           self.drawbranches(newx, newy, height * 3 / 4, oldangle + 20 - 10*(angle /90), 1, color + 10)

    def update(self, angle, color):
        pg.draw.line(self.display, self.setcolor(color, self.R, self.G, self.B), (settings.width / 2, settings.height),
                     (settings.width / 2, settings.height - self.trunkheight), self.trunkwidth)

        self.drawbranches(self.endoftrunkx, self.endoftrunky, self.heightofbranch, angle, self.trunkwidth, color)
        self.recursion = 0
