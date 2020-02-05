#Imports
import time
import pygame
import random as r
from Logic import *
pygame.init()


def main(alreadyGenerated=False):
    global Background
    global screen
    global screenwidth
    global screenheight
    global green
    global red
    global answer
    global question
    
    
    
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
        buttons = [screenwidth / 2 - 100 / 2, screenwidth / 2 - 100 / 2 + 105,screenwidth / 2 - 100 / 2 - 105, screenwidth / 2 - 100 / 2 + 210,screenwidth / 2 - 100 / 2 - 210] 
        

        def correct():
            print("yes very correct")
            alreadyGenerated = False
        
        if alreadyGenerated == False:
            answer =  Math.generateQuestion(1,10)
            buttonchoice = r.choice(buttons)
            global buttonchoice
            print("hallo")
            
        
        
        
        
        
        for each in buttons:
            select = r.randint(1,5)
            if select == 1:
                print("Indsat svar")
                button.btn("{}".format(answer),buttonchoice,screenheight / 2 - 100 / 2+200, 100,100,lightblue,green, correct)
            else:
                for each in buttons:
                    if each == buttonchoice:
                        pass
                    else:
                        button.btn("{}".format(r.randint(answer-20,answer+20)),each,screenheight / 2 - 100 / 2+200, 100,100,lightblue,green, None)
                        
                        
        

        pygame.display.update()
        



main()