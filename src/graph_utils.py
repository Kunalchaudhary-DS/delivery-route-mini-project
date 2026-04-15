import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        for neighbor, weight in graph[node].items():
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def prim_mst(graph, start):
    visited = set()
    mst = []
    total_cost = 0

    pq = [(0, start, None)]

    while pq:
        cost, node, parent = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if parent:
            mst.append((parent, node, cost))
            total_cost += cost

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(pq, (weight, neighbor, node))

    return mst, total_cost