from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_valor = float('inf') # para q qualquer n seja menor
        max_lucro = 0

        for preco in prices: # p/ cada um dos precos
            if preco < min_valor: # se for menor q inifnito
                min_valor = preco # atualiza o menor
            lucro = preco - min_valor # lucro e a diferenca
            if lucro > max_lucro: # se lucro > 0 inicial
                max_lucro = lucro # atualiza max_lucro
        return max_lucro  # retorna ele

solution = Solution()

# teste 1
prices1 = [10, 1, 5, 6, 7, 1]
output1 = solution.maxProfit(prices1)
print(f"Input: {prices1}\nOutput: {output1}\nExpected Output: 6\n")

# Teste 2
prices2 = [10, 8, 7, 5, 2]
output2 = solution.maxProfit(prices2)
print(f"Input: {prices2}\nOutput: {output2}\nExpected Output: 0\n")
