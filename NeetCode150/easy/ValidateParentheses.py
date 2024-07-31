# achei esse um pouco mais complexo que os outros e tive difiuldade de fazer
# funcionamento ->
# Cria uma pilha (uma estrutura de dados que segue o princípio LIFO - Last In, First Out)
# Define um dic (closeToOpen) que mapeia cada caractere de fechamento ao seu correspondente de abertura.
# O código percorre cada caractere na string de entrada.

# Para cada caractere:
#     Se for um caractere de abertura (, [, {:
#         Adiciona-o à pilha.
#     Se for um caractere de fechamento ), ], }:
#         Verifica se o caractere de abertura correspondente está no topo da pilha:
#             Se sim: Remove o caractere do topo da pilha (pois foi corretamente pareado).
#             Se não: Retorna False imediatamente, indicando que a string não está balanceada.

# ao final retorna True se a pilha estiver vazia, ou seja, tds os ({[]}) tiveram correspondencia
# se nao tiver vazia e pq algum nao teve correspondencia

#closeToOpen[c]

# Quando estamos iterando sobre a string s, a variável c representa o caractere atual.
# Se c for um caractere de fechamento
#(ou seja, c é uma chave no dicionário closeToOpen), closeToOpen[c] nos dá o caractere de abertura correspondente.

class Solution:
    def isValid(self, s: str) -> bool:
        '''
    comecamos criando uma pilha vazia (last in, first out (LIFO))
    dps, criamos um dic p armazenar chave valor os ({[]})
    cada um de fechamento(chave), com seu de abertura(valor)
    criamos ent um loop p cada (c)aracter na s(tring)
        se c estiver no dicionario
            e se pilha e pilha [-1] == dicionario[c]
                removemos ele com pilha.pop() pois verificado q tem compatibilidade
            caso nao
                retornamos false
        caso nao
            adiconamos c na pilha com append
    retornamos true se nao pilha (ou seja vazia) caso contrario false
        '''
        pilha = []
        closeToOpen = {"}": "{", ")": "(", "]": "["}

        for c in s:
            if c in closeToOpen:
                if pilha and pilha[-1] == closeToOpen[c]:
                    pilha.pop()
                else:
                    return False
            else:
                pilha.append(c)
        return True if not pilha else False


solution = Solution()

# teste 1
s1 = "[]"
output1 = solution.isValid(s1)
print(f"Input: {s1}\nOutput: {output1}\nExpected Output: True\n")

# teste 2
s2 = "([{}])"
output2 = solution.isValid(s2)
print(f"Input: {s2}\nOutput: {output2}\nExpected Output: True\n")

# teste 3
s3 = "[(])"
output3 = solution.isValid(s3)
print(f"Input: {s3}\nOutput: {output3}\nExpected Output: False\n")
