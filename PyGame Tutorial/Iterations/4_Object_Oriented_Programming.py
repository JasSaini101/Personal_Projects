'''Nothing was changed in terms of the game. The code was cleaned up.
Essentially, since we want to make a complex game, the style of coding being done
is not optimal. Object Oriented Program with classes that have attributes are much
better because gloabl varibales aren;t needed and everything is much cleaner and
easier to take care of. I also cleaned p the code in ways that I liked.'''


import pygame
pygame.init()  #Initializes the game, ALWAYS DO THIS

screen_size = 480
win = pygame.display.set_mode((screen_size,screen_size)) #Creates our window

pygame.display.set_caption("Object Oriented Program") 

walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'), pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'), pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png')]
walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'), pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'), pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png')]
bg = pygame.image.load('images/bg.jpg')
char = pygame.image.load('images/standing.png')  # Making variables for the images so it is easier to call them

clock = pygame.time.Clock() # Starting a clock for thje game so I can implement framerates

class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        
    def draw(self,win):
        if self.walkCount + 1 >= 27: #resets the walk count which is the index of our image traversal list
            self.walkCount = 0
        
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y)) #integer division so our index is never a decimal
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x,self.y))
        
def redrawGameWindow():
    win.blit(bg, (0,0))  #This is how you draw something in pygame, arg1 = image, arg2 = tuple of coordinates to put the image
    man.draw(win)      
    pygame.display.update() #tells the screen to update


#always make a main loop
man = player(300, 410, 64, 64)
run = True
while run:
    clock.tick(27) #Frame Rate

    for event in pygame.event.get(): # All events such as mouse movement
        if event.type == pygame.QUIT: # if the X is clicked
            run = False
            
    keys = pygame.key.get_pressed() # All the keys on our keyboard
    
    if keys[pygame.K_LEFT] and (man.x > man.vel): #The key clicked, barrier check, move model
        man.x -= man.vel
        man.left = True #self explanatory varibales, can have Left and Right both be True
        man.right = False
    elif keys[pygame.K_RIGHT] and (man.x + man.vel + man.width < screen_size):
        man.x += man.vel
        man.left = False
        man.right = True
    else:
        man.left = False
        man.right = False
        man.walkCount = 0
        
    if not (man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
    else:
        if man.jumpCount >= -10:
            neg = 1 #So the second half of the jump is going downwards
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) / 2 * neg #moving the character according to x^2 equation
            man.jumpCount -= 1  #decrements the 'x' in our x^2 equation
        else:
            man.isJump = False
            man.jumpCount = 10 #resets the variables
            
    redrawGameWindow() #calls the finction that is incharge of all the drawing in the game every time the loop runs
    
pygame.quit() #Closes the window 
