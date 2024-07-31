# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # se nn tiver raiz da arvore
            return None
        
        # esse algoritmo basicamente ve um no, e inverte os filhos
        var_temporaria = root.left # esquerda da arvore
        root.left = root.right
        root.right = var_temporaria

        # funcao invertTree
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Teste
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))

inverted_root = Solution().invertTree(root)

def print_tree(node):
    return [node.val] + print_tree(node.left) + print_tree(node.right) if node else []

print(print_tree(inverted_root))  # output deve ser: [1, 3, 7, 6, 2, 5, 4]

# usamos:
# DFS(Depth-First Search)é usado para buscar elementos em estruturas de dados como arvores e grafos.
# O algoritmo começa em um no raiz
# e explora o max possivel ao longo de cada ramo antes de retroceder.