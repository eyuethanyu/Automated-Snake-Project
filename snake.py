import pygame
import time
import random
from bfs import breadthFirstSearch
from a_star import aStarSearch
import snakeConfig as c
import heuristicFunctions as hf
 
pygame.init()
 
dis = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
 
clock = pygame.time.Clock()

def getSuccessors(currentState):
  currentPos = currentState[0]
  baseSnakeList = list(currentState[1])
  validMoves = []
  for m in c.MOVES:
    snakeList = baseSnakeList.copy()
    snakeHead = (currentPos[0] + m[0], currentPos[1] + m[1])
    snakeList.append(snakeHead)
    if not invalidMove(snakeHead, snakeList[1:]):
      validMoves.append(((snakeHead, tuple(snakeList[1:])), m, 0))
  return validMoves

def invalidMove(pos, snakeList):
  return pos[0] >= c.WIDTH or pos[0] < 0 or pos[1] >= c.HEIGHT or pos[1] < 0 or pos in snakeList[:-1]
 
def drawSnake(snakeList):
  for x in snakeList:
    pygame.draw.rect(dis, c.BLACK, [x[0], x[1], c.SNAKE_SIZE, c.SNAKE_SIZE])

def generateFood(snakeList):
  while True:
    foodx = round(random.randrange(0, c.WIDTH - c.SNAKE_SIZE) / c.SNAKE_SIZE) * c.SNAKE_SIZE
    foody = round(random.randrange(0, c.HEIGHT - c.SNAKE_SIZE) / c.SNAKE_SIZE) * c.SNAKE_SIZE
    if (foodx, foody) not in (snakeList[:-1]):
      return foodx, foody
 
def runSnakeGame(search):
  print("Running snake. Press any button to quit.")
  gameOver = False
  x = c.WIDTH // 2
  y = c.HEIGHT // 2
  xChange = 0
  yChange = 0
  snakeList = []
  snakeLength = 1
  foodx = round(random.randrange(0, c.WIDTH - c.SNAKE_SIZE) / 10.0) * 10.0
  foody = round(random.randrange(0, c.HEIGHT - c.SNAKE_SIZE) / 10.0) * 10.0

  directionsToFood = []
  while not gameOver:
    
    if len(directionsToFood) == 0:
      try:
        directionsToFood = search(((x,y), tuple(snakeList)), (foodx, foody), getSuccessors)
      except Exception as e:
        print(f"Exception: {e}")
        print(f"No solution - Score: {snakeLength - 1}")
        gameOver = True
        continue
    try:
      xChange, yChange = directionsToFood.pop(0)
    except Exception as e:
      print(f"Exception: {e}")
      print(f"Error - Score: {snakeLength - 1}")
      gameOver = True
      continue
    # default snake update
    x += xChange
    y += yChange   

    dis.fill(c.GREEN)
    snakeHead = (x, y)
    snakeList.append(snakeHead)

    if x == foodx and y == foody:
      foodx, foody = generateFood(snakeList)
      directionsToFood = []
      snakeLength += 1
    
    if len(snakeList) > snakeLength:
      snakeList.pop(0)

    drawSnake(snakeList) 
    
    if invalidMove(snakeHead, snakeList):
      print(f"Score {snakeLength - 1}")
      gameOver = True  

    pygame.draw.rect(dis, c.RED, [foodx, foody, c.SNAKE_SIZE, c.SNAKE_SIZE])
    pygame.display.update()

    clock.tick(c.SPEED)
    # quit
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        print(f"Game quit - Score {snakeLength - 1}")
        gameOver = True

  pygame.quit()
  quit()

runSnakeGame(aStarSearch)
