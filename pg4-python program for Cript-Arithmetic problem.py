def is_valid(puzzle, solution):

    a, b, c = puzzle
    num_a = int(''.join(str(solution[c]) for c in a))
    num_b = int(''.join(str(solution[c]) for c in b))
    num_c = int(''.join(str(solution[c]) for c in c))
    return num_a + num_b == num_c

def solve_cryptarithmetic(puzzle):
    
    letters = set(''.join(puzzle))
    

    from itertools import permutations
    for perm in permutations(range(10), len(letters)):
        solution = dict(zip(letters, perm))
        
        if is_valid(puzzle, solution):
            return solution
    
    return None


puzzle = ['SEND', 'MORE', 'MONEY']
solution = solve_cryptarithmetic(puzzle)

if solution:
    print("Solution found:")
    for word in puzzle:
        num = ''.join(str(solution[c]) for c in word)
        print(f"{word}: {num}")
else:
    print("No solution found.")
