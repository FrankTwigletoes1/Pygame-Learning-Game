#Imports
import time
import os, sys
import pygame
from pygame.locals import *

pygame.init()

#Check
if not pygame.font: 
    print('Fonts blev ikke importeret')




#Classes
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, screenwidth, screenheight, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (screenwidth,screenheight))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
class Menu():
    def __init__(self):
        print("Menu")


class Player():
    def __init__(self, x_pos, y_pos, w, h):
        self.x = x_pos
        self.y = y_pos
        self.w = w
        self.h = h
        self.color = (255,0,0)
    
    def move(self, direction, steps):
        if direction == right:
            print("right")
            self.x += 10

        elif direction == up:
            print("up")
            self.y += 10

#Classes slut

#Variabler
screenwidth=1500
screenheight=800
green = (0,255,0)#faven gÃ¸rn
red = (255,0,0)#farven rÃ¸d

#Load billede og sÃ¦t baggrund
BackGround = Background('background.png',screenwidth,screenheight, [0,0])
screen = pygame.display.set_mode((screenwidth,screenheight))


def triangel(Xspacer_1, Xspacer_2):
    global BackGround
    global screen
    global screenwidth
    global screenheight
    global green
    global red
    
    pygame.draw.polygon(screen, green, (((screenwidth/2)+Xspacer_1,100),((screenwidth/2)+Xspacer_1,500),((screenwidth/2)+Xspacer_2,500)))
    if Xspacer_1 < 0:
        pygame.draw.rect(screen,red,((screenwidth/2+Xspacer_1-40),460, 40, 40))
    else:
        pygame.draw.rect(screen,red,((screenwidth/2+Xspacer_1),460, 40, 40))
    

def main():
    global Background
    global screen
    global screenwidth
    global screenheight
    global green
    global red
    running = True


    
    screen.blit(BackGround.image, BackGround.rect)

    triangel(-50, -600)
    triangel(50, 600)

    while running == True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
    



main()