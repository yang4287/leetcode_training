# https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 解法1: time:O(n)  space:O(n)
        # hashmap，set是hashmap一種，檢查key在不在只要O(1)，用list會需要O(n)
        exits = set()
        for n in nums:
            if n not in exits:
                exits.add(n)
            else:
                return True
        return False

        # 解法2：time:O(n logn)  space:O(1)
        # nums.sort()
        # left = 0
        # right = 1
        # while right < len(nums):
        #     if (nums[left] == nums[right]):
        #         return True
        #     left += 1
        #     right += 1
        # return False
