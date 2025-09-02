class Solution:
    def solveSudoku(self, tabuleiro: list[list[str]]) -> None:
        self.tabuleiro = tabuleiro
        self.solve()

    def solve(self) -> bool:
        for linha in range(9):
            for coluna in range(9):
                if self.tabuleiro[linha][coluna] == '.':
                    for num in "123456789":
                        if self.is_valid(linha, coluna, num):
                            self.tabuleiro[linha][coluna] = num
                            if self.solve():
                                return True
                            self.tabuleiro[linha][coluna] = '.'
                    return False
        return True

    def is_valid(self, linha: int, coluna: int, num: str) -> bool:
        if num in self.tabuleiro[linha]:
            return False

        for row in range(9):
            if self.tabuleiro[row][coluna] == num:
                return False

        linha_inicial = (linha // 3) * 3
        coluna_inicial = (coluna // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[linha_inicial + i][coluna_inicial + j] == num:
                    return False

        return True

if __name__ == '__main__':
    result = Solution()
    
    tabuleiro = [
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
    
    print("\nTabuleiro Original:")
    for row in tabuleiro:
        print(row)
    
    result.solveSudoku(tabuleiro)
    
    print("\nTabuleiro Resolvido:")
    for row in tabuleiro:
        print(row)
