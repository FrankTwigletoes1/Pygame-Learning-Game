import time
import pygame
import random as r


 

#Variabler
screenwidth=1500
screenheight=800
green = (0,255,0)
red = (255,0,0)
lightblue = (0,162,232)
darkblue = (21,21,255)
x_pos_1 = (screenwidth / 2 - 600)
x_pos_2 = (screenwidth / 2 + 600)
y_pos_1 = 450
y_pos_2 = 450
question = True



#Classes
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, screenwidth, screenheight, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (screenwidth,screenheight))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('background.png',screenwidth,screenheight, [0,0])
screen = pygame.display.set_mode((screenwidth,screenheight))
  
        
class button:
    def text_objects(text, font):
        textSurface = font.render(text, True, (0,0,0))
        return textSurface, textSurface.get_rect()

    def btn(msg,x,y,w,h,iColor,aColor, funk=None):
        mousepos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mousepos[0] > x and y+h > mousepos[1] > y:
            pygame.draw.rect(screen, aColor,(x,y,w,h))
            if click[0] == 1 and funk != None:
                print("clicked ", click)
                funk()
        else:
            pygame.draw.rect(screen, iColor,(x,y,w,h))

        smallText = pygame.font.SysFont("bitstreamverasans",20)
        textSurf, textRect = button.text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        screen.blit(textSurf, textRect)

 

class Math:
    def generateQuestion(LowestValue, highestValue):
        num1 = r.randint(LowestValue, highestValue)
        num2 = r.randint(LowestValue, highestValue)
        selector = r.randint(1,3)
        
        if selector == 1:
            print("plus")
            question = ("Hvad er " + str(num1) +  " + " + str(num2))
            answer = num1 + num2

        if selector == 2:
            print("minus")
            question = ("Hvad er " + str(num1) +  " - " + str(num2))
            answer = num1 - num2

        if selector == 3:
            print("gange")
            question = ("Hvad er " + str(num1) +  " * " + str(num2))
            answer = num1 * num2
        return answer
        
class Player():
    def __init__(self, x_pos, y_pos, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        pygame.draw.rect(screen, color,(self.x_pos, self.y_pos, 50, 50))

    def move(self, steps):

        if self.y_pos <= 100:
            print("Du vandt")

        elif self.x_pos == screenwidth/2+50 or self.x_pos == screenwidth/2-100:
            self.y_pos += -10
            print("up",self.x_pos ," ", self.y_pos)

        elif self.x_pos < screenwidth/2:
            self.x_pos += 10
            print("right", self.x_pos," ", self.y_pos)

        elif self.x_pos > screenwidth/2:
            self.x_pos += -10
            print("right", self.x_pos," ", self.y_pos)

        else:
            print("error")


class triangle:
    def __init__(self, Xspacer_1, Xspacer_2):
        pygame.draw.polygon(screen,  lightblue, (((screenwidth/2)+Xspacer_1,100),((screenwidth/2)+Xspacer_1,500),((screenwidth/2)+Xspacer_2,500)))
        if Xspacer_1 < 0:
            pygame.draw.rect(screen,darkblue,((screenwidth/2+Xspacer_1-40),460, 40, 40))
        else:
            pygame.draw.rect(screen,darkblue,((screenwidth/2+Xspacer_1),460, 40, 40))
        #triangle_1(-50, -600)
        #triangle_2(50, 650)
