from typing import List
from bus_routes import Solution

class BusRoutesTester:
    def print_routes(self, routes: List[List[int]]):
        print("Rotas disponíveis:")
        for i, route in enumerate(routes):
            print(f"  Ônibus {i}: {route}")
    
    def test_case(self, routes: List[List[int]], source: int, target: int):
        print(f"De {source} para {target}")
        self.print_routes(routes)
        
        solution = Solution()
        result = solution.numBusesToDestination(routes, source, target)
        
        if result == -1:
            print("Resultado: Impossível chegar")
        else:
            print(f"Resultado: {result} ônibus necessários")
        
        print("-" * 40)

def main():
    tester = BusRoutesTester()
    
    test_cases = [
        ([[1,2,7],[3,6,7]], 1, 6),
        ([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12),
        ([[1,2,7],[3,6,7]], 1, 7),
        ([[1,9,12,20,23,24,35,38]], 1, 35),
        ([[1,7],[3,5]], 1, 5)
    ]
    
    for routes, source, target in test_cases:
        tester.test_case(routes, source, target)

if __name__ == "__main__":
    main()