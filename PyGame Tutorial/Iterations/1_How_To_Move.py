'''In the first installment of the series, Tim taught us how to install
pygame, what it was and the basics of how to start to create a game. In
this code, I learned how to initialize the screen, create a window, create
a character, and move that character throughout the screen. The barriers
of the screen are my own adaption. There are various varaibles around the
code that are very self explanatory and this is a good first step'''

import pygame
pygame.init()  #Initializes the game, ALWAYS DO THIS

screen_size = 500 #variable in case I wanna change the value later and dont ahve to do each one
win = pygame.display.set_mode((screen_size,screen_size)) #Creates our window

pygame.display.set_caption("Practice Moving") 


x = 50
y = 50
width = 40
height = 60
vel = 20

#always make a main loop
run = True
while run:
    pygame.time.delay(100) #milliseconds delay to update game
    
    for event in pygame.event.get(): # All events such as mouse movement
        if event.type == pygame.QUIT: # if the X is clicked
            run = False
            
    keys = pygame.key.get_pressed() # All the keys on our keyboard
    
    if keys[pygame.K_LEFT]: #The key clicked, barrier check, move model
        if(x - vel > 0):
            x -= vel
        
    if keys[pygame.K_RIGHT]:
        if(x + vel + width < screen_size):
            x += vel
        
    if keys[pygame.K_UP]:
        if(y - vel > 0):
            y -= vel
        
    if keys[pygame.K_DOWN]:
        if(y + vel + height < screen_size):
            y += vel
            
    win.fill((0,0,0)) #Fills the screen black to erase the old model    
    pygame.draw.rect(win, (255,0,0), (x,y,width, height)) #makes our model
    pygame.display.update() #tels the screen to update
    
pygame.quit() #Closes the window 
    
    