GRAPH = {
    'A': {'B': 10, 'E': 5 },
    'B': {'A': 10, 'C': 12},
    'C': { 'B': 12, 'D': 6 },
    'D': {'C': 6, 'F': 8},
    'E': {'A': 5,'F': 3},
    'F': {'D': 8, 'E': 3}
}

def bestfirst(source, destination):
    straight_line = {
        'A': 20,
        'B': 15,
        'C': 6,
        'D': 0,
        'E': 9,
        'F': 8
    }
    from queue import PriorityQueue
    priority_queue, visited = PriorityQueue(), {}
    priority_queue.put((straight_line[source], 0, source, [source]))
    visited[source] = straight_line[source]
    while not priority_queue.empty():
        (heuristic, cost, vertex, path) = priority_queue.get()
        if vertex == destination:
            return heuristic, cost, path
        for next_node in GRAPH[vertex].keys():
            current_cost = cost + GRAPH[vertex][next_node]
            heuristic = straight_line[next_node]
            if not next_node in visited or visited[next_node] >= heuristic:
                visited[next_node] = heuristic
                priority_queue.put((heuristic, current_cost, next_node, path + [next_node]))


def main():
    print('ENTER SOURCE :', end=' ')
    source = input().strip()
    print('ENTER GOAL :', end=' ')
    goal = input().strip()
    if source not in GRAPH or goal not in GRAPH:
        print('ERROR: CITY DOES NOT EXIST.')
    else:
        print('\nBFS PATH:')
        heuristic, cost, optimal_path = bestfirst(source, goal)
        print('PATH COST =', cost)
        print(' -> '.join(city for city in optimal_path))


if __name__ == '__main__':
    main()