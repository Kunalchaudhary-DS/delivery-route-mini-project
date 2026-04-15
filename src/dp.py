def check_time_constraints(route, graph, deadlines):
    time = 0
    current = 'Warehouse'

    for location in route:
        time += graph[current][location]

        if location in deadlines and time > deadlines[location]:
            return False

        current = location

    return True