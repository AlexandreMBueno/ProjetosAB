class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        verifica se s t tem a msm qntd de letras
        se nao, ja retorna false
        iniciar dois dicionario para guardar:
        1 - a letra(chave)
        2 - numero de x q a letra aparece(valor)
        p cada uma das letras das strings
        verifica se a letra ta no dicionario
        se sim, aumentamos o valor dela em 1  -> +=1
        se nao, adicionamos ela no dic com valor 1   -> = 1
        repete o processo p outra string, t
        retorna os dois dicionarios, com return dic1 == dic2
        se forem iguais, vai retornar True, caso contrario, False    
        '''
        if len(s) != len(t):
            return False

        dic_s = {}
        dic_t = {}

        for l in s:
            if l in dic_s:
                dic_s[l] = dic_s[l] + 1
            else:
                dic_s[l] = 1

        for l in t:
            if l in dic_t:
                dic_t[l] = dic_t[l] + 1
            else:
                dic_t[l] = 1

        return dic_s == dic_t
        
    
# teste 1
solution = Solution()

# teste 1
result1 = solution.isAnagram("racecar", "carrace")
print("Teste 1", result1) # deve ser True

# teste 2
result2 = solution.isAnagram("jar", "jam")
print("Teste 2", result2) # deve ser False