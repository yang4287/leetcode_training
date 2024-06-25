# leetcode URL：https://leetcode.com/problems/balanced-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travel(self, node: TreeNode):
        if node is None:
            return 0
        left_depth = self.travel(node.left)
        right_depth = self.travel(node.right)

        # 計算從當前節點通過左子樹和右子樹的深度相減，<=1 是平衡，大於是不平衡
        self.sub = max(self.sub, abs(left_depth - right_depth))

        # 返回從當前節點到最深的子樹的深度
        return max(left_depth, right_depth) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.sub = 0
        self.travel(root)
        return self.sub <= 1
