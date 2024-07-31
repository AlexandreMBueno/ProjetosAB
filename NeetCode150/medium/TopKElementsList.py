
'''
Conta a frequencia de cada numero em nums e armazena em um dicionario
Organiza os numeros em uma lista de listas baseada na frequencia
Percorre as listas de frequencia da maior para a menor
Retorna os primeiros k numeros mais frequentes
'''

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


# Teste
solution = Solution()
nums = [1, 2, 2, 3, 3, 3]
k = 2
output = solution.topKFrequent(nums, k)
print("Output:", output)  # Output esperado: [3, 2]
