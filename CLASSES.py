import pygame
import random as r


class point:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;


    def draw(self, surface, color,radius ):
        pygame.draw.circle(surface,color,(self.x,self.y),radius)


