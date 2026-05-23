# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1= []
        stack2= []
        stack3 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        str1 = ""
        str2 = ""
        while stack1 or stack2:
            if stack1:
                str1 = str1 + str (stack1.pop())
            if stack2:
                str2 = str2 + str (stack2.pop())
        add= int(str1) + int(str2)
        str_add= str(add)
        for num in str_add:
            stack3.append(num)

        print(stack3)

        head = ListNode(int(stack3.pop()))
        node = head
        while stack3:
            to_add = ListNode(int(stack3.pop()))
            node.next = to_add
            node = node.next
        return head
