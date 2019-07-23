import pygame
import player
import projectile
from animations import *
import ennemy
from time import *
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

bulletSound = pygame.mixer.Sound('sounds/bullet.wav')
#hitSound = pygame.mixer.Sound('sounds/hit.wav')

#music = pygame.mixer.music.load('sounds/music.mp3')
# pygame.mixer.music.play(-1)
# pygame.mixer.music.load('music.mp3')
# pygame.mixer.music.play()
# time.sleep(2)
# pygame.mixer.music.stop()

# Initialise the player and the start of the run
run = True
player = player.Player(300, 405, 64, 64, 5)
bullets = []
goblin = ennemy.Ennemy(16, 410, 64, 64, 450, 6)
shootLoop = 0  # not to spam the bullets
biteLoop = 0  # not to get spammed by zombies
score = 0
font = pygame.font.SysFont('comicsans', 30, True)
# The refresh window part


def redrawGameWindow():
    win.blit(bg, (0, 0))
    text = font.render("Score : "+str(score), 1, (0, 0, 0))
    win.blit(text, (390, 10))
    player.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# Beggining the loop
while run:
    clock.tick(27)  # FPS

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 10:
        shootLoop = 0

    for event in pygame.event.get():  # Stop the program if we quit
        if event.type == pygame.QUIT:
            run = False
   # bullets mouvement
    if biteLoop > 0:
        biteLoop += 1
    if biteLoop > 20:
        biteLoop = 0

    if goblin.attacks(player) and biteLoop == 0:
        goblin.bite()
        biteLoop = 1

    for bullet in bullets:
        if bullet.hits(goblin):
            goblin.hit()
            # hitSound.play()
            score += 1
            bullets.pop(bullets.index(bullet))
        if bullet.x < game_w and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

# -----------------------------------------------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run = False  # Stop the run if we press Escape

    if keys[pygame.K_SPACE] and shootLoop == 0:

        if player.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(projectile.Projectile(
                player.x+player.width//2,
                player.y+player.height//2,
                6,
                (0, 0, 0),
                facing
            ))
        shootLoop = 1
        bulletSound.play()

    if keys[pygame.K_LEFT] and player.x >= player.vel:
        player.x -= player.vel
        player.left = True
        player.right = False
        player.standing = False

    elif keys[pygame.K_RIGHT] and player.x <= game_w-player.width - player.vel:
        player.x += player.vel
        player.left = False
        player.right = True
        player.standing = False
    else:
        player.standing = True
        player.walkCount = 0

    if not(player.isJump):
        # if keys[pygame.K_UP] and  y>=vel :        WE DON'T NEED TO MOVE UP AND DOWN ANYMORE
        #     y-=vel                                            SINCE IS LIKE A PLATFORM GAME
        # if keys[pygame.K_DOWN] and y <= game_h-height-vel:
        #     y+=vel
        if keys[pygame.K_UP]:
            player.isJump = True
            player.walkCount = 0
    else:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount**2) * 0.4 * neg
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10
    redrawGameWindow()


pygame.quit()
