def _swap(self, i, j):
    # Get the values at indices i and j in the heap list
    value_i = self.heap[i]
    value_j = self.heap[j]

    # Swap the values at indices i and j in the heap list
    self.heap[i] = value_j
    self.heap[j] = value_i
