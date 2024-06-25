# leetcode URL：https://leetcode.com/problems/symmetric-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compare(self, left: TreeNode, right: TreeNode) -> bool:
        """
        對稱樹：最左邊都要等於最右邊，所以一開始要分左邊跟右邊
        """
        if left is None and right is None:
            return True
        elif left is None and right is not None:
            return False
        elif left is not None and right is None:
            return False
        if left.val == right.val:
            return self.compare(left.left, right.right) and self.compare(
                left.right, right.left
            )
        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is not None and root.right is not None:
            return self.compare(root.left, root.right)
        elif root.left is None and root.right is None:
            return True
        else:
            return False
