import pygame
import random as r


class point:
    def __init__(self,x,y,color):
        self.x = x;
        self.y = y;
        self.color = color;
        self.radius = 5;


    def draw(self, surface):
        pygame.draw.circle(surface,self.color,(self.x,self.y),self.radius)

    def drawtopoint(self,screen,outr):
        pygame.draw.line(screen,self.color,(self.x,self.y),(outr.x,outr.y))

