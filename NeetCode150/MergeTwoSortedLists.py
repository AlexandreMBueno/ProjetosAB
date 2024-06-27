# Definition for singly-linked list.
from typing  import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        dummy = node = listNode() ->
        criamos uma lista listNode() q tanto o no dummy qnt no node apontam 
        p inicio dela
        dummy e um node fake dentro de listNOde()
        node.next aponta para esse node fake gummy p facilitar o codigo
        node.next ent significa o primeiro node de listNode(), ou seja, dummy
        criamos um loop enquanto as listas existem
        if
        list1.val ou seja, primeiro valor da list 1 
        <
        list2.val ou seja, primeiro valor da list 2
        adicionamos o primeiro no de list1 a listNode() com node.next q aponta p dummy fake
        e atualizamos o valor de list1 p list1.next, ou seja proximo no de list1
        caso list1.val nao seja menor que list2.val
        adicionamos o primeiro no de list2 a listNode() tambem com node.next = list2
        e atualizamos o valor do de list2 - list2.next, ou seja proximo no de list2
        depois de sair do loop, caso tenha sobrado algum node em alguma das listas
        nos adicionamos eles na listNode()
        node = node.next serve p dps de adicioanr um novo no a listNode()
        nos movemos o ponteiro node para esse no q adicionamos agora
        ou seja, agora node aponta p final da nova lista
        pronto pa dd o proximo no no proximo loop
        ao final, retornamos dummy.next ou seja, p quem o nosso no fake aponta
        q e o primeiro node de listNode()
        '''

        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
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