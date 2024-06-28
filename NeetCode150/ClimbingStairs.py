# 1 1 1
# 1 2
# 2 1

# o número de maneiras de chegar ao degrau n é:
# a soma do número de maneiras de chegar ao degrau n-1 e ao degrau n-2.

# f(n) = f(n - 1) + f(n - 2) FIBONACCI

# -------------------------------------------------------

# MANEIRA 1 DE RESOLVER:

class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        nesse caso, a maneira de andar os n degraus segue fibonacci, ou seja
        f(n) = f(n - 1) + f(n -2)
        entao a maneira de subir os n degraus eh a soma de
        maneiras de chegar ao degrau n - 1
         +
        maneiras de chegar ao degrau n - 2
        '''

        if n == 0 or n == 1:
            return 1
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)  

print("First Test:")
solution= Solution()
n = 3
result = solution.climbStairs(n)
print(f"Input: n = {n}\nOutput: {result}")

# -------------------------------------------------------

# MANEIRA 2 DE RESOLVER:

class Solution2:
    def climbStairs2(self, n: int) -> int:
        one, two = 1, 1

        for x in range(n -1):
            temp = one
            one = one + two
            two = temp
        return one
    
print("-" * 20)
print("Second Test:")
solution2= Solution2()
n = 5
result = solution2.climbStairs2(n)
print(f"Input: n = {n}\nOutput: {result}")