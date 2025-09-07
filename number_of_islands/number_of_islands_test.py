from number_of_islands import Solution

def main():
    solution = Solution()

    map_1 = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    print("Output esperado: 1")
    print("Output obtido:", solution.numIslands(map_1))

    map_2 = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    print("Output esperado: 3")
    print("Output obtido:", solution.numIslands(map_2))

if __name__ == "__main__":
    main()