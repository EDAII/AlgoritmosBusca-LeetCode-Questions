from sudoku_solver import Solution

class SudokuSolverTester:
    def print_board(self, board):

        for row in board:
            print(row)
    
    def test_case(self, board):
        print("\nOriginal:")
        self.print_board(board)
        
        solution = Solution()
        solution.solveSudoku(board)
        
        print("\nResolvido:")
        self.print_board(board)
        print("-" * 40)

def main():
    tester = SudokuSolverTester()
    
    exemplo_1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    exemplo_2  = [
        ["1", ".", ".", ".", "3", ".", ".", ".", "."],
        [".", ".", "7", "8", ".", ".", "5", ".", "."],
        [".", "4", "8", ".", ".", "5", ".", ".", "."],
        [".", "1", ".", "9", ".", ".", ".", ".", "7"],
        ["5", "9", ".", ".", ".", ".", ".", "6", "8"],
        ["7", ".", ".", ".", ".", "3", ".", "2", "."],
        [".", ".", ".", "3", ".", ".", "7", "4", "."],
        [".", ".", "6", ".", ".", "1", "2", ".", "."],
        [".", ".", ".", ".", "9", ".", ".", ".", "6"]
    ]
        
    # Testando o exemplo 1
    print("Executando Teste para o Exemplo 1:")
    tester.test_case(exemplo_1)
        
    # Testando o exemplo 2
    print("Executando Teste para o Exemplo 2:")
    tester.test_case(exemplo_2)

if __name__ == '__main__':
    main()