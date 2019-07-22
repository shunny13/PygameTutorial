import pygame
pygame.init()

game_w = 500
game_h = 480

win = pygame.display.set_mode((game_w,game_h))

pygame.display.set_caption("Learning Pygame")

clock = pygame.time.Clock()

x=50
y=400
width = 64
height = 64
vel = 10

isJump = False
jumpCount = 10

left =False
right = False
walkCount = 0

####### THE SPRITE / ANIMATION PART ##############
walkRight = [pygame.image.load('assets/R1.png'), pygame.image.load('assets/R2.png'), pygame.image.load('assets/R3.png'), pygame.image.load('assets/R4.png'), pygame.image.load('assets/R5.png'), pygame.image.load('assets/R6.png'), pygame.image.load('assets/R7.png'), pygame.image.load('assets/R8.png'), pygame.image.load('assets/R9.png')]
walkLeft = [pygame.image.load('assets/L1.png'), pygame.image.load('assets/L2.png'), pygame.image.load('assets/L3.png'), pygame.image.load('assets/L4.png'), pygame.image.load('assets/L5.png'), pygame.image.load('assets/L6.png'), pygame.image.load('assets/L7.png'), pygame.image.load('assets/L8.png'), pygame.image.load('assets/L9.png')]
bg = pygame.image.load('assets/bg.jpg')
char = pygame.image.load('assets/standing.png')
##################################################

def redrawGameWindow():
    global walkCount
    win.blit(bg,(0,0))

    if walkCount+1>=27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount+=1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount+=1
    else:
        win.blit(char, (x,y))

    pygame.display.update()


run = True
while run:

    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>=vel :
        x-=vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x<=game_w-width - vel:
        x+=vel
        left = False
        right = True
    else :
        left = False
        right = False
        walkCount = 0
    if not(isJump):
        # if keys[pygame.K_UP] and  y>=vel :        WE DON'T NEED TO MOVE UP AND DOWN ANYMORE
        #     y-=vel                                            SINCE IS LIKE A PLATFORM GAME
        # if keys[pygame.K_DOWN] and y <= game_h-height-vel:
        #     y+=vel
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount=0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount <0:
                neg = -1
            y -= (jumpCount**2) * 0.5 * neg
            jumpCount -=1
        else :
            isJump = False
            jumpCount = 10

    redrawGameWindow()



pygame.quit()
