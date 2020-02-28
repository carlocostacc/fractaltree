import pygame as pg
import settings
from pointer import Pointer

class Rail(pg.sprite.Sprite):
    def __init__(self, posx, posy,screen):
        pg.sprite.Sprite.__init__(self)
        self.height = 3
        self.width = settings.railwidth
        self.posx = posx
        self.posy = posy
        self.rail = pg.draw.rect(screen, settings.black, (self.posx, self.posy, self.width, self.height))
        self.screen = screen


    def update(self):
        x = 0
        self.rail = pg.draw.rect(self.screen, settings.black, (self.posx, self.posy, self.width, self.height))
