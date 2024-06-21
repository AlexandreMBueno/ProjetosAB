# Inicializamos 'result' com o tamanho da lista 'nums'
# Em seguida, percorremos cada numero na lista usando um loop
# Adiciona o índice 'i' a 'result' e subtrai o valor nums[i] de 'result'
# No final, 'result' conterá o numero que esta faltando, pois a soma dos indices compensa a falta do numero
# comecamos, nesse caso, com result = 3
# result = result = result + i - nums[i]
# Para i = 0: result = 3 + 0 - 1 = 2
# Para i = 1: result = 2 + 1 - 2 = 1
# Para i = 2: result = 1 + 2 - 3 = 0

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)

        for i in range(len(nums)):
            result += + i - nums[i]
        return result

nums = [1, 2, 3]
solution = Solution()
print(solution.missingNumber(nums))