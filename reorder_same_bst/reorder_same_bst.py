from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # fatoriais para combinações
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = (fact[i-1] * i) % MOD
        
        def mod_inverse(a, mod):
            return pow(a, mod - 2, mod)
        
        def combination(n, k):
            if k > n or k < 0:
                return 0
            return (fact[n] * mod_inverse(fact[k], MOD) % MOD * mod_inverse(fact[n-k], MOD)) % MOD
        
        def count_ways(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left_subtree = []
            right_subtree = []
            
            for num in arr[1:]:
                if num < root:
                    left_subtree.append(num)
                else:
                    right_subtree.append(num)
            
            left_ways = count_ways(left_subtree)
            right_ways = count_ways(right_subtree)
            
            total_elements = len(left_subtree) + len(right_subtree)
            ways_to_merge = combination(total_elements, len(left_subtree))
            
            return (left_ways * right_ways % MOD * ways_to_merge) % MOD
        
        return (count_ways(nums) - 1) % MOD