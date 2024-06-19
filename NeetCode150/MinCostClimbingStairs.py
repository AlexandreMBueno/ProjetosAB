from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

            # Adiciona 0 ao final da lista de custos (objetivo e o topo da escada)
            cost.append(0)

            # atualiza a lista de custos de tras para frente
            for i in range(len(cost) - 3, -1, -1):
                # Cada posicao na lista agora contem o custo minimo para alcancar o topo a partir daquela posicao
                cost[i] += min(cost[i + 1], cost[i + 2])

            # Retorna o menor custo entre as duas primeiras posicoes, pois podemos comecar do degrau 0 ou 1
            return min(cost[0], cost[1])
        

# Teste
cost = [1, 2, 1, 2, 1, 1, 1]
solution = Solution()
output = solution.minCostClimbingStairs(cost)
print(f"Input: {cost}")
print(f"Output: {output}")  # Output esperado: 4

