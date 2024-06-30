# leetcode URL：https://leetcode.com/problems/palindrome-linked-list/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 1->2->2->1
        # 利用慢快，慢的會卡在中間之後
        # slow = 2->1   fast = None
        # 再把slow reverse => 1->2
        # 再找中間之前的資料，也就是 1->2
        # 進行比較

        if head is None or head.next is None:
            return True

        fast = head
        slow = head
        prev = None
        # 找中間之後=>找slow
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # 找 中間之前
        curr = head
        while curr is not None:
            if curr.next == slow:
                break
            curr = curr.next
        curr.next = None
        # head => 1->2

        # reverse slow
        prev = None
        curr = slow
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # 檢查每個節點值是否一樣
        while head is not None and prev is not None:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
