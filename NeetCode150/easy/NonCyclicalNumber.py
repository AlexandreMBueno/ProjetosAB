# cria hashset para numeros visitados
# enquanto n nao visitado
# adicionar n ao hashset
# atualiza n para (chama a funcao sumOfSquares, que tem a logica do ex) a soma dos quadrados dos digitos
# se n for 1, retorna que eh happy number
# se loop terminar, nao e happy number

#logica:
# enquanto n nao for zero
# pegar ultimo digito
# quadrado do digito
# adicionar ao output (output e usado p armazenar a soma dos quadrados dos digitos)
# remover ultimo digito e volta ao loop


class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set() # hashset

        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True

        return False

        # vms fzr mod 10 p pegar o segundo valor
        # e /10 p pegar o primeiro valor
    def sumOfSquares(self, n:int) -> int:
        output = 0

        while n: # while n not zero
            digit = n % 10 # p pegar o ultimo digito
            digit = digit ** 2 # quadrado dele
            output += digit # passa esse valor p output
            n = n // 10 # pega o primeiro valor, joga p loop dnv
        return output

# teste 1 -> deve ser false
n = 101
solution = Solution()
print(solution.isHappy(n))