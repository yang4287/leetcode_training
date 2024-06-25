# leetcode URL：https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travel(self, node):
        if node is None:
            return 0

        left_depth = self.travel(node.left)
        right_depth = self.travel(node.right)

        # 計算從當前節點通過左子樹和右子樹達到的最大深度
        self.diameter = max(self.diameter, left_depth + right_depth)

        # 返回從當前節點到最深的子樹的深度
        return max(left_depth, right_depth) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        self.diameter = 0
        self.travel(root)

        return self.diameter
