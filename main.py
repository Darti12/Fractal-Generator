import pygame
import math
pi = math.pi
import random
from pygame import gfxdraw

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def divide(self, vector, divisor):
        self.x = int((self.x + vector.x)*divisor)
        self.y = int((self.y + vector.y)*divisor)

class Weird:
    def __init__(self, initialPoints, divisor, screenSize):
        self.divisor = divisor
        self.initialPoints = initialPoints
        self.screenSize = screenSize

        pygame.init()
        pygame.display.set_caption("minimal program")
        self.screen = pygame.display.set_mode(screenSize)

        # Initializes the first point
        self.currentPos = Vector(0,0)

        # start the main loop
        self.main()

    def main(self):        
        while True:
            # draw and choose random director to go
            self.pixel(self.currentPos.x, self.currentPos.y)
            self.currentPos.divide(random.choice(self.initialPoints), self.divisor)
            pygame.display.update()

            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    pygame.quit()


    def pixel(self, x, y):
        gfxdraw.pixel(self.screen, x, y, (int((x/screenSize[0])*255),int((y/screenSize[1])*255),0))


def PointsInCircum(r, screenSize, n=100):
    return [Vector(math.cos(2*pi/n*x)*r + int(screenSize[0]/2),math.sin(2*pi/n*x)*r + int(screenSize[1]/2)) for x in range(0,n+1)]

if __name__=="__main__":
    points = []
    screenSize = (1850,1010)

    print("This program draw weird shapes based on some points and a divisor value")
    i = input("Enter amount of points: ")
    points = PointsInCircum(int(screenSize[1]/2), screenSize, int(i))

    divisor = float(input("Enter divisor value between 0 and 1: "))

    sim = Weird(points, divisor, screenSize)