import pygame as pg
import settings



class Pointer(pg.sprite.Sprite):
    def __init__(self, posx, posy, screen):
        pg.sprite.Sprite.__init__(self)
        self.dragging = False
        self.width = settings.pointerwidth
        self.height = settings.pointerheight
        self.triangleH = self.height%2 + (self.height - self.height%2)/2
        self.posx = posx
        self.posy = posy
        self.originalposx = posx
        self.originalposy = posy
        self.maxtravel = 0
        self.rect = pg.draw.rect(screen, settings.black, (self.posx, self.posy, self.width, self.height))
        self.rect.x = posx
        self.rect.y = posy
        self.smallrect = pg.draw.rect(screen, settings.white, (self.posx + self.width/2 -1, self.posy + 1, 2, self.height - 2))
        self.screen = screen

    def collidepoint(self, posx, posy):
        if (self.posx <= posx <= self.posx + self.width) and (self.posy <= posy <= self.posy + self.height):
            return True
        else:
            return False
    def settravel(self, distance):
        self.maxtravel = distance/2
    def travelonslider(self, posx):
        if posx > self.originalposx + self.maxtravel:
            self.posx = self.originalposx + self.maxtravel

        if posx < self.originalposx - self.maxtravel:
            self.posx = self.originalposx - self.maxtravel
        if self.originalposx - self.maxtravel <= posx <= self.originalposx + self.maxtravel:
            self.posx = posx

    def update(self, posx, posy):
        self.travelonslider(posx)
        self.rect = pg.draw.rect(self.screen, settings.black, (self.posx, self.originalposy, self.width, self.height))
        self.smallrect = pg.draw.rect(self.screen, settings.white,
                                      (self.posx + self.width / 2 - 1, self.originalposy + 1, 2, self.height - 2))


        self.posy = self.originalposy

    def getvalue(self):
            return self.posx - self.originalposx

    def getangle(self):
        return (self.posx - self.originalposx)*2.4
    def getcolor(self):
        return self.getvalue()*6.8
    def mouvepointer(self, Xpos):
        self.posx = Xpos