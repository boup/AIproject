import pygame, sys, random
from pygame.locals import *

#colours
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (153, 76, 0)

#tipes
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3


textures = {
DIRT : pygame.image.load('index1.png'),
GRASS : pygame.image.load('index2.png'),
WATER : pygame.image.load('images1.png'),
COAL : pygame.image.load('images2.png')
}
TILWSIZE = 100
MAPWIDTH = 5
MAPHIGHT = 5

PLAYER = pygame.image.load('images2.png')
playerPos = [0, 0]

resourses = [DIRT, GRASS, WATER, COAL]

tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHIGHT)]
for rw in range(MAPHIGHT):
    for cl in range(MAPWIDTH):
        randomNumber = random.randint(0, 15)
        if randomNumber == 0:
            title = COAL
        elif randomNumber == 1 or randomNumber == 2:
            title = WATER
        elif randomNumber >=3 and randomNumber <=7:
            title = GRASS
        else:
            title = DIRT

        tilemap[rw][cl] = title

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILWSIZE, MAPHIGHT*TILWSIZE))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_RIGHT and playerPos[0] < MAPWIDTH - 1:
                playerPos[0] +=1
            if event.key == K_LEFT and playerPos[0] > 0:
                playerPos[0] -=1
            if event.key == K_UP and playerPos[1] > 0:
                playerPos[1] -=1
            if event.key == K_DOWN and playerPos[1] < MAPHIGHT - 1:
                playerPos[1] +=1

    for row in range(MAPHIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILWSIZE, row*TILWSIZE))
            DISPLAYSURF.blit(PLAYER, (playerPos[0]*TILWSIZE, playerPos[1]*TILWSIZE))
            pygame.display.update()
