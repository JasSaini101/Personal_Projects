'''In this update, I actually practiced a lot of things I am either uncomfortable or unfamiliar with.
For starters, I downloaded images of a sprite and bachground from the internet that I put in a folder
called images in this directory. It must be in the same directory so I can create a path to the images.
I did not get images for up and down so I made the sprite unable to move in those directions from now on.
The images of walking left and right are in lists, so the program takes the next picture of what a moving
character would look like. Also removed the drawing from the main loop because the best practice is to have
all the drawing done in a function that is called in the mainloop so for me it is redrawGameWindow that handles
the drawing. Also adding a clock so I can manually adjust the framerate of the game to fit my needs.
The rest of the updates can be found through the notes next to my lines of code. '''


import pygame
pygame.init()  #Initializes the game, ALWAYS DO THIS

screen_size = 480
win = pygame.display.set_mode((screen_size,screen_size)) #Creates our window

pygame.display.set_caption("Characters and Backgrounds") 

walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'), pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'), pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png')]
walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'), pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'), pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png')]
bg = pygame.image.load('images/bg.jpg')
char = pygame.image.load('images/standing.png')  #Making variables for the images so it is easier to call them

clock = pygame.time.Clock() #Starting a clock for thje game so I can implement framerates
 
x = 50
y = 400
width = 64
height = 64
vel = 5

left = False 
right = False
walkCount = 0  #important variables that adds constraints that would make the character move strangely

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))  #This is how you draw something in pygame, arg1 = image, arg2 = tuple of coordinates to put the image
    
    
    if walkCount + 1 >= 27: #resets the walk count which is the index of our image traversal list
        walkCount = 0
        
    if left:
        win.blit(walkLeft[walkCount//3], (x,y)) #integer division so our index is never a decimal
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))
        
    pygame.display.update() #tells the screen to update

isJump = False
jumpCount = 10

#always make a main loop
run = True
while run:
    clock.tick(27) #Frame Rate
    
    for event in pygame.event.get(): # All events such as mouse movement
        if event.type == pygame.QUIT: # if the X is clicked
            run = False
            
    keys = pygame.key.get_pressed() # All the keys on our keyboard
    
    if keys[pygame.K_LEFT] and (x > vel): #The key clicked, barrier check, move model
        x -= vel
        left = True #self explanatory varibales, can have Left and Right both be True
        right = False
    elif keys[pygame.K_RIGHT] and (x + vel + width < screen_size):
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0
        
    if not (isJump):
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
            
    redrawGameWindow() #calls the finction that is incharge of all the drawing in the game every time the loop runs
    
pygame.quit() #Closes the window 
    
    

