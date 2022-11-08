import pygame
import random

class wowAmazingObject:
    def __init__(self):
        self.speed = 50
        self.acceleration = 1.1
    # Gjør matte
    def speedy(self, time):
        return self.speed * self.acceleration * time


class coolObject:
    def __init__(self):
        wowAmazingObject.__init__(self)
    def manyPrints(self, loops):
        # printer loops ganger
        for i in range(loops):
            print(wowAmazingObject().speedy(i))

coolObject().manyPrints(50)