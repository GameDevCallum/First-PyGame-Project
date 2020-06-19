"""
    INITIALISED BY: Callum S
    DATE INITIALISED: {{DD/MM/YYYY}} 19/06/2020
    DATE FINISHED: {{DD/MM/YYYY}} N/A
    EDITED BY: Callum S
"""

import pygame

pygame.init()

# WIN SETUP

HEIGHT = 500
WIDTH = 500

WIN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("First Game")

#VARIABLES

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True


while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    

pygame.quit()