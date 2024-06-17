# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # se a root for null
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # calculamos a profundidade p esquerda e p direita
        # e retorna a profundidade max entre os dois
        # o +1 serve para contar a raiz da arvore
        # fazemos chamada recursiva pros dois lados da arvore

# Teste
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)

solution = Solution()
print(solution.maxDepth(root))  # Output esperado: 3
