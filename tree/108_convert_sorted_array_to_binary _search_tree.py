# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNode(self, nums: List[int]):
        if (len(nums) == 1):
            return TreeNode(nums[0])
        mid_idx = int(len(nums)/2)
        if (len(nums) == 2):
             return TreeNode(nums[mid_idx],self.findNode(nums[:mid_idx]) )
        return TreeNode(nums[mid_idx],self.findNode(nums[:mid_idx]),self.findNode(nums[mid_idx+1:]) )


    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 找中間的位置作為節點分左右兩邊，以此類推
        # [-10,-3,0,5,9,11] ，找到 5 ，以5作為節點，分左邊為[-10,-3,0 ] 跟右邊為[9,11]
        # 再將[-10,-3,0 ] 找中間分左右和[9,11]找中間左右
        # 用遞迴
        return self.findNode(nums)

        