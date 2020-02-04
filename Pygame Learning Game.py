#Imports
import time
import pygame
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
    global answer
    global question
    
    
    Selection = "SeleOne"
    
    running = True
    
    screen.blit(BackGround.image, BackGround.rect)

    pygame.draw.rect(screen, lightblue,(screenwidth / 2 - 100 / 2, screenheight / 2 - 100 / 2+200, 100,100))
    pygame.draw.rect(screen, lightblue,(screenwidth / 2 - 100 / 2 + 105, screenheight / 2 - 100 / 2+200, 100,100))
    pygame.draw.rect(screen, lightblue,(screenwidth / 2 - 100 / 2 - 105, screenheight / 2 - 100 / 2+200, 100,100))
    pygame.draw.rect(screen, lightblue,(screenwidth / 2 - 100 / 2 + 210, screenheight / 2 - 100 / 2+200, 100,100))
    pygame.draw.rect(screen, lightblue,(screenwidth / 2 - 100 / 2 - 210, screenheight / 2 - 100 / 2+200, 100,100))
    
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
        
        def check():
            print("check")

        answer =  Math.generateQuestion(1,10)
        select = r.randint(1,5)
        
        buttons = [screenwidth / 2 - 100 / 2, screenwidth / 2 - 100 / 2 + 105,screenwidth / 2 - 100 / 2 - 105, screenwidth / 2 - 100 / 2 + 210,screenwidth / 2 - 100 / 2 - 210] 
        
        
        for each in buttons:
            if select == 1:
                print("Indsat svar")
                buttonchoice = r.choice(buttons)
                button.btn("{}".format(answer),buttonchoice,screenheight / 2 - 100 / 2+200, 100,100,lightblue,green, check)
            else:
                print("else")



        pygame.display.update()
    



main()