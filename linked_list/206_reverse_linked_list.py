# leetcode URL；https://leetcode.com/problems/reverse-linked-list/description/
#
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


sentinel = pointer = ListNode()
for i in range(5):
    pointer.next = ListNode(i)
    pointer = pointer.next

head = sentinel.next
curren_node = head
while curren_node is not None:
    print(curren_node.val)
    curren_node = curren_node.next


reversed_linkedlist = Solution().reverseList(head)
curren_node = reversed_linkedlist
while curren_node is not None:
    print(curren_node.val)
    curren_node = curren_node.next
# [0] -> [1] -> [2] -> [3] -> [4]

# Run 1 :
# current_node = [0]
# current_node.next = prev => [0] -> None
# prev = current_node => prev = [0] -> None
# current_node = [1]->.....

# Run 2 :
# current_node = [1]
# current_node.next = prev => [1] -> [0] -> None
# prev = current_node => prev = [1] -> [0] -> None


# reverse
