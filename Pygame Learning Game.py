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
        
 
class Button:
    def __init__(self, rect, command, **kwargs):
        self.process_kwargs(kwargs)
        self.rect = pg.Rect(rect)
        self.image = pg.Surface(self.rect.size).convert()
        self.function = command
        self.text = self.font.render(self.text,True,self.font_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)
         
    def process_kwargs(self, kwargs):
        settings = {
            'color'         :pg.Color('red'),
            'text'          :'default',
            'font'          :pg.font.SysFont('Arial', 16),
            'hover_color'   :(200,0,0),
            'font_color'    :pg.Color('white'),
        }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("{} has no keyword: {}".format(self.__class__.__name__, kwarg))
        self.__dict__.update(settings)
 
    def get_event(self):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click()
 
    def on_click(self):
        if self.is_hovering():
            self.function()
             
    def is_hovering(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            return True
 
    def draw(self, surf):
        if self.is_hovering():
            self.image.fill(self.hover_color)
        else:
            self.image.fill(self.color)
        surf.blit(self.image, self.rect)
        surf.blit(self.text, self.text_rect)
    
        


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
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.update()
    



main()