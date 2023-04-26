def breadthFirstSearch(startState, foodPos, getSuccessors):
    """Search the shallowest nodes in the search tree first."""
    startNode = (startState, None, 0)
    visited = [startNode]
    queue = [startNode]
    expanded = {}
    goalNode = None
    while queue:
        node = queue.pop(0)
        if foodPos == node[0][0]: # goal state
          goalNode = node
          visited.append(node)
          break
        successors = getSuccessors(node[0])
        for n in successors:
          if n[0] not in list(map(lambda x: x[0], visited)) or n[0][0] == foodPos:
            expanded[n] = node
            visited.append(n)
            queue.append(n)
    path: list = [goalNode]
    reverse = goalNode
    while reverse != startNode:
      expandedFrom = expanded[reverse]
      path.append(expandedFrom)
      reverse = expandedFrom
    path.reverse()
    return list(map(lambda x: x[1], path[1:]))