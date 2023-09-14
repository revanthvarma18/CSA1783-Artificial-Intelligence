class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.location = 0  # Start at position 0

    def move_left(self):
        if self.location > 0:
            self.location -= 1

    def move_right(self):
        if self.location < len(self.grid) - 1:
            self.location += 1

    def clean(self):
        self.grid[self.location] = 0  # Mark the square as clean

    def is_dirty(self):
        return self.grid[self.location] == 1

    def print_status(self):
        status = "Clean" if not self.is_dirty() else "Dirty"
        print(f"Location {self.location}: {status}")

def vacuum_cleaner_world(grid):
    cleaner = VacuumCleaner(grid)
    steps = 0

    while any(cleaner.grid):  # Continue until all squares are clean
        cleaner.print_status()

        if cleaner.is_dirty():
            cleaner.clean()
            steps += 1

        if cleaner.location == 0:
            cleaner.move_right()
            steps += 1
        elif cleaner.location == len(grid) - 1:
            cleaner.move_left()
            steps += 1
        else:
            # Decide whether to move left or right based on the dirtiness of the adjacent squares
            left_square = grid[cleaner.location - 1]
            right_square = grid[cleaner.location + 1]
            if left_square == 1 and right_square == 0:
                cleaner.move_left()
                steps += 1
            elif left_square == 0 and right_square == 1:
                cleaner.move_right()
                steps += 1
            else:
                # Randomly choose left or right if both squares are of the same dirtiness
                import random
                move_direction = random.choice(["left", "right"])
                if move_direction == "left":
                    cleaner.move_left()
                else:
                    cleaner.move_right()
                steps += 1

    cleaner.print_status()
    print(f"Cleaning completed in {steps} steps.")

# Test case 1
grid1 = [1, 0, 1, 0, 1]
print("Test Case 1:")
vacuum_cleaner_world(grid1)

# Test case 2
grid2 = [1, 1, 1, 1, 1]
print("\nTest Case 2:")
vacuum_cleaner_world(grid2)
