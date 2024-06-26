class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        primeiro, precisamos formatar e retirar os espacos, acentos e letras maiusculas
        criamos 2 variaveis,
        inicial -> p primeira letra (0)
        final -> para len(string q formatamos) - 1
        ai criamos um loop p enquanto a inicial for menor q a final
        ou seja, vamos comparar a primeira letra com a ultima 
        dentro do loop, criamos uma condicao para verificar se sao diferentes
        se forem, ja retorna False
        caso contrario, incrementamos 1 em inicial e diminuimos 1 em final
        ao final, retornamos true fora do loop caso todas as letras sejam iguais
        '''
        s_formatada = ''.join(char for char in s if char.isalnum()).lower()


        inicial = 0
        final = len(s_formatada) - 1

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
