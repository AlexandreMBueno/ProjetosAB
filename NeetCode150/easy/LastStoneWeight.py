# heap eh uma arvore binaria
# minheap seria uma arvore em que o no raiz tem o menor valor da arvore
# maxheap seria uma arvore em que o no raiz tem o maior valor da arvore

# heapq.heappush(heap, item)
    # Insere um item no heap.

# heapq.heappop(heap)
    # Remove e retorna o menor item do heap.

# heapq.heappushpop(heap, item)
    # Insere um item e, em seguida, remove e retorna o menor item em uma única operação.

# heapq.heapify(x)
    # Transforma a lista x em um heap.

# nao temos max heap em python
# usamos min heap(arvore binaria em q o menor valor eh o root)
# vms usar min heap, multiplicar tds por -1. ex 8,5,3 -> -8,-5,-3
# assim pegamos o menor valor (-8) e dps pegamos o valor absoluto(8)

import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # * -1
        heapq.heapify(stones) # deixando em arvore

        while len(stones) > 1:
            first_stone = heapq.heappop(stones) # 1 maior
            second_stone = heapq.heappop(stones) # 2 maior
            if second_stone > first_stone:
                heapq.heappush(stones, first_stone - second_stone ) # add a stones


        stones.append(0) # se n tiver mada, add 0 p retornar ele
        return abs(stones[0]) # abs p ser positivo
    
# Teste
solution = Solution()
stones = [2, 3, 6, 2, 4]
result = solution.lastStoneWeight(stones)
print(f"Input: stones = {stones}")
print(f"Output: {result}") # Esperado: 1