'''Created hitboxes for all the classes and have them drawn as a red rectangle around the instance.
If a bullet is inside of the goblins hitbox, the bullet dissappears and registers as a 'hit'. Collision
between the player and goblin is not done yet however a simple variable that essentially counts has been
added called 'shootLoop' that stops the player from shooting more than one bullet at a time. The bullet hitbox
was created by me on my own by playing with the numbers until it looed really nice.'''


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
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)  #the hitbox of this player instance
        
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
        self.hitbox = (self.x + 17, self.y + 11, 29, 52) 
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2) #draws the hitbox around the models
                
class enemy(): #creating a new class for the enemies
    
    walkRight = [pygame.image.load('images/R1E.png'), pygame.image.load('images/R2E.png'), pygame.image.load('images/R3E.png'), pygame.image.load('images/R4E.png'), pygame.image.load('images/R5E.png'), pygame.image.load('images/R6E.png'), pygame.image.load('images/R7E.png'), pygame.image.load('images/R8E.png'), pygame.image.load('images/R9E.png'), pygame.image.load('images/R10E.png'), pygame.image.load('images/R11E.png')]
    walkLeft = [pygame.image.load('images/L1E.png'), pygame.image.load('images/L2E.png'), pygame.image.load('images/L3E.png'), pygame.image.load('images/L4E.png'), pygame.image.load('images/L5E.png'), pygame.image.load('images/L6E.png'), pygame.image.load('images/L7E.png'), pygame.image.load('images/L8E.png'), pygame.image.load('images/L9E.png'), pygame.image.load('images/L10E.png'), pygame.image.load('images/L11E.png')]
    #above are the images of the enemy walking that are traversed in the list
    
    
    def __init__(self, x, y, width, height, end): #initialiing enemy instances
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end] #path is where the enemy currently is to the coordinate we want it to move to
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57) #the hitbox of this enemy instance
        
    def draw(self,win): #a draw function that draws the correct image of the enemy on the screen
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel > 0: #if velocity is positive, enemy moving right so get image from that list
            win.blit(self.walkRight[self.walkCount // 3], (self.x,self.y))
            self.walkCount += 1
        else: #if velocity is negative, enemy moving right so get image from that list
            win.blit(self.walkLeft[self.walkCount // 3], (self.x,self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 17, self.y, 31, 57)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2) #draws the hitbox around the models
        
    def move(self):
        if self.vel > 0: #if velocity is positive, the enemy is moving right
            if self.x + self.vel < self.path[1]: #if the enemy can continuing moving right
                self.x += self.vel #move the enemy right by adding this to its x coordinate
            else:
                self.vel = self.vel * -1 #change the direction of the enemy
                self.walkCount = 0 #reset the animation index
        else: #if velocity is negative, the enemy is moving left
            if self.x + self.vel > self.path[0]: #if the enemy can continuing moving left
                self.x += self.vel #move the enemy left by adding this to its x coordinate
            else:
                self.vel = self.vel * -1 #change the direction of the enemy
                self.walkCount = 0 #reset the animation index
    
    def hit(self): #function for what to do when an enemy is hit by a bullet
        print('Hit')
        pass
    
            
class projectile():
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        self.hitbox = (self.x - 5, self.y - 5, 10, 10)  #the hitbox of this projectile instance
        
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
        self.hitbox = (self.x - 5, self.y - 5, 10, 10)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2) #draws the hitbox around the models
            
        
def redrawGameWindow():
    win.blit(bg, (0,0))  #This is how you draw something in pygame, arg1 = image, arg2 = tuple of coordinates to put the image
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update() #tells the screen to update


#always make a main loop
man = player(300, 405, 64, 64)
goblin = enemy(100, 410, 64, 64, 400) #instance of an enemy is created
run = True
shootLoop = 0
bullets = []
while run:
    clock.tick(27) #Frame Rate
    if shootLoop < 5 and shootLoop > 0: #a basic time loop that counts to 5 essentially
        shootLoop += 1
    else:
        shootLoop = 0

    for event in pygame.event.get(): # All events such as mouse movement
        if event.type == pygame.QUIT: # if the X is clicked
            run = False
            
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]: 
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                #nested if statements checks to see if the bullets are insides the hitboxes of the enemy instances
                goblin.hit() #calls the hit funtion for that goblin
                bullets.pop(bullets.index(bullet)) #removes the bullet that hit the goblin
                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            
    keys = pygame.key.get_pressed() # All the keys on our keyboard
    
    if keys[pygame.K_SPACE] and shootLoop == 0:
        shootLoop = 1
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0,0,0), facing)) 
    
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
        man.walkCount = 0
        
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