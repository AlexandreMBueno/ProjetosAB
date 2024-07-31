# A função enumerate() em Python adiciona um contador aos itens de um iterável(como uma lista ou uma tupla)
# Esse contador normalmente serve como índice.

# Cada item retornado por enumerate() é uma tupla, consistindo de dois elementos:
# O índice (ou contador) do item
# O valor do item 

# exemplo dessa funcao
# index eh a posicao do item
# item eh o valor atribuido a chave index
lista = ['laranja', 'banana', 'kiwi']
for index, item in enumerate(lista):
    print(index, item)

# -----------------------------
# exercicio neetcode:

from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       listNumber = {} # armazena chave: valor -> num: index

       for i, n in enumerate(nums): # indice i valor n
        diferenca = target - n
        if diferenca in listNumber: # diferenca ta na listnumber
            return [listNumber[diferenca], i] # retorna indices
        listNumber[n] = i # indice i do valor n na listNumber

# comentario linha 27 do return
# Retorna os indices dos dois elementos cuja soma e igual ao valor 'target'.
# O primeiro e o indice recuperado do dicionario listNumber para a chave 'diferenca',
# e o segundo e o indice atual 'i' no loop."

solution = Solution()

# teste 1
nums1 = [3, 4, 5, 6]
target1 = 7
print("Teste 1", solution.twoSum(nums1, target1)) # deve ser [0, 1]

# teste 2
nums2 = [4, 5, 6]
target2 = 10
print("Teste 2", solution.twoSum(nums2, target2)) # dever ser [0, 2]