import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Learning Pygame")

x=50
y=50
width = 40
height = 60
vel = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        run = False

pygame.quit()
