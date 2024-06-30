# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        利用hashmap，記住該數字的索引
        [2,7,11,15]  => {2:0, 7:1, 11:2, 15:3}
        [3,3] => {3:1}

        """
        hash_map = {}
        for index in range(len(nums)):
            another_num = target - nums[index]
            if another_num in hash_map:
                return [hash_map[another_num], index]
            # 加進去map
            hash_map[nums[index]] = index
