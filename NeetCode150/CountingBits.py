from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        offset = 1 #highest power of 2
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp

# 1. Inicializa a lista dp com n + 1 zeros para armazenar a contagem de bits 1 de 0 ate n.
# 2. offset mantem a maior potencia de 2 encontrada ate o momento.
# 3. Para cada numero i de 1 ate n:
#    - Atualiza offset se i for uma nova potencia de 2.
#    - Calcula dp[i] como 1 + dp[i - offset], onde dp[i - offset] ja foi calculado.
# 4. Retorna a lista dp com a contagem de bits 1 para cada numero de 0 ate n.

n = 4
solution = Solution()
print(solution.countBits(n))