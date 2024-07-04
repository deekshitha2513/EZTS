#heap
#Max heap

import heapq
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        heapq.heappush(self.heap, -key)

    def print_heap(self):
        print([-x for x in self.heap])


max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(15)
max_heap.insert(30)
max_heap.insert(40)


print("Max Heap:")
max_heap.print_heap()

# OUTPUT
Max Heap:
[40, 30, 15, 10, 20]