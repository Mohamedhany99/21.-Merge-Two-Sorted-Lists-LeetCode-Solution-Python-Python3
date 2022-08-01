# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def counter(self, node):
      count = 0
      while node:
         count +=1
         node=node.next
      return count

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        head=list1
        if list1.val>list2.val:
            head=list2
            list2=list2.next
        else:
            list1=list1.next
        
        current = head
        
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1==None:
            current.next = list2
        else:
            current.next = list1
        return head        