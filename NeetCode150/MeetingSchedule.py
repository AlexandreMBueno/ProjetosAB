# nesse problema, comecamos ordenando a lista pelo horario de inicio das reunioes
# em  seguida, criamos um loop para tds os valores dentro do tamanho da lista ordenada
# para cada um deles, verificamos se o horario de termino de uma reuniao eh maior que o de inicio da proxima
# se sim, retornamos False pois a conflito
# se nao, retornamos True fora do loop, ou seja, dps de ter passado pelo por tds os horarios

from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start # = comeco da reuniao
        self.end = end # = final da reuniao

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i - 1].end > sorted_intervals[i].start:
                return False
        return True

# na linha 20, fato interessante que fiquei com duvida ->
# por que nao poderia ser:
#        if sorted_intervals[i].end > sorted_intervals[i + 1].start:
# a resposta foi que, assim, uma hr comparariamos com um valor que nao existe, i+1, ou seja, fora da lista
# assim, teriamos un erro: index out of range

# teste 1
# Teste
intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
solution = Solution()
print(solution.canAttendMeetings(intervals))  # Output: False