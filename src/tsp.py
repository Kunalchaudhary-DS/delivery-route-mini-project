from itertools import permutations

def tsp(graph, nodes):
    min_path = None
    min_cost = float('inf')

    for perm in permutations(nodes):
        current = 'Warehouse'
        cost = 0

        for node in perm:
            cost += graph[current][node]
            current = node

        # Return to warehouse
        cost += graph[current]['Warehouse']

        if cost < min_cost:
            min_cost = cost
            min_path = perm

    return min_path, min_cost