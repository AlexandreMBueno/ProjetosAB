class Solution:
    def calculadora(self, a, b):

        if opcao == 1:
            return a + b
        elif opcao == 2:
            return a - b
        elif opcao == 3:
            return a * b
        elif opcao == 4:
            return a / b

opcao = 4
a = 2
b = 5
solution = Solution()
print(solution.calculadora(a, b))
