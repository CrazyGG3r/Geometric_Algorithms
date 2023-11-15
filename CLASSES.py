import pygame
import random as r


class point:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 10
        self.completed = True


    def draw(self, surface):
        pygame.draw.circle(surface,self.color,(self.x,self.y),self.radius)

    def drawtopoint(self,screen,outr):
        pygame.draw.line(screen,self.color,(self.x,self.y),(outr.x,outr.y))

class line:
    def __init__(self,w,duration,color):
        self.w = w
        self.duration = duration
        self.elapsed = 0
        self.color = color;

    def update(self,dt):
        self.elapsed +=dt
        if self.elapsed >= self.duration:
            self.elapsed = self.duration
            self.completed = False
        else:
            self.completed = True

    def draw(self,screen,point1,point2):
        if point1.x == point2.x and point1.y == point2.y:
            self.elapsed = self.duration
            
        else:
            progress = self.elapsed / self.duration
            current_x = int(point1.x + (point2.x - point1.x) * progress)
            current_y = int(point1.y + (point2.y - point1.y) * progress)
            pygame.draw.line(screen, self.color, (point1.x,point1.y),(current_x, current_y), self.w)



