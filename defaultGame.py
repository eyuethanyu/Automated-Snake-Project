import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (100, 100, 255)
 
width = 200
height = 300
 
dis = pygame.display.set_mode((width, height))
 
clock = pygame.time.Clock()
 
snakeSize = 10
speed = 15
 
def snake(snakeSize, snakeList):
    for x in snakeList:
        pygame.draw.rect(dis, black, [x[0], x[1], snakeSize, snakeSize])
 
def gameLoop():
    gameOver = False
 
    x = width / 2
    y = height / 2
 
    xChange = 0
    yChange = 0
 
    snakeList = []
    snakeLength = 1
 
    foodx = round(random.randrange(0, width - snakeSize) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snakeSize) / 10.0) * 10.0
 
    while not gameOver:
        
        # def insert search code here
        steps = None
        
        # direction change
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -snakeSize
                    yChange = 0
                elif event.key == pygame.K_RIGHT:
                    xChange = snakeSize
                    yChange = 0
                elif event.key == pygame.K_UP:
                    yChange = -snakeSize
                    xChange = 0
                elif event.key == pygame.K_DOWN:
                    yChange = snakeSize
                    xChange = 0
 
        # terminate condition
        if x >= width or x < 0 or y >= height or y < 0:
            print(f"Score {snakeLength - 1}")
            gameOver = True

        # default snake update
        x += xChange
        y += yChange
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snakeSize, snakeSize])
        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
 
        # other terminate condition
        for i in snakeList[:-1]:
            if i == snakeHead:
                print(f"Score {snakeLength - 1}")
                gameOver = True
 
        snake(snakeSize, snakeList)
 
        pygame.display.update()
 
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - snakeSize) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snakeSize) / 10.0) * 10.0
            snakeLength += 1
 
        clock.tick(speed)
 
    pygame.quit()
    quit()
 
gameLoop()