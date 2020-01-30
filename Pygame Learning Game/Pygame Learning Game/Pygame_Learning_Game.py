"""
import random as r



def generate():
    selector = 1
    
    l = []
    SelectorRange = r.randrange(3,5)
    if selector == 1:
        print("Selected Plus")
        for each in range(2, SelectorRange):
            l.append(each)
            l.append("+")
            print(l)
        answer = ''.join(l)
        
    if selector == 2:
        print("selected minus")

    if selector == 3:
        print("selected multiply")
        

"""

#Imports
import time
import os, sys
import pygame
from pygame.locals import *
import random as r

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
        
class DrawButton:
    def __init__(self, x, y, w, h, btnColor):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.btnColor = btnColor

class generateMathProblem:
    def generate():
        selector = r.randrange(1,3)
        if selector == 1:
            print("Selected Plus")
            
        if selector == 2:
            print("selected minus")

        if selector == 3:
            print("selected multiply")


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

#Classes slut

#Variabler
screenwidth=1500
screenheight=800
green = (0,255,0)#faven goern
red = (255,0,0)#farven raad


#Load billede og saet baggrund
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
    
    Selection = "SeleOne"
    
    running = True
    
    screen.blit(BackGround.image, BackGround.rect)

    triangel(-50, -600)
    triangel(50, 600)
    

    while running == True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if Selection == "SeleOne":
                        print("-1 on ", Selection)
                        Selection = "SeleFour"
                    elif Selection == "SeleFour":
                        print("-1 on ", Selection)
                        Selection = "SeleThree"
                    elif Selection == "SeleThree":
                        print("-1 on ", Selection)
                        Selection = "SeleTwo"
                    elif Selection == "SeleTwo":
                        print("-1 on ", Selection)
                        Selection = "SeleOne"
                    print(Selection)
                

                if event.key == pygame.K_RIGHT:
                    if Selection == "SeleOne":
                        print("+1 on ", Selection)
                        Selection = "SeleTwo"
                    elif Selection == "SeleTwo":
                        print("+1 on ", Selection)
                        Selection = "SeleThree"
                    elif Selection == "SeleThree":
                        print("+1 on ", Selection)
                        Selection = "SeleFour"
                    elif Selection == "SeleFour":
                        print("+1 on ", Selection)
                        Selection = "SeleOne"
                    print(Selection)
                
                if event.key == pygame.K_RETURN:
                    if Selection == "SeleOne":
                        Pl1Answer = "SeleOne"
                    if Selection == "SeleTwo":
                        Pl1Answer = "SeleTwo"
                    if Selection == "SeleThree":
                        Pl1Answer = "SeleThree"
                    if Selection == "SeleFour":
                        Pl1Answer = "SeleFour"
                    
            
        pygame.display.update()
    



main()