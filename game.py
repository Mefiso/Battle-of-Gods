import pygame
from pygame.locals import *
from players.battler import Battler

pygame.init()

screen = pygame.display.set_mode((640, 480))
player1 = pygame.image.load('images/sprites/test1.jpeg').convert()
player2 = pygame.image.load('images/sprites/test2.jpeg').convert()
background = pygame.image.load('images/backgrounds/background.jpeg').convert()
elems1 = {'fire': 2, 'water': 3, 'earth': 3, 'air': 1}
elems1 = {'fire': 2, 'water': 3, 'earth': 3, 'air': 1}

screen.blit(background, (0, 0))
battlers = [Battler(player1, (0, 200), elems1, 7), Battler(player2, (500, 200), elems2, 7)]

while True:
    for event in pygame.event.get()

