# explicacao
# result += n % 2:
# adiciona o valor do bit menos significativo(ultimo) ao contador.
# Por exemplo: 101 % 2 resulta em 1, então adiciona 1 ao resultado.
# Se o bit for 0, nada é adicionado.
# Isso continua até que todos os bits tenham sido verificados.

class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0 # aqui guardamos a contagem de 1
        while n > 0: # enquanto for maior q 0
            result += n % 2 # mod dele, p pegar a sobra e se for 1...
            n = n >> 1 # >> serve para passarmo p proximo bit
        return result


# necessario colocar esse b para dizer que o numero a seguir esta em formato binario
n = 0b00000000000000000000000000010111
solution = Solution()
print(solution.hammingWeight(n))