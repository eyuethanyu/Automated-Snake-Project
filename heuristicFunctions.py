import snakeConfig as c

def manhattanDistHeuristic(state, food):
   pos = state[0]
   return manhattanDistance(pos, food)

def manhattanDistance(pos1, pos2):
   return abs( pos1[0] - pos2[0] ) + abs( pos1[1] - pos2[1] )

def wallBodyDistance(pos, snakeList):
    # Calculate the distance to the walls
    wall_dist = c.WIDTH + c.HEIGHT - 2 * (pos[0] + pos[1] + 1)
    
    # Calculate the distance to the body
    body_dist = float('inf')
    for body_part in snakeList:
        dist = manhattanDistance(pos, body_part)
        if dist < body_dist:
            body_dist = dist
    
    # Invert the distances and return the sum
    return (c.WIDTH * c.HEIGHT + wall_dist + body_dist)

def foodAndSelfHeuristic(state, food):
   return manhattanDistHeuristic(state, food) - wallBodyDistance(state[0], state[1])

def wallDist(pos):
   return min(pos[0], pos[1], c.WIDTH - pos[0], c.HEIGHT - pos[1])

def wallHeuristic(state, food):
   pos = state[0]
   return wallDist(pos)

def foodAndTailHeuristic(state, food):
   pos = state[0]
   tail = state[1]
   distToTail = manhattanDistance(pos, tail[-1]) if tail else 0
   return manhattanDistance(pos, food) + distToTail

def foodTailWallHeuristic(state, food):
   return (3 * foodAndTailHeuristic(state, food)) + wallDist(state[0])

def foodWallHeuristic(state, food):
   return manhattanDistHeuristic(state, food) + wallDist(state[0])

def variableDualHeuristic(state, food, h1=manhattanDistHeuristic, h2=foodAndSelfHeuristic):
   if len(state[1]) < 0.25 * min(c.WIDTH, c.HEIGHT):
      return h1(state, food)
   else:
      return h2(state, food)