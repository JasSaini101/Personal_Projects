'''Created a new class for projectiles aka bullets that the character is no able to shoot.
The projectiles are managed by all being put into a list. As long as the projectile is on screen,
it is in the list and a for each loop constantly draws each projectile by calling the draw function in
the projectile class. Once a projectile is off the screen, its is removed from the list. Instances of projectiles
are added into the list as soon as they are created. A maximumn of 5 items can be in the list so no more than 5 projectiles,
if more want to be shot, need to wait for some of the current ones to go off screen so there is space in the list.'''


import pygame
pygame.init()  #Initializes the game, ALWAYS DO THIS

screen_size = 480
win = pygame.display.set_mode((screen_size,screen_size)) #Creates our window

pygame.display.set_caption("Projectiles") 

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
        self.standing = True
        
    def draw(self,win):
        if self.walkCount + 1 >= 27: #resets the walk count which is the index of our image traversal list
            self.walkCount = 0
        
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y)) #integer division so our index is never a decimal
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
            
class projectile(): #New class for our projectiles aka bullets
    def __init__(self,x,y,radius,color,facing): #initialize
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        
    def draw(self, win): #a draw function that we can call to draw that instance of a projectile
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
            
        
def redrawGameWindow():
    win.blit(bg, (0,0))  #This is how you draw something in pygame, arg1 = image, arg2 = tuple of coordinates to put the image
    man.draw(win)
    for bullet in bullets: #For each bullet that is currently in bullets, draw it
        bullet.draw(win)
    pygame.display.update() #tells the screen to update


#always make a main loop
man = player(300, 410, 64, 64)
run = True
bullets = [] #an empty list that will contain all the active bullets
while run:
    clock.tick(27) #Frame Rate

    for event in pygame.event.get(): # All events such as mouse movement
        if event.type == pygame.QUIT: # if the X is clicked
            run = False
            
    for bullet in bullets: #for all the current bullets in bullet
        if bullet.x < 500 and bullet.x > 0: #if the bullet is on screen
            bullet.x += bullet.vel #change the bullets x coordinate by this much
        else:
            bullets.pop(bullets.index(bullet)) #remove the bullet that is off screen from the bullets list
            
    keys = pygame.key.get_pressed() # All the keys on our keyboard
    
    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1 #change the direction of the bullet velocity
        else:
            facing = 1
        if len(bullets) < 5: #if there are less than 5 bullets in the list / on screen
            bullets.append(projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0,0,0), facing))
            #this above line creates a bullet according to the players information and puts it in the bullets list
    
    if keys[pygame.K_LEFT] and (man.x > man.vel): #The key clicked, barrier check, move model
        man.x -= man.vel
        man.left = True #self explanatory varibales, can have Left and Right both be True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and (man.x + man.vel + man.width < screen_size):
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True 
        man.walkCount = 0 #resets the animation so he is not mid walk and standing
        
    if not (man.isJump):
        if keys[pygame.K_UP]:
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

