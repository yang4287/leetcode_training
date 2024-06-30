# https://leetcode.com/problems/linked-list-cycle/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 利用快慢走，持早會走到相同節點
        # 排除none情況
        if head is None:
            return False
        # 只有一個節點不是循環
        if head.next is None:
            return False

        slow_ptr = head
        fast_ptr = head
        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                return True
        return False
