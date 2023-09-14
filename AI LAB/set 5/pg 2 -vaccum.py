import random

class VacuumWorld:
    def __init__(self):
        self.squares = {'A': 'clean', 'B': 'clean'}  # Initialize the squares as clean
        self.agent_location = random.choice(['A', 'B'])  # Start agent in a random square

    def percept(self):
        return self.agent_location, self.squares[self.agent_location]

    def act(self, action):
        current_location, current_status = self.percept()

        if action == 'vacuum':
            self.squares[current_location] = 'clean'
        elif action == 'move':
            # Move to the other square
            self.agent_location = 'A' if current_location == 'B' else 'B'

def simple_reflex_agent(vacuum_world):
    while True:
        location, status = vacuum_world.percept()

        if status == 'dirty':
            print(f"Agent is in square {location} and detects dirt. Vacuuming...")
            vacuum_world.act('vacuum')
        else:
            print(f"Agent is in square {location} and it's clean. Moving...")
            vacuum_world.act('move')

        if all(status == 'clean' for status in vacuum_world.squares.values()):
            print("Environment is clean. Agent is done.")
            break

if __name__ == "__main__":
    vw = VacuumWorld()
    print("Initial state:")
    print(vw.squares)
    print("Agent's initial location:", vw.agent_location)
    print("\nAgent actions:")
    simple_reflex_agent(vw)
