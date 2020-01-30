#Imports
import time
import os, sys
import pygame
from pygame.locals import *
import random as r
from Logic import *
pygame.init()


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

    triangle(-50, -600)
    triangle(50, 600)
    

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