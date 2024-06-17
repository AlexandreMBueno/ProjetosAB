# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        resultado = [0]

        def dfs(root): # parametro -> node q estamos comecando
            if not root: # se root for null
                return -1 # -1 eh a altura do root.
            left = dfs(root.left) # pegando a profundidade(height) de left
            right = dfs(root.right) # "              " de right
            resultado[0] = max(resultado[0], 2 + left + right) # diametro do root q viemos
            # diametro eh 2 + left + right


            return 1 + max(left, right)
            # qualquer q seja a altura max em left ou right
            # adicionando 1, sera a altura passando pelo root
            # root  = no raiz

        dfs(root)
        return resultado[0]
    
# teste 1
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(5)

# instancia e chamando metodo
solution = Solution()
output = solution.diameterOfBinaryTree(root)
print(output)  # Esperado: 3