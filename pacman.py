import pygame
# locals are needed for QUIT and exit()
from pygame.locals import *


# initialize pygame
pygame.init()

#create a window screen
screen = pygame.display.set_mode((600,400),0,32)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      exit()
  pygame.display.update()
