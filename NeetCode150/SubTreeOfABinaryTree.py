# Definition for a binary tree node.


# achei essa bem complexa, rever para concretizar conceitos e a forma como funciona

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True # pq toda arvore tem uma arvore vazia em algum filho por ex
        if not root: return False

        if self.sameTree(root, subRoot):  # Verifica se arvore atual root == subRoot
            return True  # Se for igual, retorna True, ou seja subRoot é uma subarvore de root

        # se nao, continua verificando recursivamente nas sub-arvores a left e a right de root
        return(self.isSubtree(root.left, subRoot) or  # verifica se subRoot eh uma subarvore do filho esquerdo de root
                self.isSubtree(root.right, subRoot))  # verifica se subRoot eh uma subarvore do filho direito de root


    def sameTree(self, root, subRoot): # funcao auxiliar p ver se e a mesma arvore
        if not root and not subRoot: # se ambos sao nulos, subRoot eh sim uma subarvore de root
            return True # por isso retorna True
        if root and subRoot and root.val == subRoot.val: # se existem e tem valores iguais
            return(self.sameTree(root.left, subRoot.left) and # aplica a funcao(forma recursiva) p LL e RR
                    self.sameTree(root.right, subRoot.right))
        return False # se nao existem ou tem valores diferentes ja retorna false
    
solution = Solution()

#  teste
# arvore root
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# arvore subRoot
subRoot = TreeNode(2)
subRoot.left = TreeNode(4)
subRoot.right = TreeNode(5)

solution = Solution()
result = solution.isSubtree(root, subRoot)
print(result)  # True

