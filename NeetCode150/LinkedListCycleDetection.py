# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # comecar definindo 2 ponteiros, slow e fast
        # ambos na mesma posicao,slow +=1, fast +=2
        # sempre vao se encontrar independentemente do tamanho
        # explicacao com anexo no trello
        slow, fast = head, head

        while fast and fast.next: #enquanto proximo nao for null
            slow = slow.next # aponta p proximo
            fast = fast.next.next # aponta p proximo, do proximo
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