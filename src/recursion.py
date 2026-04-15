def recursive_cost(graph, current, remaining):
    if not remaining:
        return graph[current]['Warehouse']

    min_cost = float('inf')

    for node in remaining:
        cost = graph[current][node] + recursive_cost(
            graph,
            node,
            [x for x in remaining if x != node]
        )

        if cost < min_cost:
            min_cost = cost

    return min_cost