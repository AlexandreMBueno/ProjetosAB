# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        comecaremos definindo 2 ponteiros
        slow e fast, +=1 +=2
        slow vai p proximo, ou seja, slow.next
        fast vai p proximo, do proximo, ou seja, fast.next.next
        isso significa q uma hr o fast vai chegar em slow se tiver ciclo
        p fzr isso, enquanto o proximo nao for null
        ficamos andando +=1 +=2
        se uma hora slow == fast
        retorna True q existe um ciclo
        se nao, retorna false pq acabaram os nodes e nao se encontraram
        '''

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


# Teste
# criacao manual da lista ligada com ciclo
head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)

head.next = second
second.next = third
third.next = fourth
fourth.next = second  # criacao do ciclo

# Executando o teste
solution = Solution()
print(solution.hasCycle(head))  # Output deve ser: True