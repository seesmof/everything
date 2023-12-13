from customtkinter import *
import time
import json


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


def showSortingTimeAlert(sortingTime: str):
    AlertPopup(
        f"Sorting took {sortingTime:.2f} seconds or {sortingTime*1000:.2f} milliseconds"
    )


def _quickSortUtil(arr):
    n = len(arr)
    if n < 2:
        return arr

    pivot = arr[n // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    more = [x for x in arr if x > pivot]

    return _quickSortUtil(more) + equal + _quickSortUtil(less)


def sortHeap_HeapSort():
    if len(heapElements.heap) == 0:
        return

    startTimer = time.time()
    heapElements.heap = heapElements.sort()
    time.sleep(0.1)
    endTimer = time.time()
    sortingTime = endTimer - startTimer
    updateHeapElementsContainer()
    showSortingTimeAlert(sortingTime=sortingTime)


def sortHeap_QuickSort():
    if len(heapElements.heap) == 0:
        return

    startTimer = time.time()
    heapElements.heap = _quickSortUtil(heapElements.heap)
    time.sleep(0.1)
    endTimer = time.time()
    sortingTime = endTimer - startTimer
    updateHeapElementsContainer()
    showSortingTimeAlert(sortingTime=sortingTime)


def sortHeap_DefaultSort():
    if len(heapElements.heap) == 0:
        return

    startTimer = time.time()
    heapElements.heap = sorted(heapElements.heap, reverse=True)
    time.sleep(0.1)
    endTimer = time.time()
    sortingTime = endTimer - startTimer
    updateHeapElementsContainer()
    showSortingTimeAlert(sortingTime=sortingTime)


def saveHeapOnExit():
    if len(heapElements.heap) == 0:
        return
    with open("heap.json", "w") as file:
        json.dump(heapElements.heap, file)


def loadHeapOnStart():
    try:
        with open("heap.json", "r") as file:
            heapArray = json.load(file)
            heapElements.buildHeap(arr=heapArray)
            updateHeapElementsContainer()
    except FileNotFoundError:
        pass


heapOutputBoxesContainer = CTkTabview(heapTab, width=210, height=290)
heapOutputBoxesContainer.add("Heap")
heapOutputBoxesContainer.add("Linked List")
heapOutputBoxesContainer.add("Task")
heapOutputBoxesContainer.place(x=430, y=5)

heapElementsTab = heapOutputBoxesContainer.tab("Heap")
linkedListElementsTab = heapOutputBoxesContainer.tab("Linked List")
heapTaskElementsTab = heapOutputBoxesContainer.tab("Task")

heapElementsContainer = CTkScrollableFrame(heapElementsTab, width=210, height=260)
heapElementsContainer.pack(padx=5, pady=5, fill="both", expand=True)

linkedListElementsContainer = CTkScrollableFrame(
    linkedListElementsTab, width=210, height=260
)
linkedListElementsContainer.pack(padx=5, pady=5, fill="both", expand=True)

heapTaskElementsContainer = CTkScrollableFrame(
    heapTaskElementsTab, width=210, height=260
)
heapTaskElementsContainer.pack(padx=5, pady=5, fill="both", expand=True)


addHeapElementHeading = CTkLabel(
    heapTab, text="Add to Heap", font=("Arial", 14, "bold")
)
addHeapElementHeading.place(x=5, y=5)

addHeapElementInput = CTkEntry(heapTab, placeholder_text="Enter element...", width=350)
addHeapElementInput.place(x=5, y=35)

addHeapElementButton = CTkButton(
    heapTab,
    text="Add",
    command=lambda: addHeapElement(int(addHeapElementInput.get()))
    if addHeapElementInput.get()
    else AlertPopup("Input box is empty"),
    width=60,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
)
addHeapElementButton.place(x=360, y=35)

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
deleteHeapElementButton.place(x=300, y=80)

heapSortingButtonsContainer = CTkFrame(heapTab, fg_color="transparent", width=300)
heapSortingButtonsContainer.place(x=0, y=80)

sortHeap_DefaultSortButton = CTkButton(
    heapSortingButtonsContainer,
    text="Default Sort",
    command=lambda: sortHeap_DefaultSort(),
    width=60,
)
sortHeap_DefaultSortButton.pack(padx=5, side="left")

sortHeap_QuickSortButton = CTkButton(
    heapSortingButtonsContainer,
    text="Quick Sort",
    command=lambda: sortHeap_QuickSort(),
    width=60,
)
sortHeap_QuickSortButton.pack(padx=5, side="left")

sortHeap_HeapSortButton = CTkButton(
    heapSortingButtonsContainer,
    text="Heap Sort",
    command=lambda: sortHeap_HeapSort(),
    width=60,
)
sortHeap_HeapSortButton.pack(padx=5, side="left")

heapElements = Heap()
loadHeapOnStart()


# ! DOUBLY LINKED LIST
class DoublyLinkedList:
    class LinkedListNode:
        def __init__(self, data=None):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = self.LinkedListNode(data)
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            newNode = self.LinkedListNode(data)
            currentNode.next = newNode
            newNode.prev = currentNode

    def search(self, data) -> bool:
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == data:
                return True
            currentNode = currentNode.next
        return False

    def delete(self, data) -> bool:
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == data:
                if currentNode.prev is not None:
                    currentNode.prev.next = currentNode.next
                if currentNode.next is not None:
                    currentNode.next.prev = currentNode.prev
                if currentNode == self.head:
                    self.head = currentNode.next
                return True
            currentNode = currentNode.next
        return False

    def getList(self):
        list = []
        currentNode = self.head
        while currentNode is not None:
            list.append(currentNode.data)
            currentNode = currentNode.next
        return list

    def buildList(self, list):
        for element in list:
            self.append(element)


def updateLinkedListElementsContainer():
    for widget in linkedListElementsContainer.winfo_children():
        widget.destroy()

    for _, element in enumerate(linkedListElements.getList()):
        currentLabel = CTkLabel(linkedListElementsContainer, text=element)
        currentLabel.pack(padx=5, anchor="w")


def addLinkedListNode(data):
    if linkedListElements.search(data):
        AlertPopup(f"{data} already exists in linked list")
        return

    linkedListElements.append(data)
    updateLinkedListElementsContainer()


def deleteLinkedListNode(data):
    if not linkedListElements.delete(data):
        AlertPopup(f"{data} is NOT found in a list")
        return

    updateLinkedListElementsContainer()


def searchLinkedListNode(data):
    if linkedListElements.search(data):
        AlertPopup(f"{data} is found in a list")
    else:
        AlertPopup(f"{data} is NOT found in a list")


def saveLinkedListOnExit():
    if len(linkedListElements.getList()) == 0:
        return
    with open("linkedList.json", "w") as f:
        json.dump(linkedListElements.getList(), f)


def loadLinkedListOnStart():
    try:
        with open("linkedList.json", "r") as f:
            list = json.load(f)
            linkedListElements.buildList(list)
            updateLinkedListElementsContainer()
    except FileNotFoundError:
        pass


addLinkedListNodeHeading = CTkLabel(
    heapTab, text="Add Node", font=("Arial", 14, "bold")
)
addLinkedListNodeHeading.place(x=5, y=130)

addLinkedListNodeInput = CTkEntry(heapTab, placeholder_text="Node...", width=75)
addLinkedListNodeInput.place(x=5, y=160)

addLinkedListNodeButton = CTkButton(
    heapTab,
    text="Add",
    command=lambda: addLinkedListNode(int(addLinkedListNodeInput.get()))
    if addLinkedListNodeInput.get()
    else AlertPopup("Input box is empty"),
    width=45,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
)
addLinkedListNodeButton.place(x=85, y=160)

deleteHeapNodeHeading = CTkLabel(
    heapTab, text="Delete Node", font=("Arial", 14, "bold")
)
deleteHeapNodeHeading.place(x=145, y=130)

deleteLinkedListNodeInput = CTkEntry(heapTab, placeholder_text="Node...", width=75)
deleteLinkedListNodeInput.place(x=145, y=160)

deleteLinkedListNodeButton = CTkButton(
    heapTab,
    text="Delete",
    command=lambda: deleteLinkedListNode(int(deleteLinkedListNodeInput.get()))
    if deleteLinkedListNodeInput.get()
    else AlertPopup("Input box is empty"),
    width=45,
    fg_color="#D32F2F",
    hover_color="#B71C1C",
    text_color="white",
    font=("Arial", 12, "bold"),
)
deleteLinkedListNodeButton.place(x=225, y=160)

searchLinkedListNodeHeading = CTkLabel(
    heapTab, text="Search Node", font=("Arial", 14, "bold")
)
searchLinkedListNodeHeading.place(x=290, y=130)

searchLinkedListNodeInput = CTkEntry(heapTab, placeholder_text="Node...", width=75)
searchLinkedListNodeInput.place(x=290, y=160)

searchLinkedListNodeButton = CTkButton(
    heapTab,
    text="Search",
    command=lambda: searchLinkedListNode(int(searchLinkedListNodeInput.get()))
    if searchLinkedListNodeInput.get()
    else AlertPopup("Input box is empty"),
    width=45,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
)
searchLinkedListNodeButton.place(x=370, y=160)

linkedListElements = DoublyLinkedList()
loadLinkedListOnStart()


# ! HEAP TASK - EMPLOYEES
def updateHeapTaskElementsContainer():
    for widget in heapTaskElementsContainer.winfo_children():
        widget.destroy()

    for employee in heapTaskEmployeesData:
        employeeText = f"{employee['name']} - {employee['disease']}"
        currentLabel = CTkLabel(heapTaskElementsContainer, text=employeeText)
        currentLabel.pack(padx=5, anchor="w")


def heapTaskLoadEmployeesData(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    try:
        global heapTaskEmployeesData
        heapTaskEmployeesData = data["employees"]
    except:
        AlertPopup(f"Failed to load data from {filename}")

    updateHeapTaskElementsContainer()


def heapTaskShowResults():
    def countDiseaseCases():
        diseasesCount = dict()

        for employee in heapTaskEmployeesData:
            if employee["disease"] not in diseasesCount:
                diseasesCount[employee["disease"]] = 1
            else:
                diseasesCount[employee["disease"]] += 1

        return diseasesCount

    def sortDiseasesList(arr):
        if len(arr) == 0:
            return arr

        sortedArr = Heap().buildHeap(arr).sort()
        return sortedArr

    diseasesCount = countDiseaseCases()
    diseasesCountList = [
        (occurences, name) for name, occurences in diseasesCount.items()
    ]

    diseasesCountList = sortDiseasesList(diseasesCountList)
    resultsString = f"Employees' Diseases sorted by Occurences:\n"
    for occurence, name in diseasesCountList:
        currentDisease = f"{name}: {occurence} times\n"
        resultsString += currentDisease
    AlertPopup(resultsString)


heapTaskLoadEmployeesDataHeading = CTkLabel(
    heapTab, text="Load employees JSON file", font=("Arial", 14, "bold")
)
heapTaskLoadEmployeesDataHeading.place(x=5, y=210)

heapTaskLoadEmployeesDataInput = CTkEntry(
    heapTab, placeholder_text="Filename...", width=140
)
heapTaskLoadEmployeesDataInput.place(x=5, y=240)

heapTaskLoadEmployeesDataButton = CTkButton(
    heapTab,
    text="Load",
    width=60,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: heapTaskLoadEmployeesData(heapTaskLoadEmployeesDataInput.get())
    if heapTaskLoadEmployeesDataInput.get()
    else AlertPopup("Input box is empty"),
)
heapTaskLoadEmployeesDataButton.place(x=150, y=240)

heapTaskShowResultsButton = CTkButton(
    heapTab,
    text="Show Results",
    width=120,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: heapTaskShowResults(),
)
heapTaskShowResultsButton.place(x=220, y=240)

heapTaskEmployeesData = []


# ! HASH TABLE
class HashTable:
    def __init__(self, size=15):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key):
        return int((key * ((5**0.5 - 1) / 2) % 1) * self.size)

    def unhash(self, key):
        # TODO implement backwards hash function
        pass

    def insert(self, key, value):
        self.table[self.hash(key)].append((key, value))

    def delete(self, key):
        chain = self.table[self.hash(key)]
        for i, kv in enumerate(chain):
            if kv[0] == key:
                del chain[i]
                return True
        return False

    def search(self, key):
        chain = self.table[self.hash(key)]
        for kv in chain:
            if kv[0] == key:
                return kv[1]
        return None

    def getList(self):
        res = []
        for chain in self.table:
            if chain:
                for value in chain:
                    res.append(value)
        return res


def updateHashTableElementsContainer():
    for widget in hashTableElementsContainer.winfo_children():
        widget.destroy()

    for el in hashTableElements.getList():
        elementText = f"{el[0]} - {el[1]}"
        currentLabel = CTkLabel(hashTableElementsContainer, text=elementText)
        currentLabel.pack(padx=5, anchor="w")


def addHashTableElement(keyValuePair):
    key, value = keyValuePair.split(" ")
    # TODO check if key contains letters, if so only then convert to this sum of values else write like that
    key = sum(ord(c) for c in key)

    hashTableElements.insert(key, value)
    updateHashTableElementsContainer()


hashOutputBoxesContainer = CTkTabview(dataStructuresTab, width=210, height=290)
hashOutputBoxesContainer.add("Hash Table")
hashOutputBoxesContainer.add("B-Tree")
hashOutputBoxesContainer.add("Task A")
hashOutputBoxesContainer.add("Task B")
hashOutputBoxesContainer.place(x=430, y=5)

hashTableElementsTab = hashOutputBoxesContainer.tab("Hash Table")
bTreeElementsTab = hashOutputBoxesContainer.tab("B-Tree")
hashTaskElementsTab = hashOutputBoxesContainer.tab("Task A")
bTreeTaskElementsTab = hashOutputBoxesContainer.tab("Task B")

hashTableElementsContainer = CTkScrollableFrame(
    hashTableElementsTab, width=210, height=260
)
hashTableElementsContainer.pack(padx=5, pady=5, fill="both", expand=True)

bTreeElementsContainer = CTkScrollableFrame(bTreeElementsTab, width=210, height=260)
bTreeElementsContainer.pack(padx=5, pady=5, fill="both", expand=True)

hashTaskElementsContainer = CTkScrollableFrame(
    hashTaskElementsTab, width=210, height=260
)
hashTaskElementsContainer.pack(padx=5, pady=5, fill="both", expand=True)

bTreeTaskElementsContainer = CTkScrollableFrame(
    bTreeTaskElementsTab, width=210, height=260
)
bTreeTaskElementsContainer.pack(padx=5, pady=5, fill="both", expand=True)


addHashTableElementHeading = CTkLabel(
    dataStructuresTab, text="Add Dictionary Element", font=("Arial", 14, "bold")
)
addHashTableElementHeading.place(x=5, y=5)

addHashTableElementInput = CTkEntry(
    dataStructuresTab, placeholder_text="Key & Value...", width=110
)
addHashTableElementInput.place(x=5, y=35)

addHashTableElementButton = CTkButton(
    dataStructuresTab,
    text="Add",
    width=45,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: addHashTableElement(addHashTableElementInput.get())
    if addHashTableElementInput.get()
    else AlertPopup("Input box is empty"),
)
addHashTableElementButton.place(x=120, y=35)

deleteHashTableElementHeading = CTkLabel(
    dataStructuresTab, text="Delete Key", font=("Arial", 14, "bold")
)
deleteHashTableElementHeading.place(x=180, y=5)

deleteHashTableElementInput = CTkEntry(
    dataStructuresTab, placeholder_text="Key...", width=75
)
deleteHashTableElementInput.place(x=180, y=35)

deleteHashTableElementButton = CTkButton(
    dataStructuresTab,
    text="Delete",
    width=45,
    fg_color="#D32F2F",
    hover_color="#B71C1C",
    text_color="white",
    font=("Arial", 12, "bold"),
)
deleteHashTableElementButton.place(x=260, y=35)

searchHashTableElementHeading = CTkLabel(
    dataStructuresTab, text="Search Key", font=("Arial", 14, "bold")
)
searchHashTableElementHeading.place(x=320, y=5)

searchHashTableElementInput = CTkEntry(
    dataStructuresTab, placeholder_text="Key...", width=65
)
searchHashTableElementInput.place(x=320, y=35)

searchHashTableElementButton = CTkButton(
    dataStructuresTab,
    text="Run",
    width=40,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
)
searchHashTableElementButton.place(x=390, y=35)

hashTableElements = HashTable()

app.mainloop()
saveHeapOnExit()
saveLinkedListOnExit()
