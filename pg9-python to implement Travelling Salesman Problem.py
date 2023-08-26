import itertools
def calculate_distance(points, order):
    total_distance = 0
    num_points = len(order)
    for i in range(num_points):
        point1 = points[order[i]]
        point2 = points[order[(i + 1) % num_points]]
        total_distance += calculate_distance_between_points(point1, point2)
    return total_distance
def calculate_distance_between_points(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5
def tsp_bruteforce(points):
    min_distance = float('inf')
    optimal_order = None
    num_points = len(points)
    for order in itertools.permutations(range(num_points)):
        distance = calculate_distance(points, order)
        if distance < min_distance:
            min_distance = distance
            optimal_order = order
    return min_distance, optimal_order
points = {
    'A': (0, 0),
    'B': (1, 2),
    'C': (4, 1),
    'D': (2, 4)
}
min_distance, optimal_order = tsp_bruteforce(list(points.values()))
optimal_path = [list(points.keys())[i] for i in optimal_order]
print("Optimal Path:", optimal_path)
print("Min Distance:", min_distance)
