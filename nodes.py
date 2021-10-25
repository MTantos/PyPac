import pygame
from vector import Vector
from constants import *

class Node(object):
    def __init__(self, x, y):
        self.position = Vector(x, y)
        self.neighbours = {UP:None, DOWN:None, LEFT:None, RIGHT:None}

    def render(self, screen):
        for key in self.neighbours.keys():
            if self.neighbours[key] is not None:
                line_start = self.position.asTuple()
                line_end = self.neighbours[key].position.asTuple()
                pygame.draw.line(screen, WHITE, line_start, line_end, 4)
                pygame.draw.circle(screen, RED, self.position.asInt(), 12)

class NodeGroup(object):
    def __init__(self):
        self.nodeList = []

    def setupTestNodes(self):
        nodeA = Node(80 ,80)
        nodeB = Node(160, 80)
        nodeC = Node(80, 160)
        nodeD = Node(160, 160)
        nodeE = Node(208, 160)
        nodeF = Node(80, 320)
        nodeG = Node(208, 320)
        nodeA.neighbours[RIGHT] = nodeB
        nodeA.neighbours[DOWN] = nodeC
        nodeB.neighbours[LEFT] = nodeA
        nodeB.neighbours[DOWN] = nodeD
        nodeC.neighbours[UP] = nodeA
        nodeC.neighbours[RIGHT] = nodeD
        nodeC.neighbours[DOWN] = nodeF
        nodeD.neighbours[UP] = nodeB
        nodeD.neighbours[LEFT] = nodeC
        nodeD.neighbours[RIGHT] = nodeE
        nodeE.neighbours[LEFT] = nodeD
        nodeE.neighbours[DOWN] = nodeG
        nodeF.neighbours[UP] = nodeC
        nodeF.neighbours[RIGHT] = nodeG
        nodeG.neighbours[UP] = nodeE
        nodeG.neighbours[LEFT] = nodeF
        self.nodeList = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG]

    def render(self, screen):
        for node in self.nodeList:
            node.render(screen)
