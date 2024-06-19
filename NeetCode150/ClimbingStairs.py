class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        else:
            return self.climbStairs(n -1) + self.climbStairs(n-2)

# Teste
solution= Solution()
n = 3
result = solution.climbStairs(n)
print(f"Input: n = {n}\nOutput: {result}")

# 1 1 1
# 1 2
# 2 1

# o número de maneiras de chegar ao degrau n é:
# a soma do número de maneiras de chegar ao degrau n-1 e ao degrau n-2.

# f(n) = f(n - 1) + f(n - 2) FIBONACCI