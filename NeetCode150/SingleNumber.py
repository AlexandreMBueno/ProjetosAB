'''
Em Python, "xor" refere-se ao operador de "exclusive or" (ou exclusivo).
O "xor" é um operador bit a bit, representado por ^ que:
Retorna
    1 se os bits correspondentes de seus operandos forem diferentes
    0 se os bits correspondentes de seus operandos forem iguais. 

  0101  (5 em binário)
^ 0011  (3 em binário)
-------
  0110  (6 em binário)
'''

a = 5  # em binário: 0101
b = 3  # em binário: 0011

resultado = a ^ b

print(resultado)  # saída: 6, que em binário é 0110


# entao, para resolver o problema SingleNumber, a solucao usa ^
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
    
solution = Solution()
nums = [4, 1, 2, 1, 2]
print(solution.singleNumber(nums)) 