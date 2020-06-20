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
        self.standing = True

    def draw(self, WIN):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if not(self.standing):
            if self.left:
                WIN.blit(walkLeft[self.walkCount//3], (self.plrX, self.plrY))
                self.walkCount += 1
            elif self.right:
                WIN.blit(walkRight[self.walkCount//3], (self.plrX, self.plrY))
                self.walkCount += 1
        else:
            if self.right:
                WIN.blit(walkRight[0], (self.plrX, self.plrY))
            else:
                WIN.blit(walkLeft[0], (self.plrX, self.plrY))

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10 * facing

    def draw(self, WIN):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.radius)

def reDrawGameWindow():
    WIN.blit(bg, (0, 0))
    character.draw(WIN)
    for bullet in bullets:
        bullet.draw(WIN)
    pygame.display.update()

character = player(300, 410, 64, 64)

bullets = []

run = True

""" MAIN LOOP """

while run:
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if character.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(projectile(round(character.plrX + character.plrWidth //2), round(character.plrY + character.plrHeight//2), 6, (0, 0, 0), facing))
    
    if keys[pygame.K_a] and character.plrX > character.plrVel:
        character.plrX -= character.plrVel
        character.left = True
        character.right = False
        character.standing = False

    elif keys[pygame.K_d] and character.plrX < WIDTH - character.plrWidth - character.plrVel:
        character.plrX += character.plrVel
        character.right = True
        character.left = False
        character.standing = False
    else:
        character.standing = True
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
            character.plrY -= int((character.jumpCount ** 2) / 1 * neg)
            character.jumpCount -= 1

        else:
            character.isJump = False
            character.jumpCount = 8
    
    reDrawGameWindow()


pygame.quit()