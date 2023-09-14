# Function to check if it's safe to assign a color to a region
def is_safe(graph, region, color, assignment):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking algorithm to assign colors to regions
def map_coloring(graph, regions, colors, assignment={}):
    if len(assignment) == len(regions):
        return assignment  # All regions have been assigned colors

    current_region = None
    for region in regions:
        if region not in assignment:
            current_region = region
            break

    for color in colors:
        if is_safe(graph, current_region, color, assignment):
            assignment[current_region] = color
            result = map_coloring(graph, regions, colors, assignment)
            if result is not None:
                return result
            assignment.pop(current_region)

    return None  # No valid assignment found

# Define the map as a graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C'],
}

# List of regions to be colored
regions = list(graph.keys())

# List of available colors
colors = ['Red', 'Green', 'Blue']

# Solve the Map Coloring problem
result = map_coloring(graph, regions, colors)

if result is not None:
    print("Map Coloring Assignment:")
    for region, color in result.items():
        print(f"{region}: {color}")
else:
    print("No valid map coloring assignment found.")
