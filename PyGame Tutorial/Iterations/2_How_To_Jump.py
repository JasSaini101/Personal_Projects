'''In  the second installment, we made some improvements to the barrier
in accordance to the size of the character so not portion can cross into
the void. Along with that we created a jumping mechanic that revolves
around the simple x^2 quadratic equation since that equation follows the
pattern of a jump pretty similarly. Not much else was added but next time
I am going to simplify some lines to make my code look nicer'''


import pygame
pygame.init()  #Initializes the game, ALWAYS DO THIS

screen_size = 500
win = pygame.display.set_mode((screen_size,screen_size)) #Creates our window

pygame.display.set_caption("Practice Moving") 


x = 50
y = 400
width = 40
height = 60
vel = 15

isJump = False
jumpCount = 10

#always make a main loop
run = True
while run:
    pygame.time.delay(100) #milliseconds delay to update game
    
    for event in pygame.event.get(): # All events such as mouse movement
        if event.type == pygame.QUIT: # if the X is clicked
            run = False
            
    keys = pygame.key.get_pressed() # All the keys on our keyboard
    
    if keys[pygame.K_LEFT] and (x > vel): #The key clicked, barrier check, move model
            x -= vel
    if keys[pygame.K_RIGHT] and (x + vel + width < screen_size):
            x += vel
    if not (isJump): #Can't move up/down or jump again while jumping
        if keys[pygame.K_UP] and (y > vel):
                y -= vel
        if keys[pygame.K_DOWN] and (y + vel + height < screen_size):
                y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1 #So the second half of the jump is going downwards
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) / 2 * neg #moving the character according to x^2 equation
            jumpCount -= 1  #decrements the 'x' in our x^2 equation
        else:
            isJump = False
            jumpCount = 10 #resets the variables
            

    win.fill((0,0,0)) #Fills the screen black to erase the old model    
    pygame.draw.rect(win, (255,0,0), (x,y,width, height)) #makes our model
    pygame.display.update() #tels the screen to update
    
pygame.quit() #Closes the window 
    
    
