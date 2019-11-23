import pygame
from pygame.locals import *

class Battler:
    
    def __init__(self, image, (width,height), elems, hp):
        self.image = image
        self.pos = image.get_rect().move(width, height)
        self.elems = { element:power for element, power in elems.items() }
        self.hp = hp
    
    def attack(self, element):
        self.pos = self.pos.move(10, 0)
        return elems[element]
        
    def retreat(self):
        self.pos = self.pos.move(-10, 0)
