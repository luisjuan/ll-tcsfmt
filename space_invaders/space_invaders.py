
import pygame, sys, time
from pygame.locals import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()                      #initialize pygame

pygame.mouse.set_visible(0)

ship = pygame.image.load("images/ship.png")
ship = pygame.transform.scale(ship,(int(ship.get_width()/2),int(ship.get_height()/2)))
ship_top = screen.get_height() - ship.get_height() - 10
ship_left = screen.get_width()/2 - ship.get_width()/2
shipSpeed = 6

shot = pygame.draw.rect(screen,(0,255,0),(100,100,3,15))
shootSpeed = 10
shoot_y = 0 # top of the screen
shootSound = pygame.mixer.Sound(file="sounds/shoot.wav")

alien1 = pygame.image.load("images/alien_1a.png")
print(ship.get_width()/2)
alien1 = pygame.transform.scale(alien1,(50,50))
fastInvader_s1 = pygame.mixer.Sound(file="sounds/fastinvader1.wav")
fastInvader_s2 = pygame.mixer.Sound(file="sounds/fastinvader2.wav")
alienSpeed = 10
alien_x=100
alien_direction = 1
# place ship
tick_count=0
turn = 0

def playAlienInvasionSound(turn):
    if turn==0:
        fastInvader_s1.play()
    else:
        fastInvader_s2.play()        
    turn=abs(turn-1)
    return turn

alienTopRow1=[1,1,1,1,1,1,1,1,1,1,1]
alienTopRow2=[1,1,1,1,1,1,1,1,1,1,1]
alienMiddleRow1=[1,1,1,1,1,1,1,1,1,1,1]
def findRightMostAlien(alienRow):
    return int(max(loc for loc, val in enumerate(alienRow) if val == 1))


while True:
    tick_count += clock.tick(80)
    #print(tick_count)
    pygame.display.update()

    screen.fill ((0,0,0)) #refresh the screen
    screen.blit(ship, (ship_left-ship.get_width()/2, ship_top))

    outerRight=findRightMostAlien(alienTopRow1)*60

    for c,alienNum in enumerate(alienTopRow1):
        screen.blit(alien1,(alien_x+c*60,100))
    for c,alienNum in enumerate(alienTopRow2):
        screen.blit(alien1,(alien_x+c*60,160))
    for c,alienNum in enumerate(alienMiddleRow1):
        screen.blit(alien1,(alien_x+c*60,220))
        
    if tick_count > 750:
        if alien_x+outerRight > 730:
            alien_direction = -1
        elif alien_x < 50:
            alien_direction=1
        alien_x += (alien_direction* alienSpeed)
        tick_count=0
        
        turn=playAlienInvasionSound(turn)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[K_LEFT]:
        if ship_left > 30:
            ship_left -= shipSpeed
    if pressed[K_RIGHT]:
        if ship_left < 770:
            ship_left += shipSpeed
    if pressed[K_SPACE] and shoot_y <=0:
        shootSound.play()
        shoot_y = ship_top
        shoot_x = ship_left
    if shoot_y > 0:
        pygame.draw.rect(screen,(0,255,0),(shoot_x,shoot_y,3,15))
        shoot_y -= shootSpeed

    
