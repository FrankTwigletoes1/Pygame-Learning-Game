#Note til selv, øv dig på at bruge fucking pygame.
#Note til selv, øv dig på at bruge fucking pygame.
#Note til selv, øv dig på at bruge fucking pygame.
#Note til selv, øv dig på at bruge fucking pygame.
#Note til selv, øv dig på at bruge fucking pygame.
#Note til selv, øv dig på at bruge fucking pygame.
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
    updateScreen.update(red, green)

    while running == True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: 
                pygame.quit()
                

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    

                elif event.key == pygame.K_LEFT:
                    Player_1.move(10)
                    updateScreen.update(red,green)

                elif event.key == pygame.K_RIGHT:
                    Player_2.move(10)
                    updateScreen.update(red,green)

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
                    button.btn("{}".format(r.choice(randomNums)),each,screenheight / 2 - 100 / 2 + 200, 100,100,lightblue,green, None)

       
# Nah fam, for ellers ville jeg ikke kunne spam skifte teksten
        pygame.display.update()
        

main()