from collections import deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stop_to_routes = {}
        for route_idx, route in enumerate(routes):
            route_set = set(route)
            for stop in route_set:
                if stop not in stop_to_routes:
                    stop_to_routes[stop] = []
                stop_to_routes[stop].append(route_idx)
        
        if source not in stop_to_routes or target not in stop_to_routes:
            return -1
        
        route_sets = [set(route) for route in routes]
        target_routes = set(stop_to_routes[target])
        
        queue = deque([(source, 0)])
        visited_stops = {source}
        visited_routes = set()
        
        while queue:
            current_stop, buses_taken = queue.popleft()
            
            for route_idx in stop_to_routes[current_stop]:
                if route_idx in visited_routes:
                    continue
                
                if route_idx in target_routes:
                    return buses_taken + 1
                
                visited_routes.add(route_idx)
                
                for next_stop in route_sets[route_idx]:
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses_taken + 1))
        
        return -1