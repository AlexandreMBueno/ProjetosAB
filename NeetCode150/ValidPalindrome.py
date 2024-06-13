from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_formatada = ''.join(char for char in s if char.isalnum()).lower() # tira espaco pontuacao e .lower

        inicial = 0
        final = len(s_formatada) - 1 # tamanho dela -1

        while inicial < final:
            if s_formatada[inicial] != s_formatada[final]:
                return False
            inicial += 1
            final -= 1
        return True
    

solution = Solution()

# teste 1
s1 = "Was it a car or a cat I saw?"
output1 = solution.isPalindrome(s1)
print(f"Input: {s1}\nOutput: {output1}\nExpected Output: True\n")

# Teste 2
s2 = "tab a cat"
output2 = solution.isPalindrome(s2)
print(f"Input: {s2}\nOutput: {output2}\nExpected Output: False\n")
