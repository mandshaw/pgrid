def dijsktra(board, initial):
  costs = {initial: 0}
  # path = {}

  nodes = set(board.cities.keys())

  while nodes:
    path = []
    min_node = None
    for node in nodes:
      if node in costs:
        if min_node is None:
          min_node = node
        elif costs[node] < costs[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    path.append(min_node)
    cost = costs[min_node]

    for connection in board.connections[min_node]:
      accumulated_cost = cost + board.connection_costs[(min_node, connection)]
      if connection not in costs or accumulated_cost < costs[connection]:
          costs[connection] = accumulated_cost
        # costs[connection] = min_node

  return costs