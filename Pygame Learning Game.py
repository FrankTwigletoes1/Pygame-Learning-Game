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
    triangle(50, 650)

    Player_1 = Player((screenwidth/2-600), 450, red)
    Player_2 = Player((screenwidth/2+600), 450, green)
    
    while running == True:
        

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                elif event.key == pygame.K_LEFT:
                    Player_1.move(1)

                elif event.key == pygame.K_RIGHT:
                    Player_2.move(1)

        buttons = [screenwidth / 2 - 100 / 2, screenwidth / 2 - 100 / 2 + 105,screenwidth / 2 - 100 / 2 - 105, screenwidth / 2 - 100 / 2 + 210,screenwidth / 2 - 100 / 2 - 210] 
        

        def correct():
            pass
            #print("yes very correct")
            
        
        while alreadyGenerated == False:
            answer = Math.generateQuestion(1,10)
            buttonchoice = r.choice(buttons)
            randomNums = []
            for i in range(0,5):
                randomNums.append(r.randint(answer - 20,answer + 20))
            alreadyGenerated = True

        
        for each in buttons:
            select = r.randint(1,5)
            if select == 1:
                #print("Indsat svar")
                button.btn("{}".format(answer),buttonchoice,screenheight / 2 - 100 / 2 + 200, 100,100,lightblue,green, correct)
            else:
                if each == buttonchoice:
                    pass
                else:
                    #print(randomNums)
                    button.btn("{}".format(randomNums),each,screenheight / 2 - 100 / 2 + 200, 100,100,lightblue,green, None)
                        
        

        pygame.display.update()
        



main()