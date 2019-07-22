import pygame
pygame.init()

game_w = 500
game_h = 500

win = pygame.display.set_mode((game_w,game_h))

pygame.display.set_caption("Learning Pygame")

x=100
y=100
width = 40
height = 60
vel = 10

isJump = False
jumpCount = 10
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>=vel :
        x-=vel
    if keys[pygame.K_RIGHT] and x<=game_w-width - vel:
        x+=vel
    if not(isJump):
        if keys[pygame.K_UP] and  y>=vel :
            y-=vel
        if keys[pygame.K_DOWN] and y <= game_h-height-vel:
            y+=vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount <0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -=1
        else :
            isJump = False
            jumpCount = 10

    win.fill((0,0,0))
    pygame.draw.rect(win, (0,0,255),(x, y, width, height))
    pygame.display.update()

pygame.quit()
