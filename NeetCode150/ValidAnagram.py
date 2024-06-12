class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False # anagramas tem q ter msm qtd letras

        count_s = {} # contagem das letras
        count_t = {}

        for letter in s:
            if letter in count_s:
                count_s[letter] += 1 # incrementa valor em 1
            else:
                count_s[letter] = 1  # add letra com valor 1

        for letter in t:
            if letter in count_t:
                count_t[letter] += 1
            else:
                count_t[letter] = 1 

        #print(count_s)
        #print(count_t)
        return count_s == count_t # retorna se sao iguais
    
# p testar no vscode
solution = Solution()

# teste 1
result1 = solution.isAnagram("racecar", "carrace")
print("Teste 1", result1) # deve ser True

# teste 2
result2 = solution.isAnagram("jar", "jam")
print("Teste 2", result2) # deve ser False