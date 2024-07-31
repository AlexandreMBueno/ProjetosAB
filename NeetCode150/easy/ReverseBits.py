class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0 # aq sera o nosso numero invertido

        for i in range(32): # 32 vezes pq eh o tamanho
            bit = (n >> i) & 1 # n vai p direita i posicoes
            # na linha acima, o & 1 eh p isolar o ultimo bit
            # isso pq precisamos pegar bit a bit para poder reverter
            result += (bit << (31 - i)) # muda o bit p direita em 31 - i
        # bit extraido eh jogado la p comeco p fzr a inversao       
        return result

# teste
# b necessario para dizer q e binario
n = 0b0000000000000000000000000010101

solution = Solution()
print(solution.reverseBits(n))