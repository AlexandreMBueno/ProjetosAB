import heapq
from typing  import  List

class KthLargest:
# fiz com ajuda do video
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

# teste
operations = ["KthLargest", "add", "add", "add", "add", "add"]
values = [[3, [1, 2, 3, 3]], [3], [5], [6], [7], [8]]

output = [None]
kthLargest = KthLargest(values[0][0], values[0][1])

for i in range(1, len(operations)):
    if operations[i] == "add":
        result = kthLargest.add(values[i][0])
        output.append(result)

print(output)  # Deve imprimir: [None, 3, 3, 3, 5, 6]
