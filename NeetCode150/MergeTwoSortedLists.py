# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode() # dummy e um no ficticio

        while list1 and list2:
            if list1.val < list2.val: # list1.val acessa o valor do no atual na list1.
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
    
solution = Solution()

# Teste 1
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(5)))
merged_list = solution.mergeTwoLists(list1, list2)
print([merged_list.val, merged_list.next.val, merged_list.next.next.val, merged_list.next.next.next.val, merged_list.next.next.next.next.val, merged_list.next.next.next.next.next.val])  # Output: [1, 1, 2, 3, 4, 5]

# Teste 2
list1 = None
list2 = ListNode(1, ListNode(2))
merged_list = solution.mergeTwoLists(list1, list2)
print([merged_list.val, merged_list.next.val])  # Output: [1, 2]

# Teste 3
list1 = None
list2 = None
merged_list = solution.mergeTwoLists(list1, list2)
print([] if not merged_list else [merged_list.val])  # Output: []