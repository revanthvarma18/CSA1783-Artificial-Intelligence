import heapq

# Define a class to represent a node in the search tree
class Node:
    def __init__(self, state, cost, path):
        self.state = state  # Current state
        self.cost = cost    # Cost to reach this state
        self.path = path    # Path from the initial state to this state

    def __lt__(self, other):
        return self.cost < other.cost

# Define the tree structure as an adjacency list
tree = {
    'S': [('A', 2), ('B', 3)],
    'A': [('C', 1), ('D', 4)],
    'B': [('E', 2)],
    'C': [],
    'D': [('G', 5)],
    'E': [('F', 1)],
    'F': [('G', 3)],
    'G': []
}

def uniform_cost_search(graph, start, goal):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, Node(start, 0, []))

    while priority_queue:
        current_node = heapq.heappop(priority_queue)
        current_state, current_cost, current_path = current_node.state, current_node.cost, current_node.path

        if current_state == goal:
            return current_path + [current_state]

        if current_state not in visited:
            visited.add(current_state)

            for neighbor, cost in graph[current_state]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, Node(neighbor, current_cost + cost, current_path + [current_state]))

    return None  # Goal state not reachable

# Define the initial and goal states
initial_state = 'S'
goal_state = 'G'

# Find the path from initial state to goal state using Uniform Cost Search
path = uniform_cost_search(tree, initial_state, goal_state)

if path:
    print("Path from", initial_state, "to", goal_state, ":", path)
    print("Total cost:", sum(tree[node][0][1] for node in path))
else:
    print("Goal state", goal_state, "is not reachable from initial state", initial_state)
