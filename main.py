"""
    INITIALISED BY: Callum S
    DATE INITIALISED: {{DD/MM/YYYY}} 19/06/2020
    DATE FINISHED: {{DD/MM/YYYY}} N/A
    EDITED BY: Callum S
    LAST EDITED BY & DATE {{DD/MM/YYYY}}: Callum S, 19/06/2020|10:54
"""

import pygame
import os

pygame.init()

# WIN SETUP

HEIGHT = 480
WIDTH = 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

#LOADING ASSETS

walkRight = [pygame.image.load(os.path.join("Media", "R1.png")), pygame.image.load(os.path.join("Media", "R2.png")), pygame.image.load(os.path.join("Media", "R3.png")), pygame.image.load(os.path.join("Media", "R4.png")), pygame.image.load(os.path.join("Media", "R5.png")), pygame.image.load(os.path.join("Media", "R6.png")), pygame.image.load(os.path.join("Media", "R7.png")), pygame.image.load(os.path.join("Media", "R8.png")), pygame.image.load(os.path.join("Media", "R9.png")) ]
walkLeft = [pygame.image.load(os.path.join("Media", "L1.png")), pygame.image.load(os.path.join("Media", "L2.png")), pygame.image.load(os.path.join("Media", "L3.png")), pygame.image.load(os.path.join("Media", "L4.png")), pygame.image.load(os.path.join("Media", "L5.png")), pygame.image.load(os.path.join("Media", "L6.png")), pygame.image.load(os.path.join("Media", "L7.png")), pygame.image.load(os.path.join("Media", "L8.png")), pygame.image.load(os.path.join("Media", "L9.png")) ]
bg = pygame.image.load(os.path.join("Media", "bg.jpg")) 
char = pygame.image.load(os.path.join("Media", "standing.png")) 

#VARIABLES

clock = pygame.time.Clock()

plrX = 50
plrY = 400
plrWidth = 64
plrHeight = 64
plrVel = 5
isJump = False
jumpCount = 8
left = False
right = True
walkCount = 0

def reDrawGameWindow():
    global walkCount
    WIN.blit(bg, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0
    
    if left:
        WIN.blit(walkLeft[walkCount//3], (plrX, plrY))
        walkCount += 1
    elif right:
        WIN.blit(walkRight[walkCount//3], (plrX, plrY))
        walkCount += 1
    else:
        WIN.blit(char, (plrX, plrY))
    
    pygame.display.update()

run = True

while run:
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and plrX > plrVel:
        plrX -= plrVel
        left = True
        right = False

    elif keys[pygame.K_d] and plrX < WIDTH - plrWidth - plrVel:
        plrX += plrVel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_w]:
            isJump = True
            right = False
            left = False
            walkCount = 0
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
    
    reDrawGameWindow()


pygame.quit()