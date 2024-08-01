'''
    Inicializa res com 1 em todas as posicoes.
    Calcula o produto prefixo para cada posicao.
    Percorre nums de tras para frente.
    Multiplica res[i] pelo produto sufixo atual.
    Atualiza postfix com o proximo elemento.
    Retorna a lista res.
'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

# Teste 1
test_input = [1, 2, 4, 6]
solution = Solution()
output = solution.productExceptSelf(test_input)
print(f"Input: {test_input}")
print(f"Output: {output}")
