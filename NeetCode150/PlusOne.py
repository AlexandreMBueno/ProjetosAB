# Esta funcao implementa a operacao de incrementar um ao numero representado 
# pelo array digits, onde cada elemento do array e um digito do numero.
# 1. Calcula a posicao do ultimo digito (p) e incrementa este digito em 1.
# 2. Usa um loop while para verificar se ha algum carry para ser propagado:
#    - Se o digito for maior que 9, ajusta o digito para 0 e propaga o carry.
#    - Se estiver na primeira posicao (p == 0) e o carry precisa ser propagado, 
#      insere um novo digito 1 no inicio do array.
# 3. Decrementa p para verificar o proximo digito a esquerda.
# 4. Retorna o array digits atualizado.

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p = len(digits) -1
        digits[p] += 1

        while p >= 0:
            if digits[p] > 9:
                digits[p] = 0
                if p == 0:
                    digits.insert(0, 1)
                else:
                    digits[p- 1] += 1
            p -= 1
        return digits
    
digits = [9, 9, 9]
solution = Solution()
print(solution.plusOne(digits))