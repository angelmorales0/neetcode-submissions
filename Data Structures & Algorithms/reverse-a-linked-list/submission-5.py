#class ListNode():
 #   def __init__(self, val=0, next=None):
  #      self.next = None
   #     self.val= val


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = None
        temp = head
        while head:
            temp = head.next
            head.next = dummy
            dummy = head
            head = temp
        return dummy

