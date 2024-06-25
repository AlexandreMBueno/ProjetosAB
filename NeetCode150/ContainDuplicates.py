from typing import List # nao precisa no neetcode

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        criar um hashset [   ]
        p cada um dos numeros em nums
        verificar se ele ja ta no hashSet (caixa)
        se ja tiver, retorna true pq encontramos um duplicado
        se nao, add ele no hashSet
        e continua verificando
        assim, evitamos uso de memoria excessivo de verificar como cada um dos outros numeros
        '''

        hashSet = set() # criando hashet
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False
    
solution = Solution()

# teste 1
nums1 = [1, 2, 3, 3]
print(solution.hasDuplicate(nums1))

# teste 2
nums2 = [1, 2, 3, 4]
print(solution.hasDuplicate(nums2))

# a forma como esse codigo funciona  basicamente cria uma caixinha separada (hashset)
# essa caixa comeca vazia e vamos adicionando os itens la dentro verificando com oq ja ta la
# se nao tem no hashset, add la dentro, se ja tem, retorna True pq encontrou duplicata
 