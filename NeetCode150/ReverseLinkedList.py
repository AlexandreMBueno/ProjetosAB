# nesse codigo usamos ponteiros e nos
# [ ] -> [ ] -> [ ] -> [ ] -> [ ] e temos q inverter esses ponteiros
# comecamos com anterior None e a cabeca do no como atual

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        anterior, atual = None, head

        while atual:  # Enquanto atual nao for None (não chegamos ao final da lista)
            proximo = atual.next  # armazena o próximo no
            atual.next = anterior  # Inverte o ponteiro: o próximo do nó atual passa a ser o no anterior
            anterior = atual  # move o ponteiro anterior para o no atual
            atual = proximo  # move o ponteiro atual para o proximo no (salvo anteriormente)
        
        return anterior  # anterior agora e a nova cabeça(head) da lista invertida


# testes mais chatos por ser nos mas deu boa

solution = Solution()

# teste 1
head1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3)))) # nos 
teste1 = solution.reverseList(head1)
print("Teste 1 - Output:", end=" ") # so p ficar bnt na hr de printar
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