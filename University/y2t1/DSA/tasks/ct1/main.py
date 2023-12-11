from customtkinter import *
from Heap import *


class AlertPopup(CTkToplevel):
    def __init__(self, message: str):
        super().__init__()
        self.resizable(False, False)

        label = CTkLabel(master=self, text=message)
        label.pack(padx=10, pady=10, anchor="center")

        button = CTkButton(master=self, text="Close", command=self.close_dialog)
        button.pack(padx=10, pady=10, anchor="center")

        self.grab_set()
        self.lift()
        self.bind("<Escape>", self.close_dialog)

    def close_dialog(self, event=None):
        self.destroy()


app = CTk()
app.title("Data Structures and Algorithms")
app.geometry("700x400")
app.resizable(False, False)

tabsContainer = CTkTabview(app)
tabsContainer.pack(expand=1, fill="both")

tabsContainer.add("Heap")
tabsContainer.add("Data Structures")
tabsContainer.add("Greedy Algorithms")
tabsContainer.add("Dynamic Programming")
tabsContainer.add("Graph Traversal")
tabsContainer.add("Graph Shortest Path")

heapTab = tabsContainer.tab("Heap")
dataStructuresTab = tabsContainer.tab("Data Structures")
greedyAlgosTab = tabsContainer.tab("Greedy Algorithms")
dynamicProgrammingTab = tabsContainer.tab("Dynamic Programming")
graphTraversalTab = tabsContainer.tab("Graph Traversal")
graphShortestPathTab = tabsContainer.tab("Graph Shortest Path")


# ! HEAP
# TODO add files for storing elements
# TODO time the time it takes to sort and output - for each sorting
class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapifyUp(index=len(self.heap) - 1)

    def delete(self):
        if len(self.heap) == 0:
            return None
        self._swap(0, len(self.heap) - 1)
        root = self.heap.pop()
        self._heapifyDown(index=0)
        return root

    def sort(self):
        sortedItems = []
        for _ in range(len(self.heap)):
            sortedItems.append(self.delete())
        return sortedItems

    def buildHeap(self, arr):
        self.heap = arr
        start = len(arr) // 2
        for i in reversed(range(start + 1)):
            self._heapifyDown(index=i)
        return self

    def _heapifyUp(self, index):
        parentIndex = (index - 1) // 2
        if parentIndex >= 0 and self.heap[index] > self.heap[parentIndex]:
            self._swap(parentIndex, index)
            self._heapifyUp(index=parentIndex)

    def _heapifyDown(self, index):
        leftChildIndex = 2 * index + 1
        rightChildIndex = 2 * index + 2
        largest = index

        if (
            leftChildIndex < len(self.heap)
            and self.heap[leftChildIndex] > self.heap[largest]
        ):
            largest = leftChildIndex

        if (
            rightChildIndex < len(self.heap)
            and self.heap[rightChildIndex] > self.heap[largest]
        ):
            largest = rightChildIndex

        if largest != index:
            self._swap(index, largest)
            self._heapifyDown(index=largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def updateHeapElementsContainer():
    for widget in heapElementsContainer.winfo_children():
        widget.destroy()

    for _, element in enumerate(heapElements.heap):
        currentLabel = CTkLabel(heapElementsContainer, text=element)
        currentLabel.pack(padx=5, anchor="w")


def addHeapElement(element):
    heapElements.insert(value=element)
    updateHeapElementsContainer()


def deleteHeapElement():
    heapElements.delete()
    updateHeapElementsContainer()


def sortHeap_HeapSort():
    if len(heapElements.heap) == 0:
        return

    heapElements.heap = heapElements.sort()
    updateHeapElementsContainer()


def sortHeap_QuickSort():
    if len(heapElements.heap) == 0:
        return

    heapElements.heap = _quickSortUtil(heapElements.heap)
    updateHeapElementsContainer()


def _quickSortUtil(arr):
    n = len(arr)
    if n < 2:
        return arr

    pivot = arr[n // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    more = [x for x in arr if x > pivot]

    return _quickSortUtil(more) + equal + _quickSortUtil(less)


def sortHeap_DefaultSort():
    if len(heapElements.heap) == 0:
        return

    heapElements.heap = sorted(heapElements.heap, reverse=True)
    updateHeapElementsContainer()


heapElements = Heap()
heapElementsContainer = CTkScrollableFrame(heapTab, width=200, height=300)
heapSortingButtonsContainer = CTkFrame(heapTab, fg_color="transparent", width=300)
addHeapElementHeading = CTkLabel(
    heapTab, text="Add Heap Element", font=("Arial", 14, "bold")
)
heapElementsHeading = CTkLabel(
    heapTab, text="Heap Elements", font=("Arial", 14, "bold")
)
addHeapElementInput = CTkEntry(heapTab, placeholder_text="Enter element...", width=350)
addHeapElementButton = CTkButton(
    heapTab,
    text="Add",
    command=lambda: addHeapElement(int(addHeapElementInput.get())),
    width=60,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
)
deleteHeapElementButton = CTkButton(
    heapTab,
    text="Delete Element",
    command=lambda: deleteHeapElement(),
    width=120,
    fg_color="#BF181D",
    hover_color="#961316",
    text_color="white",
    font=("Arial", 12, "bold"),
)
sortHeap_DefaultSortButton = CTkButton(
    heapSortingButtonsContainer,
    text="Default Sort",
    command=lambda: sortHeap_DefaultSort(),
    width=60,
)
sortHeap_QuickSortButton = CTkButton(
    heapSortingButtonsContainer,
    text="Quick Sort",
    command=lambda: sortHeap_QuickSort(),
    width=60,
)
sortHeap_HeapSortButton = CTkButton(
    heapSortingButtonsContainer,
    text="Heap Sort",
    command=lambda: sortHeap_HeapSort(),
    width=60,
)

addHeapElementHeading.place(x=5, y=5)
addHeapElementInput.place(x=5, y=35)
addHeapElementButton.place(x=360, y=35)
deleteHeapElementButton.place(x=300, y=80)
heapSortingButtonsContainer.place(x=0, y=80)
sortHeap_DefaultSortButton.pack(padx=5, side="left")
sortHeap_QuickSortButton.pack(padx=5, side="left")
sortHeap_HeapSortButton.pack(padx=5, side="left")
heapElementsHeading.place(x=440, y=5)
heapElementsContainer.place(x=440, y=35)

app.mainloop()
