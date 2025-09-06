from typing import List, Optional
from reorder_same_bst import Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTTester:
    def build_bst(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        root = TreeNode(nums[0])
        
        for val in nums[1:]:
            self.insert_node(root, val)
        
        return root
    
    def insert_node(self, root: TreeNode, val: int):
        if val < root.val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insert_node(root.left, val)
        else:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insert_node(root.right, val)
    
    def print_tree(self, root: Optional[TreeNode], level=0, prefix="Raiz: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.val))
            if root.left is not None or root.right is not None:
                self.print_tree(root.left, level + 1, "E--- ")
                self.print_tree(root.right, level + 1, "D--- ")
    
    def test_solution(self, nums: List[int]):
        print(f"Testando: {nums}")
        
        tree = self.build_bst(nums)
        print("Árvore:")
        self.print_tree(tree)
        print()
        
        solution = Solution()
        result = solution.numOfWays(nums)
        print(f"Resultado: {result}")
        print("-" * 30)

def main():
    tester = BSTTester()
    
    test_cases = [
        [2, 1, 3],
        [3, 4, 5, 1, 2],
        [1, 2, 3],
        [1, 3, 2],
        [3, 1, 2]
    ]
    
    for nums in test_cases:
        tester.test_solution(nums)

if __name__ == "__main__":
    main()