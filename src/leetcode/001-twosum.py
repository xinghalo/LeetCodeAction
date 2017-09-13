class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(length):
            for j in range(length-1,i,-1):
                if nums[i]+nums[j] == target:
                    return [i,j]

solution = Solution()
print solution.twoSum([3,2,4],6)
