import pygame
import player
from animations import *
# Initialisation
pygame.init()

# screen sizes
game_w = 500
game_h = 480

# Displaying the window
win = pygame.display.set_mode((game_w, game_h))

# The title of the pygame
pygame.display.set_caption("Learning Pygame")

# Getting the clock in order to fix the FPS
clock = pygame.time.Clock()


# Initialise the player and the start of the run
run = True
player = player.Player(300, 410, 64, 64, 5)


# The refresh window part
def redrawGameWindow():
    win.blit(bg, (0, 0))
    player.draw(win)
    pygame.display.update()


# Beggining the loop
while run:
    clock.tick(27)  # FPS
    for event in pygame.event.get():  # Stop the program if we quit
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run = False  # Stop the run if we press Escape

    if keys[pygame.K_LEFT] and player.x >= player.vel:
        player.x -= player.vel
        player.left = True
        player.right = False

    elif keys[pygame.K_RIGHT] and player.x <= game_w-player.width - player.vel:
        player.x += player.vel
        player.left = False
        player.right = True
    else:
        player.left = False
        player.right = False
        player.walkCount = 0
    if not(player.isJump):
        # if keys[pygame.K_UP] and  y>=vel :        WE DON'T NEED TO MOVE UP AND DOWN ANYMORE
        #     y-=vel                                            SINCE IS LIKE A PLATFORM GAME
        # if keys[pygame.K_DOWN] and y <= game_h-height-vel:
        #     y+=vel
        if keys[pygame.K_SPACE]:
            player.isJump = True
            player.left = False
            player.right = False
            player.walkCount = 0
    else:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount**2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10

    redrawGameWindow()


pygame.quit()
