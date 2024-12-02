sudoku = [
    0, 0, 4, 0, 5, 0, 0, 0, 0,
    9, 0, 0, 7, 3, 4, 6, 0, 0,
    0, 0, 3, 0, 2, 1, 0, 4, 9,
    0, 3, 5, 0, 9, 0, 4, 8, 0,
    0, 9, 0, 0, 0, 0, 0, 3, 0,
    0, 7, 6, 0, 1, 0, 9, 2, 0,
    3, 1, 0, 9, 7, 0, 2, 0, 0,
    0, 0, 9, 1, 8, 2, 0, 0, 3,
    0, 0, 0, 0, 6, 0, 1, 0, 0
]

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def options(cell, sudoku):
    """Determines the available values for a given cell."""
    column = {v for ix, v in enumerate(sudoku) if ix % 9 == cell % 9}
    row = {v for ix, v in enumerate(sudoku) if ix // 9 == cell // 9}
    box = {v for ix, v in enumerate(sudoku) if (ix // (9 * 3) == cell // (9 * 3)) and ((ix % 9) // 3 == (cell % 9) // 3)}
    return numbers - (box | row | column)

def is_valid_sudoku(grid):
    """Validates the Sudoku grid to ensure it is in correct format and has valid values."""
    if len(grid) != 81:
        return False
    for value in grid:
        if value not in range(0, 10):
            return False
    return True

def sudoku_solver(sudoku):
    """Solves the Sudoku puzzle using a backtracking approach."""
    
    if not all(0 <= value <= 9 for value in sudoku):
        raise ValueError("Sudoku contains invalid values; must be between 0 and 9.")
    
    state = sudoku[:]
    
    def find_empty_cell(state):
        """Find the next empty cell in the Sudoku grid (represented by 0)."""
        for i in range(len(state)):
            if state[i] == 0:
                return i
        return None  
    
    def solve(state):
        """Recursive backtracking function."""

        empty_cell = find_empty_cell(state)
        
        if empty_cell is None:
            return state  # Puzzle solved
        
        for value in options(empty_cell, state):
            new_state = state[:]
            new_state[empty_cell] = value  # Try this value
            
            result = solve(new_state)
            if result:
                return result 
        
        return None  
    
    return solve(state)

solved_sudoku = sudoku_solver(sudoku)
if solved_sudoku:
    print("Solved Sudoku:")
    for i in range(9):
        print(solved_sudoku[i*9:(i+1)*9])
else:
    print("No solution exists.")