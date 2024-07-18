import operator
from itertools import permutations, product

# List of operator functions and symbols
operator_functions = [operator.add, operator.sub, operator.mul, operator.truediv]
operator_symbols = {
    operator.add: '+',
    operator.sub: '-',
    operator.mul: '*',
    operator.truediv: '/',
}

def calculator(a, b, op):
    """Apply an operation and handle division by zero."""
    if a != None and b != None:
        try:
            return op(a, b)
        except ZeroDivisionError:
            return None
    else:
        return None

def answer_checker(numbers, ops):
    """Tries for the given combination of numbers and operators all the expressions"""
    a, b, c, d = numbers
    op1, op2, op3 = ops

    # All possible ways to group the operations
    expressions = [
        (calculator(calculator(calculator(a, b, op1), c, op2), d, op3), f"(({a} {operator_symbols[op1]} {b}) {operator_symbols[op2]} {c}) {operator_symbols[op3]} {d}"),
        (calculator(calculator(a, calculator(b, c, op2), op1), d, op3), f"({a} {operator_symbols[op1]} ({b} {operator_symbols[op2]} {c})) {operator_symbols[op3]} {d}"),
        (calculator(a, calculator(calculator(b, c, op2), d, op3), op1), f"{a} {operator_symbols[op1]} (({b} {operator_symbols[op2]} {c}) {operator_symbols[op3]} {d})"),
        (calculator(calculator(a, b, op1), calculator(c, d, op3), op2), f"({a} {operator_symbols[op1]} {b}) {operator_symbols[op2]} ({c} {operator_symbols[op3]} {d})"),
        (calculator(a, calculator(b, calculator(c, d, op3), op2), op1), f"{a} {operator_symbols[op1]} ({b} {operator_symbols[op2]} ({c} {operator_symbols[op3]} {d}))")
    ]

    # Filter out None results caused by division by zero
    valid_expressions = [(result, expr) for result, expr in expressions if result is not None]
    return valid_expressions

def solution_finder(numbers, target=24):
    """Find a combination of operations that result in the target value."""
    for num_perm in permutations(numbers):
        for ops in product(operator_functions, repeat=3):
            for result, expression in answer_checker(num_perm, ops):
                if abs(result - target) < 1e-6:  # Handle floating-point precision
                    return expression
    return None

def main():
    while True:
        input_numbers = []
        print("Hello everyone! this is your game 24 solution finder. Give me the four numbers and I will give you a solution if possible.")
        for i in range(4):
            input_numbers.append(int(input(f"Give me number {i+1}: ")))
        solution = solution_finder(input_numbers)
        if solution:
            print(f"Solution: {solution}. Try another!")
            input_numbers = []
        else:
            print("No solution found. Try another!")
            input_numbers = []

if __name__ == "__main__":
    main()


