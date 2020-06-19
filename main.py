"""
    INITIALISED BY: Callum S
    DATE INITIALISED: {{DD/MM/YYYY}} 19/06/2020
    DATE FINISHED: {{DD/MM/YYYY}} N/A
    EDITED BY: Callum S
    LAST EDITED BY & DATE {{DD/MM/YYYY}}: Callum S, 19/06/2020|10:54
"""

import pygame

pygame.init()

# WIN SETUP

HEIGHT = 500
WIDTH = 500

WIN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("First Game")

#VARIABLES

plrX = 225
plrY = 225
plrWidth = 40
plrHeight = 40
plrVel = 5

run = True


while run:
    pygame.time.delay(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and plrX != 0:
        plrX -= plrVel
    if keys[pygame.K_RIGHT] and plrX != WIDTH - plrWidth:
        plrX += plrVel
    if keys[pygame.K_UP] and plrY != 0:
        plrY -= plrVel
    if keys[pygame.K_DOWN] and plrY != HEIGHT - plrHeight:
        plrY += plrVel

    WIN.fill((0, 255, 150))
    pygame.draw.rect(WIN, (255, 0, 0), (plrX, plrY, plrWidth, plrHeight))
    pygame.display.update()


pygame.quit()