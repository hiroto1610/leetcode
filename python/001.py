class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            other = target - num  # 「あといくつあればtargetになるか？」

            if other in seen:
                return [seen[other], i]  # 答えが見つかった！

            seen[num] = i 