class Solution:
    def numIslands(self, grade: list[list[str]]) -> int:
        if not grade:
            return 0

        num_islands = 0
        linhas, colunas = len(grade), len(grade[0])

        def dfs(lin, col):
            if lin < 0 or lin >= linhas or col < 0 or col >= colunas or grade[lin][col] == "0":
                return
            grade[lin][col] = "0" 
            dfs(lin - 1, col)  
            dfs(lin + 1, col) 
            dfs(lin, col - 1) 
            dfs(lin, col + 1) 

        for linha in range(linhas):
            for coluna in range(colunas):
                if grade[linha][coluna] == "1":
                    num_islands += 1
                    dfs(linha, coluna)

        return num_islands