# leetcode URL；https://leetcode.com/problems/reverse-linked-list/description/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 記得前面
        prev_node = None
        current_node = head
        while current_node is not None:
            # 先把原先後面的存起來 (避面等等重新指向時遺失)
            next_node = current_node.next

            # 將 head 反方向指，也就是記住的prev
            current_node.next = prev_node

            # 記住 prev_node 指向 head ，此current_node資料，提供下一次 current_node.next指反方向指向
            prev_node = current_node

            # 繼續跑下一個
            current_node = next_node
        return prev_node
