import heuristicFunctions as hf
import random
import numpy as np

def aStarSearch(startState, foodPos, getSuccessors, heuristic=hf.manhattanDistHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    startNode = (startState, None, 0)
    visited = [startNode]
    queue = [startNode]
    expanded = {}
    goalNode = None
    while queue:
      queue.sort(key = lambda x: x[2] + heuristic(x[0], foodPos))
      node = queue.pop(0)
      if foodPos == node[0][0]: # goal state
        goalNode = node
        visited.append(node)
        break
      successors = getSuccessors(node[0])
      for n in successors:
        n = (n[0], n[1], n[2] + node[2])
        if n[0] not in list(map(lambda x: x[0], visited)) or n[0][0] == foodPos:
          expanded[n] = node
          visited.append(n)
          queue.append(n)
      # if visited is too long, just do something
      if len(visited) > 500:
        availableMoves = list(map(lambda x: len(getSuccessors(x[0])), visited[1:]))
        goalNode = visited[np.argmax(availableMoves)]
        visited.append(node)
        break

    path: list = [goalNode]
    reverse = goalNode
    while reverse != startNode:
      expandedFrom = expanded[reverse]
      path.append(expandedFrom)
      reverse = expandedFrom
    path.reverse()
    toReturn = list(map(lambda x: x[1], path[1:]))
    if toReturn:
      return toReturn
    # no solution found, just keep going
    sortVisited = visited[1:]
    sortVisited.sort(key = lambda x: len(getSuccessors(x[0])), reverse=True)
    return [visited[1][1]]
