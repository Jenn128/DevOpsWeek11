import unittest
from sudoku import sudoku_solver

class TestSudokuSolver(unittest.TestCase):

    def test_sudoku_solver_basic(self):
        sudoku = [
            5, 3, 0, 6, 0, 8, 9, 1, 2,
            6, 0, 2, 1, 9, 5, 3, 4, 8,
            1, 9, 8, 3, 4, 2, 5, 6, 7,
            8, 5, 9, 7, 6, 1, 4, 2, 3,
            4, 2, 6, 8, 5, 3, 7, 9, 1,
            7, 1, 3, 9, 2, 4, 8, 5, 6,
            9, 6, 1, 5, 3, 7, 2, 8, 4,
            2, 8, 7, 4, 1, 9, 6, 3, 5,
            3, 4, 5, 2, 8, 6, 1, 7, 9
        ]
        solved_sudoku = sudoku_solver(sudoku)
        self.assertIsNotNone(solved_sudoku)
        self.assertEqual(len(solved_sudoku), 81)
        self.assertTrue(all(1 <= v <= 9 or v == 0 for v in solved_sudoku))

    def test_sudoku_solver_already_solved(self):
        sudoku = [
            5, 3, 4, 6, 7, 8, 9, 1, 2,
            6, 7, 2, 1, 9, 5, 3, 4, 8,
            1, 9, 8, 3, 4, 2, 5, 6, 7,
            8, 5, 9, 7, 6, 1, 4, 2, 3,
            4, 2, 6, 8, 5, 3, 7, 9, 1,
            7, 1, 3, 9, 2, 4, 8, 5, 6,
            9, 6, 1, 5, 3, 7, 2, 8, 4,
            2, 8, 7, 4, 1, 9, 6, 3, 5,
            3, 4, 5, 2, 8, 6, 1, 7, 9
        ]
        solved_sudoku = sudoku_solver(sudoku)
        self.assertEqual(sudoku, solved_sudoku)  

    def test_sudoku_solver_hard(self):
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
        solved_sudoku = sudoku_solver(sudoku)
        self.assertIsNotNone(solved_sudoku)
        self.assertTrue(all(1 <= v <= 9 for v in solved_sudoku))

    def test_sudoku_solver_invalid(self):
        invalid_sudoku = [
            0, 0, 4, 0, 5, 0, 0, 0, 0,
            9, 0, 0, 7, 3, 4, 6, 10, 0,
            0, 0, 3, 0, 2, 1, 0, 4, 9,
            0, 3, 5, 0, 9, 0, 4, 8, 0,
            0, 9, 0, 0, 0, 0, 0, 3, 0,
            0, 7, 6, 0, 1, 0, 9, 2, 0,
            3, 1, 0, 9, 7, 0, 2, 0, 0,
            0, 0, 9, 1, 8, 2, 0, 0, 3,
            0, 0, 0, 0, 6, 0, 1, 0, 0
        ]
        with self.assertRaises(ValueError):
            sudoku_solver(invalid_sudoku)

    def test_sudoku_solver_noSolution(self):
        unsolvable_sudoku = [
            5, 3, 0, 0, 7, 0, 0, 0, 0,
            6, 0, 0, 1, 9, 5, 0, 0, 0,
            0, 9, 8, 0, 0, 0, 0, 6, 0,
            8, 0, 0, 0, 6, 0, 0, 0, 3,
            4, 0, 0, 8, 0, 3, 0, 0, 1,
            7, 0, 0, 0, 2, 0, 0, 0, 6,
            0, 6, 0, 0, 0, 0, 2, 8, 0,
            0, 0, 0, 4, 1, 9, 0, 0, 5,
            0, 0, 0, 0, 8, 0, 0, 7, 9
        ]
        solved_sudoku = sudoku_solver(unsolvable_sudoku)
        if solved_sudoku:
            print("Solved Sudoku:")
        for i in range(9):
            print(solved_sudoku[i*9:(i+1)*9])
        else:
            print("No solution exists.")

    def test_sudoku_solver_Unsolvable(self):
        impossible_sudoku = [
            1, 2, 3, 4, 5, 6, 7, 8, 9,
            1, 2, 3, 4, 5, 6, 7, 8, 9,
            1, 2, 3, 4, 5, 6, 7, 8, 9,
            1, 2, 3, 4, 5, 6, 7, 8, 9,
            1, 2, 3, 4, 5, 6, 7, 8, 9,
            1, 2, 3, 4, 5, 6, 7, 8, 9,
            1, 2, 3, 4, 5, 6, 7, 8, 9,
            1, 2, 3, 4, 5, 6, 7, 8, 9,
            1, 2, 3, 4, 5, 6, 7, 8, 9
        ]
        solved_sudoku = sudoku_solver(impossible_sudoku)
        if solved_sudoku:
            print("Solved Sudoku:")
        for i in range(9):
            print(solved_sudoku[i*9:(i+1)*9])
        else:
            print("No solution exists.")