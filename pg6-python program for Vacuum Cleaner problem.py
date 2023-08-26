class VacuumCleaner:
print(“program was run by bharath”)
    def __init__(self):
        self.position = 0  
        self.environment = [0, 0] 
    def sense(self):
        return self.environment[self.position]

    def move(self):
        if self.position == 0:
            self.position = 1
        else:
            self.position = 0

    def clean(self):
        self.environment[self.position] = 0

    def run(self, steps):
        for _ in range(steps):
            current_state = self.sense()
            if current_state == 1: 
                self.clean()
                print(f"Cleaned cell {self.position}")
            else:
                print(f"Cell {self.position} is already clean.")
            self.move()
if __name__ == "__main__":
    vacuum_cleaner = VacuumCleaner()
    steps = 5
    print("Initial environment:", vacuum_cleaner.environment)
    vacuum_cleaner.run(steps)
    print("Final environment:", vacuum_cleaner.environment)
