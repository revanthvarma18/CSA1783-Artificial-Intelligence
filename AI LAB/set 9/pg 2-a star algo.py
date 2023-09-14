import heapq

def heuristic(node, goal):
    # Replace this with an appropriate heuristic function
    return 0

def astar(graph, start, goal):
    open_list = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.insert(0, current_node)
                current_node = came_from[current_node]
            path.insert(0, start)
            return path

        for neighbor, cost in graph[current_node].items():
            tentative_g_score = g_score[current_node] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))

    return None

# Example usage:
graph = {
    'A': {'B': 7, 'D': 9},
    'B': {'A': 7, 'C': 7},
    'C': {'B': 7, 'D': 3, 'E': 10},
    'D': {'A': 9, 'C': 3,'E':3},
    'E': {'D':3, 'C':10},
}

start_node = 'A'
goal_node = 'E'
path = astar(graph, start_node, goal_node)
if path:
    print("Shortest path:", path)
else:
    print("No path found.")
