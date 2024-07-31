'''
inicializamos um dicionario para agrupar os anagramas
Percorre cada palavra na lista com as palavras
Conta a frequencia de cada letra na palavra ex 1c 3a
Usa a contagem como chave no dicionario
Adiciona a palavra ao grupo de anagramas correspondente
Retorna os grupos de anagramas
'''

from collections import defaultdict
from typing  import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # mapeando charCount p list de anagramas

        for s in strs:
            count = [0] * 26 # 26 zeros, um para cada caracter 

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return result.values()

# ord -> funcao do py que retorna o valor inteiro
# representando o codigo Unicode de um determinado caractere.

solution = Solution()

strs = ["act", "pots", "tops", "cat", "stop", "hat"]
output = solution.groupAnagrams(strs)
print("Input:", strs)
print("Output:", output)