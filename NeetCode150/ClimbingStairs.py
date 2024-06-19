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