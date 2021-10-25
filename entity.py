import pygame
from pygame.locals import *
from random import randint
from vector import Vector
from constants import *

class Entity(object):
    def __init__(self, node):
        self.name = None
        self.directions = {STOP:Vector(),UP:Vector(0,-1),DOWN:Vector(0,1),LEFT:Vector(-1,0),RIGHT:Vector(1,0)}
        self.direction = STOP
        self.setSpeed(100)
        self.radius = 10
        self.collideRadius = 5
        self.colour = WHITE
        self.node = node
        self.setPosition()
        self.target = node
        self.visible = True
        self.disablePortal = False
        self.goal = None
        self.directionMethod = self.randomDirection

    def setPosition(self):
        self.position = self.node.position.copy()

    def update(self, dt):
        self.position += self.directions[self.direction]*self.speed*dt
        if self.overshotTarget():
            self.node = self.target
            directions = self.validDirections()
            direction = self.directionMethod(directions)
            if not self.disablePortal:
                if self.node.neighbours[PORTAL] is not None:
                    self.node = self.node.neighbours[PORTAL]
            self.target = self.getNewTarget(direction)
            if self.target is not self.node:
                self.direction = direction
            else:
                self.target = self.getNewTarget(self.direction)
            self.setPosition()

    def validDirection(self, direction):
        if direction is not STOP:
            if self.node.neighbours[direction] is not None:
                return True
        return False

    def getNewTarget(self, direction):
        if self.validDirection(direction):
            return self.node.neighbours[direction]
        return self.node

    def overshotTarget(self):
        if self.target is not None:
            vec1 = self.target.position - self.node.position
            vec2 = self.position - self.node.position
            node2Target = vec1.magnitudeSquared()
            node2Self = vec2.magnitudeSquared()
            return node2Self >= node2Target
        return False

    def reverseDirection(self):
        self.direction = -self.direction
        temp = self.node
        self.node = self.target
        self.target = temp
        
    def oppositeDirection(self, direction):
        if direction is not STOP:
            if direction == -self.direction:
                return True
        return False

    def validDirections(self):
        directions = []
        for key in [UP, DOWN, LEFT, RIGHT]:
            if self.validDirection(key):
                if key != -self.direction:
                    directions.append(key)
        if len(directions) == 0:
            directions.append(-self.direction)
        return directions

    def randomDirection(self, directions):
        return directions[randint(0, len(directions)-1)]

    def setSpeed(self, speed):
        self.speed = speed * TILEWIDTH / 16

    def render(self, screen):
        if self.visible:
            p = self.position.asInt()
            pygame.draw.circle(screen, self.colour, p, self.radius)
