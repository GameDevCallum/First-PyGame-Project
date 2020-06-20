"""
    INITIALISED BY: Callum S
    DATE INITIALISED: {{DD/MM/YYYY}} 19/06/2020
    DATE FINISHED: {{DD/MM/YYYY}} N/A
    EDITED BY: Callum S
    LAST EDITED BY & DATE {{DD/MM/YYYY}}: Callum S, 19/06/2020|12:47
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

class player(object):
    def __init__(self, plrX, plrY, plrWidth, plrHeight):
        self.plrX = plrX
        self.plrY = plrY
        self.plrWidth = plrWidth
        self.plrHeight = plrHeight
        self.plrVel = 5
        self.isJump = False
        self.jumpCount = 8
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, WIN):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if self.left:
            WIN.blit(walkLeft[self.walkCount//3], (self.plrX, self.plrY))
            self.walkCount += 1
        elif self.right:
            WIN.blit(walkRight[self.walkCount//3], (self.plrX, self.plrY))
            self.walkCount += 1
        else:
            WIN.blit(char, (self.plrX, self.plrY))

def reDrawGameWindow():
    WIN.blit(bg, (0, 0))
    character.draw(WIN)
    pygame.display.update()

character = player(300, 410, 64, 64)

run = True

while run:
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and character.plrX > character.plrVel:
        character.plrX -= character.plrVel
        character.left = True
        character.right = False

    elif keys[pygame.K_d] and character.plrX < WIDTH - character.plrWidth - character.plrVel:
        character.plrX += character.plrVel
        character.right = True
        character.left = False
    else:
        character.right = False
        character.left = False
        character.walkCount = 0

    if not(character.isJump):
        if keys[pygame.K_w]:
            character.isJump = True
            character.right = False
            character.left = False
            character.walkCount = 0
    else:
        if character.jumpCount >= -8:
            neg = 1
            if character.jumpCount < 0:
                neg = -1
            character.plrY -= (character.jumpCount ** 2) / 1 * neg
            character.jumpCount -= 1

        else:
            character.isJump = False
            character.jumpCount = 8
    
    reDrawGameWindow()


pygame.quit()