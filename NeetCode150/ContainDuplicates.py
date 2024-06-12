from typing import List # nao precisa no neetcode

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set() #caixa separada com numero nn duplicados

        for number in nums:
            if number in hashset: # se tiver nessa cx
                return True # retorna true e ja tem duplicado
            hashset.add(number) # add o numero dentro do hashset
        return False # se nao, retorna false
    
solution = Solution()

# teste 1
nums1 = [1, 2, 3, 3]
print(solution.hasDuplicate(nums1))

# teste 2
nums2 = [1, 2, 3, 4]
print(solution.hasDuplicate(nums2))

# a forma como esse codigo funciona  basicamente cria uma caixinha separada (hashset)
# essa caixa comeca vazia e vamos adicionando os itens la dentro verificando com oq ja ta la
# assim, evitamos uso de memoria excessivo de verificar como cada um dos outros numeros
# se nao tem no hashset, add la dentro, se ja tem, retorna True pq encontrou duplicata
 