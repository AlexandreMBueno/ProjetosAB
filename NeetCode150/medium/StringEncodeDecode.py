'''
função encode:

Recebe uma lista de strings.
Converte a lista em uma unica string codificada.
Para cada string na lista:
Adiciona o comprimento da string.
Adiciona um delimitador #.
Adiciona a propria string.
Repeticao do processo para todas as strings na lista.
Resultado: uma string final contendo todas as strings originais codificadas juntas.
4#neet4#code4#love3#you
'''

'''
função decode:

Recebe a string codificada. (4#neet4#code4#love3#you)
Percorre a string codificada:
Identifica o comprimento de cada string atraves do numero antes do delimitador #.
Extrai a string correspondente.
Adiciona a string a lista de resultados.
Repeticao do processo ate que todas as strings originais sejam recuperadas.
Resultado: uma lista contendo todas as strings originais.
'''

# lembra do q victor me explicou ontem sobre expressoes regulares, de procurar um "padrao" em um texto por ex
# duvida, e se dentro das minhas strings, existisse, por acaso, um int seguido de um #? oq aconteceria?
#   -> Resposta, codigo funcionaria perfeitamente, pois quando encontra o primeiro delimitador#...
#      ...o codigo entende que os proximos 5 caracteres(ex: 5#) sao pertencentes a string, independentendo do que tem dentro delas
#      ... ate mesmo se fosse outro int seguido de um delimitador#

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j + 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

#teste 1
solution = Solution()

test_input = ["neet", "code", "love", "you"]
encoded = solution.encode(test_input)
decoded = solution.decode(encoded)

if decoded == test_input:
    print("sucesso!")
    print(test_input)
    print(encoded)
    print(decoded)
else:
    print(f"Erro")
