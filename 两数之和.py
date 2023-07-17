
# https://leetcode.cn/problems/two-sum/
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for o in range(0,len(nums)):
                if i == o:
                    continue
                ret = nums[i] + nums[o]
                if ret == target:
                    return i,o
nums = [2,7,11,15]
target = 9
result = Solution().twoSum(nums=nums,target=target)
print(result)

1
