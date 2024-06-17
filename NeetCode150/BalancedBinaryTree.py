# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # precisamos retornar 2 valores 
        # ent e necessario mais uma funcao

        def dfs(root):
            if not root: return[True, 0] # arvore vazia e considerada balanceada
            # true balanceada, altura 0

            # ver se e balanceado em cada lado primeiro
            left, right = dfs(root.left), dfs(root.right)
            # ver se a partir de root(raiz) e balanecado
            # abs = absolute value 
            # nessa linha abaixo, vemos se cada lado e balanceado e se
            # ... a partir de root(raiz da arvore) tambem e
            balanced =  (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return[balanced, 1 + max(left[1], right[1])]
            # altura eh 1 + max de right e left linha acima

        return dfs(root)[0] # [0] para pegar apenas se e balanceada ou nao
        # [1] seria a altura

# teste
solution = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
output = solution.isBalanced(root)
print(output)