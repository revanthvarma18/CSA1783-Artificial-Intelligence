def is_valid_assignment(assignment, letters):
    # Check if the assignment is valid (no repeated digits)
    values = list(assignment.values())
    return len(values) == len(set(values))

def evaluate_expression(expression, assignment):
    # Evaluate the expression using the given assignment
    value = 0
    for char in expression:
        value = value * 10 + assignment[char]
    return value

def solve_cryptarithmetic(equation):
    words = equation.replace("+", " ").replace("=", " ").split()
    unique_letters = set("".join(words))
    leading_letters = set(word[0] for word in words)
    letters = list(unique_letters)
    
    # Try all possible digit assignments
    from itertools import permutations
    for perm in permutations(range(10), len(letters)):
        assignment = dict(zip(letters, perm))
        
        if all(assignment[letter] != 0 for letter in leading_letters):
            left_value = evaluate_expression(words[0], assignment)
            right_value = evaluate_expression(words[1], assignment)
            result_value = evaluate_expression(words[2], assignment)
            
            if left_value + right_value == result_value:
                return assignment
    
    return None

# Example problem: SEND + MORE = MONEY
equation = "SEND + MORE = MONEY"
solution = solve_cryptarithmetic(equation)

if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print(f"{letter}: {digit}")
else:
    print("No solution found.")
