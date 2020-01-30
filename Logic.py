import time
import os, sys
import pygame
from pygame.locals import *
import random as r
#Check
if not pygame.font: 
    print('Fonts blev ikke importeret')



#Variabler
screenwidth=1500
screenheight=800
green = (0,255,0)
red = (255,0,0)


#Classes
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, screenwidth, screenheight, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (screenwidth,screenheight))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
class DrawButton:
    def __init__(self, x, y, w, h, btnColor):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.btnColor = btnColor

#class Math:
#    def generate(self, LowestValue, highestValue, Lenght):
#        selector = r.randrange(1,3)
#        x = r.randrange(2,Length)
#        answer = []
#        
#        if selector == 1:
#            print("plus")
#            for each in range(1,x):
#                num = r.randint()
#        elif selector == 2:
#            print("minus")
#        elif selector == 3:
#            print("multiply")
#    
#    def Confirm(self, test="hallo"):
#        print(test)


class Player():
    def __init__(self, x_pos, y_pos, w, h):
        self.x = x_pos
        self.y = y_pos
        self.w = w
        self.h = h
        self.color = (255,0,0)
    
    def move_right(self, steps):
        self.x += 10
        print("right", self.x," ", self.y)

    def move_up(self, steps):
        self.y += 10
        print("up",self.x ," ", self.y)


BackGround = Background('background.png',screenwidth,screenheight, [0,0])

screen = pygame.display.set_mode((screenwidth,screenheight))

class triangle:
    def __init__(self, Xspacer_1, Xspacer_2):
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
