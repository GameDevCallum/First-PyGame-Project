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

#LOADING ASSETS

walkRight = [pygame.image.load("R1.png"), pygame.image.load("R2.png"), pygame.image.load("R3.png"), pygame.image.load("R4.png"), pygame.image.load("R5.png"), pygame.image.load("R6.png"), pygame.image.load("R7.png"), pygame.image.load("R8.png"), pygame.image.load("R9.png"), ]
walkLeft = [pygame.image.load("L1.png"), pygame.image.load("L2.png"), pygame.image.load("L3.png"), pygame.image.load("L4.png"), pygame.image.load("L5.png"), pygame.image.load("L6.png"), pygame.image.load("L7.png"), pygame.image.load("L8.png"), pygame.image.load("L9.png"), ]
bg = pygame.image.load("bg.jpg")
char = pygame.image.load("standing.png")


#VARIABLES

plrX = 0
plrY = 460
plrWidth = 40
plrHeight = 40
plrVel = 5
isJump = False
jumpCount = 8
left = False
right = True
walkCount = 0

run = True


while run:
    pygame.time.delay(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and plrX != 0:
        plrX -= plrVel
    if keys[pygame.K_d] and plrX != WIDTH - plrWidth:
        plrX += plrVel
    if not(isJump):
        if keys[pygame.K_w]:
            isJump = True
    else:
        if jumpCount >= -8:
            neg = 1
            if jumpCount < 0:
                neg = -1
            plrY -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 8


    WIN.fill((0, 255, 150))
    pygame.draw.rect(WIN, (255, 0, 0), (plrX, plrY, plrWidth, plrHeight))
    pygame.display.update()


pygame.quit()