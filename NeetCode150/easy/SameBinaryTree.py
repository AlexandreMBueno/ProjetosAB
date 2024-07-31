# Recursão é onde uma função chama a si mesma para resolver subproblemas menores de um problema maior.
# Iteração é onde um bloco de código é repetido várias vezes usando estruturas de loop, como for ou while.

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # construtor da classe
        self.val = val # inicia o no
        self.left = left # inicia filho esquerda
        self.right = right # inicia filho direita

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # se forem nulo ta equivalente
            return True
        if p and q and p.val == q.val: # abordagem interessante q eu n tinha pensando
        # alem de ver o valor igual, verifica se eles existem antes
        # linha abaixo: 
        # abordagem recursiva pois chamamos a mesma funcao dentro dela mesma
        # se fosse iterativa, usaria loop for ou while
        # verificamos: aplicamos a funcao isSameTree para p.left e q.left e p.right e q.right
        # ve se sao iguais com a logica acima, na linha 19
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

# teste 1
solution = Solution()

# criando arvores p testar

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1) # root
q.left = TreeNode(2) # no a esquerda
q.right = TreeNode(3) # no a direita

output = solution.isSameTree(p, q)
print(output)  # esperado: True