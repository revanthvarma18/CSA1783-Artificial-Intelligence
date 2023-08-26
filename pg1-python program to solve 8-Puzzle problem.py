import heapq
class PuzzleNode:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = 0
        self.h = self.calculate_manhattan_distance()
    def calculate_manhattan_distance(self):
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    x, y = divmod(self.state[i][j] - 1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance
    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)
def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def is_valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3
def get_possible_actions(blank_x, blank_y):
    moves = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = blank_x + dx, blank_y + dy
        if is_valid_move(new_x, new_y):
            moves.append((new_x, new_y))
    return moves
def apply_action(state, blank_x, blank_y, new_x, new_y):
    new_state = [row[:] for row in state]
    new_state[blank_x][blank_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[blank_x][blank_y]
    return new_state
def solve_8_puzzle(initial_state):
    initial_node = PuzzleNode(initial_state)
    open_set = [initial_node]
    closed_set = set()
    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            solution_path = []
            while current_node.parent:
                solution_path.append(current_node.state)
                current_node = current_node.parent
            solution_path.append(initial_state)
            return solution_path[::-1]
        closed_set.add(tuple(map(tuple, current_node.state)))
        blank_x, blank_y = get_blank_position(current_node.state)
        possible_actions = get_possible_actions(blank_x, blank_y)
        for new_x, new_y in possible_actions:
            new_state = apply_action(current_node.state, blank_x, blank_y, new_x, new_y)
            if tuple(map(tuple, new_state)) not in closed_set:
                new_node = PuzzleNode(new_state, current_node, (new_x, new_y))
                new_node.g = current_node.g + 1
                heapq.heappush(open_set, new_node)
    return None
def print_puzzle(puzzle_state):
    for row in puzzle_state:
        print(' '.join(str(tile) for tile in row))
if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [5, 6, 8],
    [4, 7, 0]
    ]
    print("Initial Puzzle State:")
    print_puzzle(initial_state)
    solution_path = solve_8_puzzle(initial_state)
    if solution_path:
        print("\nSolution:")
        for step, state in enumerate(solution_path):
            print(f"Step {step + 1}:")
            print_puzzle(state)
            print()
    else:
        print("\nNo solution found.")
