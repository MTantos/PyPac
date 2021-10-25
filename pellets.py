import numpy as np
import pygame
from vector import Vector
from constants import *

class Pellet(object):
    def __init__(self, row, column):
        self.name = PELLET
        self.position = Vector(column * TILEWIDTH, row * TILEHEIGHT)
        self.colour = WHITE
        self.radius = int(TILEWIDTH >> 3)
        self.collideRadius = int (TILEWIDTH >> 3)
        self.points = 10
        self.visible = True

    def render(self, screen):
        if self.visible:
            adjust = Vector(TILEWIDTH, TILEHEIGHT) / 2
            p = self.position + adjust
            pygame.draw.circle(screen, self.colour, p.asInt(), self.radius)

class PowerPellet(Pellet):
    def __init__(self, row, column):
        Pellet.__init__(self, row, column)
        self.name = POWERPELLET
        self.radius = int(TILEWIDTH >> 1)
        self.points = 50
        self.flashTime = 0.2
        self.timer = 0

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.flashTime:
            self.visible = not self.visible
            self.timer = 0

class PelletGroup(object):
    def __init__(self, pelletfile):
        self.pelletList = []
        self.powerpellets = []
        self.pelletKeys = ['.', '+']
        self.ppKeys = ['P', 'p']
        self.createPelletList(pelletfile)
        self.numEaten = 0

    def update(self, dt):
        for powerpellet in self.powerpellets:
            powerpellet.update(dt)

    def createPelletList(self, pelletfile):
        data = self.readPelletfile(pelletfile)
        for row in range(data.shape[0]):
            for col in range(data.shape[1]):
                if data[row][col] in self.pelletKeys:
                    self.pelletList.append(Pellet(row, col))
                elif data[row][col] in self.ppKeys:
                    pp = PowerPellet(row, col)
                    self.pelletList.append(pp)
                    self.powerpellets.append(pp)

    def readPelletfile(self, textfile):
        return np.loadtxt(textfile, dtype='<U1')
    
    def isEmpty(self):
        return len(self.pelletList) == 0

    def render(self, screen):
        for pellet in self.pelletList:
            pellet.render(screen)
