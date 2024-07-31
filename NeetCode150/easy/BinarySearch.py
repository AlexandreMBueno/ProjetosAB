# comecamos com dois ponteiros left e right
# mid e definido pela distancia entre L e R / 2
# itera enquanto left <= right 
# e a cada iteracao, calcula mid ate achar mid = target
# se nao encontra, retorna -1

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target in nums:
        #     return nums.index(4) # f. index retorna indice
        # else:
        #     return -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2 # distancia entre LR = mid
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1 # caso n encontre target

solution = Solution()

# teste 1
nums1 = [-1, 0, 2, 4, 6, 8]
target1 = 4
output1 = solution.search(nums1, target1)
print(f"Input: nums = {nums1}, target = {target1}\nOutput: {output1}")

# teste 2
nums2 = [-1, 0, 2, 4, 6, 8]
target2 = 3
output2 = solution.search(nums2, target2)
print(f"Input: nums = {nums2}, target = {target2}\nOutput: {output2}")
