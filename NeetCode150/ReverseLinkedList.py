# nesse codigo usamos ponteiros e nos
# [ ] -> [ ] -> [ ] -> [ ] -> [ ] e temos q inverter esses ponteiros
# comecamos com anterior None e a cabeca do no como atual

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        comecamos criando 2 ponteiros, anterior e atual
        loop enquanto o q atual nao for null
            proximo no vai ser o atual.next ->
            o proximo do atual vai ser o anterior
            o anterior tera q ser o atual
            e o atual o proximo
        retornamos o anterior
        '''

        anterior, atual = None, head

        while atual: 
            proximo = atual.next
            atual.next = anterior
            anterior = atual
            atual = proximo
        return anterior


# testes

solution = Solution()

# teste 1
head1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3)))) # nos 
teste1 = solution.reverseList(head1)
print("Teste 1 - Output:", end=" ")
while teste1:
    print(teste1.val, end=" ")
    teste1 = teste1.next

# teste 2
head2 = None # sem nos
teste2 = solution.reverseList(head2)
print("\nTeste 2 - Output:", end=" ")
if not teste2:
    print("[]")
else:
    while teste2:
        print(teste2.val, end=" ")
        teste2 = teste2.next