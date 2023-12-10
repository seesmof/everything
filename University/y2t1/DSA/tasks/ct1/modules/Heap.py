class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        # append element to our array
        self.heap.append(value)
        # heapify it in order to set in the correct place
        self._heapifyUp(len(self.heap) - 1)

    def sort(self):
        sortedItems = []
        size = len(self.heap)
        # for each element in the heap
        for _ in range(size):
            # append the largest element to the temporary array
            sortedItems.append(self.delete())
        return sortedItems

    def buildHeap(self, arr):
        # set our heap to be the given array
        self.heap = arr
        # start in the middle of it cause the other half are leaves - nodes without children
        start = len(arr) // 2
        # for each element from the start to the first element in reversed order
        for i in reversed(range(start + 1)):
            # heapify it down to set in the correct place
            self._heapifyDown(i)
        return self

    def delete(self):
        # if the heap is empty, return null
        if len(self.heap) == 0:
            return None
        # swap root with the last element
        self._swap(0, len(self.heap) - 1)
        # assign root to temporary veriable
        root = self.heap.pop()
        # heapify the new root, which previously was the last element, to set it in a correct position
        self._heapifyDown(0)
        # return the original root
        return root

    def display(self):
        for item in self.heap:
            print(item, end=" ")
        print()

    def _heapifyUp(self, index):
        parentIndex = (index - 1) // 2
        # checking if parent element exists and if our current element is larger than its parrent
        if parentIndex >= 0 and self.heap[index] > self.heap[parentIndex]:
            # then swapping those two and continuing the process for parent
            self._swap(parentIndex, index)
            self._heapifyUp(parentIndex)

    def _heapifyDown(self, index):
        leftChildIndex = 2 * index + 1
        rightChildIndex = 2 * index + 2
        largest = index

        # checking if left child exists and its more than our largest element, which is currently our current element
        if (
            leftChildIndex < len(self.heap)
            and self.heap[leftChildIndex] > self.heap[largest]
        ):
            # then reassigning largest element to left child
            largest = leftChildIndex

        # checking if right child exists and if its larger than the current largest element
        if (
            rightChildIndex < len(self.heap)
            and self.heap[rightChildIndex] > self.heap[largest]
        ):
            # then reassigning largest element to the right child
            largest = rightChildIndex

        # checking if our current element is not the largest one
        if largest != index:
            # if so, swapping them two
            self._swap(index, largest)
            # continuing the process for the current largest element
            self._heapifyDown(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def heapSort(arr):
    return Heap().buildHeap(arr).sort()
