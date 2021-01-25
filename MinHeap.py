​class MinHeap:

    def __init__(self, arr):
        self.heap = self.buildHeap(arr)

    def buildHeap(self, arr):
        firstParentIdx = (len(arr) - 2) // 2
        for currIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currIdx, len(arr) - 1, arr)
        return arr

    def siftDown(self, currIdx, endIdx, heap):
        childOneIdx = currIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currIdx * 2 + 2 if currIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] < heap[currIdx]:
                self.swap(currIdx, idxToSwap, heap)
                currIdx = idxToSwap
                childOneIdx = currIdx * 2 + 1
            else:
                return

    def siftUp(self, currIdx, heap):
        parentIdx = (currIdx - 1) // 2
        while currIdx > 0 and heap[currIdx] < heap[parentIdx]:
            self.swap(currIdx, parentIdx, heap)
            currIdx = parentIdx
            parentIdx = (currIdx - 1) // 2

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def peek(self):
        return self.heap[0]

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
