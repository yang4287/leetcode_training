# leetcode URL：https://leetcode.com/problems/remove-linked-list-elements/description/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 虛擬的哨兵
        sentinel = ListNode(next=head)
        # 用來記住前面，同時透過指向變更sential
        prev = sentinel

        # 負責跑回圈
        curr = head

        while curr is not None:
            if curr.val == val:
                # 重新指向
                prev.next = curr.next
            else:
                # 不等於，就是要等於當前curr，供下次記住前面是啥
                prev = curr
            curr = curr.next

        return sentinel.next
