def depth_first_search(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()  # Pop the last element from the stack
        if node not in visited:
            print(node, end=' ')  # Process the node (in this case, print it)
            visited.add(node)

            # Push adjacent nodes to the stack in reverse order to explore them in the desired order (a, b, c, d, e)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Define the state space graph as an adjacency list
graph = {
    'a': ['d', 'c','e'],
    'b': [],
    'c': ['b'],
    'd': [],
    'e': [],
}

# Start DFS from node 'a'
print("DFS starting from 'a':")
depth_first_search(graph, 'a')

# Start DFS from node 'a'
print("\nDFS starting from 'b':")
depth_first_search(graph, 'b')
