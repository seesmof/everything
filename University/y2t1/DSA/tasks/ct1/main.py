from customtkinter import *
import time
import json
import heapq
import os
import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

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


#! HEAP
# TODO perhaps add visualization of binary heap
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


def visualizeHeap():
    def getGraph():
        G = nx.DiGraph()
        for i in range(len(heapElements.heap)):
            if i != 0:
                parent = (i - 1) // 2
                G.add_edge(parent, i)
        return G

    def treeLayout(G):
        pos = {}
        width = max(nx.node_connected_component(G, node) for node in G.nodes())
        height = len(G.nodes() // width)
        for node in nx.topological_sort(G):
            x = node % width
            y = node // width
            pos[node] = (x, -y)
        return pos

    G = getGraph()
    pos = treeLayout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray")
    plt.show()


heapTabsContainer = CTkTabview(heapTab)
heapTabsContainer.add("Heap")
heapTabsContainer.add("Linked List")
heapTabsContainer.add("Task")
heapTabsContainer.pack(fill="both", expand=True)

heapDemoTab = heapTabsContainer.tab("Heap")
linkedListDemoTab = heapTabsContainer.tab("Linked List")
heapTaskTab = heapTabsContainer.tab("Task")

heapElementsContainer = CTkScrollableFrame(heapDemoTab, width=240, height=270)
heapElementsContainer.place(x=400, y=0)

linkedListElementsContainer = CTkScrollableFrame(
    linkedListDemoTab, width=240, height=270
)
linkedListElementsContainer.place(x=400, y=0)

heapTaskElementsContainer = CTkScrollableFrame(heapTaskTab, width=240, height=270)
heapTaskElementsContainer.place(x=400, y=0)


addHeapElementHeading = CTkLabel(
    heapDemoTab, text="Add to Heap", font=("Arial", 14, "bold")
)
addHeapElementHeading.place(x=0, y=0)

addHeapElementInput = CTkEntry(
    heapDemoTab, placeholder_text="Enter element...", width=300
)
addHeapElementInput.place(x=0, y=30)

addHeapElementButton = CTkButton(
    heapDemoTab,
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
addHeapElementButton.place(x=305, y=30)

sortHeapSectionHeading = CTkLabel(
    heapDemoTab, text="Sort Heap", font=("Arial", 14, "bold")
)
sortHeapSectionHeading.place(x=0, y=70)

sortHeap_DefaultSortButton = CTkButton(
    heapDemoTab,
    text="Default Sort",
    command=lambda: sortHeap_DefaultSort(),
    width=60,
)
sortHeap_DefaultSortButton.place(x=0, y=100)

sortHeap_QuickSortButton = CTkButton(
    heapDemoTab,
    text="Quick Sort",
    command=lambda: sortHeap_QuickSort(),
    width=60,
)
sortHeap_QuickSortButton.place(x=90, y=100)

sortHeap_HeapSortButton = CTkButton(
    heapDemoTab,
    text="Heap Sort",
    command=lambda: sortHeap_HeapSort(),
    width=60,
)
sortHeap_HeapSortButton.place(x=170, y=100)

deleteHeapElementHeading = CTkLabel(
    heapDemoTab, text="Delete from Heap", font=("Arial", 14, "bold")
)
deleteHeapElementHeading.place(x=0, y=140)

deleteHeapElementButton = CTkButton(
    heapDemoTab,
    text="Delete Element",
    command=lambda: deleteHeapElement(),
    width=120,
    fg_color="#BF181D",
    hover_color="#961316",
    text_color="white",
    font=("Arial", 12, "bold"),
)
deleteHeapElementButton.place(x=0, y=170)

visualizeHeapHeading = CTkLabel(
    heapDemoTab, text="Visualize Heap", font=("Arial", 14, "bold")
)
visualizeHeapHeading.place(x=0, y=210)

visualizeHeapButton = CTkButton(
    heapDemoTab,
    text="Visualize",
    width=120,
    command=lambda: visualizeHeap()
    if len(heapElements.heap) > 0
    else AlertPopup("Heap is empty"),
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
)
visualizeHeapButton.place(x=0, y=240)

heapElements = Heap()
loadHeapOnStart()


#! DOUBLY LINKED LIST
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
    except:
        AlertPopup("Failed to load Linked List data")


addLinkedListNodeHeading = CTkLabel(
    linkedListDemoTab, text="Add Node", font=("Arial", 14, "bold")
)
addLinkedListNodeHeading.place(x=5, y=130)

addLinkedListNodeInput = CTkEntry(
    linkedListDemoTab, placeholder_text="Node...", width=75
)
addLinkedListNodeInput.place(x=5, y=160)

addLinkedListNodeButton = CTkButton(
    linkedListDemoTab,
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
    linkedListDemoTab, text="Delete Node", font=("Arial", 14, "bold")
)
deleteHeapNodeHeading.place(x=145, y=130)

deleteLinkedListNodeInput = CTkEntry(
    linkedListDemoTab, placeholder_text="Node...", width=75
)
deleteLinkedListNodeInput.place(x=145, y=160)

deleteLinkedListNodeButton = CTkButton(
    linkedListDemoTab,
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
    linkedListDemoTab, text="Search Node", font=("Arial", 14, "bold")
)
searchLinkedListNodeHeading.place(x=290, y=130)

searchLinkedListNodeInput = CTkEntry(
    linkedListDemoTab, placeholder_text="Node...", width=75
)
searchLinkedListNodeInput.place(x=290, y=160)

searchLinkedListNodeButton = CTkButton(
    linkedListDemoTab,
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


#! HEAP TASK - EMPLOYEES
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
    heapTaskTab, text="Load employees JSON file", font=("Arial", 14, "bold")
)
heapTaskLoadEmployeesDataHeading.place(x=5, y=210)

heapTaskLoadEmployeesDataInput = CTkEntry(
    heapTaskTab, placeholder_text="Filename...", width=140
)
heapTaskLoadEmployeesDataInput.place(x=5, y=240)

heapTaskLoadEmployeesDataButton = CTkButton(
    heapTaskTab,
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
    heapTaskTab,
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


#! HASH TABLE
class HashTable:
    def __init__(self, size=15):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key):
        return int((key * ((5**0.5 - 1) / 2) % 1) * self.size)

    def insert(self, key, value):
        self.table[self.hash(key)].append((key, value))

    def delete(self, key):
        chain = self.table[self.hash(key)]
        for index, keyValuePair in enumerate(chain):
            if keyValuePair[0] == key:
                del chain[index]
                return True
        return False

    def search(self, key):
        chain = self.table[self.hash(key)]
        for keyValuePair in chain:
            if keyValuePair[0] == key:
                return True
        return False


def updateHashTableElementsContainer():
    for widget in hashTableElementsContainer.winfo_children():
        widget.destroy()

    for pair in hashTableElementsList:
        key, value = pair.split(" ")
        elementText = f"{key} - {value}"
        currentLabel = CTkLabel(hashTableElementsContainer, text=elementText)
        currentLabel.pack(padx=5, anchor="w")


def addHashTableElement(keyValuePair):
    hashTableElementsList.append(keyValuePair)
    key, value = keyValuePair.split(" ")
    key = sum(ord(c) for c in key)

    hashTableElements.insert(key, value)
    updateHashTableElementsContainer()


def deleteHashTableKey(key):
    for el in hashTableElementsList:
        if el.split(" ")[0] == key:
            hashTableElementsList.remove(el)
            break
    convertedKey = sum(ord(c) for c in key)

    res = hashTableElements.delete(convertedKey)
    if not res:
        AlertPopup(f"Failed to delete {key}")

    updateHashTableElementsContainer()


def searchHashTableKey(key):
    convertedKey = sum(ord(c) for c in key)

    res = hashTableElements.search(convertedKey)
    AlertPopup(f"{key} is in the dictionary") if res else AlertPopup(
        f"{key} is NOT in the dictionary"
    )


def saveHashTableOnExit():
    if len(hashTableElementsList) == 0:
        return
    with open("hashTable.json", "w") as f:
        json.dump(hashTableElementsList, f)


def loadHashTableOnStart():
    try:
        with open("hashTable.json", "r") as f:
            res = json.load(f)
            for pair in res:
                addHashTableElement(pair)
    except:
        AlertPopup("Failed to load Hash Table data")


hashOutputBoxesContainer = CTkTabview(dataStructuresTab, width=210, height=290)
hashOutputBoxesContainer.add("Hash Table")
hashOutputBoxesContainer.add("B-Tree")
hashOutputBoxesContainer.add("Subs")
hashOutputBoxesContainer.add("Search")
hashOutputBoxesContainer.place(x=430, y=5)

hashTableElementsTab = hashOutputBoxesContainer.tab("Hash Table")
bTreeElementsTab = hashOutputBoxesContainer.tab("B-Tree")
hashTaskElementsTab = hashOutputBoxesContainer.tab("Search")
bTreeTaskElementsTab = hashOutputBoxesContainer.tab("Subs")

hashTableElementsContainer = CTkScrollableFrame(hashTableElementsTab)
hashTableElementsContainer.pack(padx=5, pady=5, fill="both", expand=True)

bTreeElementsContainer = CTkScrollableFrame(bTreeElementsTab)
bTreeElementsContainer.pack(padx=5, pady=5, fill="both", expand=True)

hashTaskElementsContainer = CTkScrollableFrame(hashTaskElementsTab)
hashTaskElementsContainer.pack(padx=5, pady=5, fill="both", expand=True)

bTreeTaskElementsContainer = CTkScrollableFrame(bTreeTaskElementsTab)
bTreeTaskElementsContainer.pack(padx=5, pady=5, fill="both", expand=True)


addHashTableElementHeading = CTkLabel(
    dataStructuresTab, text="Add Pair", font=("Arial", 14, "bold")
)
addHashTableElementHeading.place(x=5, y=5)

addHashTableElementInput = CTkEntry(
    dataStructuresTab, placeholder_text="Key & Val...", width=75
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
addHashTableElementButton.place(x=85, y=35)

deleteHashTableElementHeading = CTkLabel(
    dataStructuresTab, text="Delete Key", font=("Arial", 14, "bold")
)
deleteHashTableElementHeading.place(x=150, y=5)

deleteHashTableElementInput = CTkEntry(
    dataStructuresTab, placeholder_text="Key...", width=75
)
deleteHashTableElementInput.place(x=150, y=35)

deleteHashTableElementButton = CTkButton(
    dataStructuresTab,
    text="Delete",
    width=45,
    fg_color="#D32F2F",
    hover_color="#B71C1C",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: deleteHashTableKey(deleteHashTableElementInput.get())
    if deleteHashTableElementInput.get()
    else AlertPopup("Input box is empty"),
)
deleteHashTableElementButton.place(x=230, y=35)

searchHashTableElementHeading = CTkLabel(
    dataStructuresTab, text="Search Key", font=("Arial", 14, "bold")
)
searchHashTableElementHeading.place(x=295, y=5)

searchHashTableElementInput = CTkEntry(
    dataStructuresTab, placeholder_text="Key...", width=75
)
searchHashTableElementInput.place(x=295, y=35)

searchHashTableElementButton = CTkButton(
    dataStructuresTab,
    text="Search",
    width=45,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: searchHashTableKey(searchHashTableElementInput.get())
    if searchHashTableElementInput.get()
    else AlertPopup("Input box is empty"),
)
searchHashTableElementButton.place(x=375, y=35)

hashTableElementsList = []
hashTableElements = HashTable()
loadHashTableOnStart()


#! B-TREE
class BTree:
    class BTreeNode:
        def __init__(self, leaf=False):
            self.leaf = leaf
            self.keys = []
            self.child = []

    def __init__(self, t):
        self.root = self.BTreeNode(True)
        self.t = t

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            tempNode = self.BTreeNode()
            self.root = tempNode
            tempNode.child.insert(0, root)
            self._splitChild(tempNode, 0)
            self._insertNonFull(tempNode, key)
        else:
            self._insertNonFull(root, key)

    def searchKey(self, key, nodeA=None):
        if nodeA is not None:
            index = 0
            while index < len(nodeA.keys) and key > nodeA.keys[index][0]:
                index += 1
            if index < len(nodeA.keys) and key == nodeA.keys[index][0]:
                return (True, nodeA, index)
            elif nodeA.leaf:
                return (False, nodeA, index)
            else:
                return self.searchKey(key, nodeA.child[index])
        else:
            return self.searchKey(key, self.root)

    def _insertNonFull(self, nodeA, key):
        i = len(nodeA.keys) - 1
        if nodeA.leaf:
            nodeA.keys.append((None, None))
            while i >= 0 and key < nodeA.keys[i]:
                nodeA.keys[i + 1] = nodeA.keys[i]
                i -= 1
            nodeA.keys[i + 1] = key
        else:
            while i >= 0 and key < nodeA.keys[i]:
                i -= 1
            i += 1
            if len(nodeA.child[i].keys) == (2 * self.t) - 1:
                self._splitChild(nodeA, i)
                if key > nodeA.keys[i]:
                    i += 1
            self._insertNonFull(nodeA.child[i], key)

    def _splitChild(self, nodeA, index):
        t = self.t
        nodeB = nodeA.child[index]
        nodeC = self.BTreeNode(nodeB.leaf)
        nodeA.child.insert(index + 1, nodeC)
        nodeA.keys.insert(index, nodeB.keys[t - 1])
        nodeC.keys = nodeB.keys[t : (2 * t) - 1]
        nodeB.keys = nodeB.keys[0 : t - 1]
        if not nodeB.leaf:
            nodeC.child = nodeB.child[t : 2 * t]
            nodeB.child = nodeB.child[0 : t - 1]


def updateBTreeElementsContainer():
    for widget in bTreeElementsContainer.winfo_children():
        widget.destroy()

    for node in bTreeElementsList:
        currentLabel = CTkLabel(bTreeElementsContainer, text=node)
        currentLabel.pack(padx=5, anchor="w")


def addBTreeNode(data):
    bTreeElements.insert(data)
    bTreeElementsList.append(data)
    updateBTreeElementsContainer()


def searchBTreeNode(data):
    # TODO fix search not working for values >10
    isFound, node, index = bTreeElements.searchKey(data)

    if isFound:
        AlertPopup(f"{data} is in the B-Tree")
    else:
        AlertPopup(f"{data} is NOT in the B-Tree")


def saveBTreeOnExit():
    if len(bTreeElementsList) == 0:
        return
    with open("bTree.json", "w") as file:
        json.dump(bTreeElementsList, file)


def loadBTreeOnStart():
    try:
        with open("bTree.json", "r") as file:
            res = json.load(file)
            for element in res:
                addBTreeNode(element)
    except:
        AlertPopup("Failed to load B-Tree elements")


addBTreeNodeHeading = CTkLabel(
    dataStructuresTab, text="Add Node", font=("Arial", 14, "bold")
)
addBTreeNodeHeading.place(x=5, y=75)

addBTreeNodeInput = CTkEntry(dataStructuresTab, placeholder_text="Node...", width=75)
addBTreeNodeInput.place(x=5, y=105)

addBTreeNodeButton = CTkButton(
    dataStructuresTab,
    text="Add",
    command=lambda: addBTreeNode(addBTreeNodeInput.get())
    if addBTreeNodeInput.get()
    else AlertPopup("Input box is empty"),
    width=45,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
)
addBTreeNodeButton.place(x=85, y=105)

deleteBTreeNodeHeading = CTkLabel(
    dataStructuresTab, text="Delete Node", font=("Arial", 14, "bold")
)
deleteBTreeNodeHeading.place(x=150, y=75)

deleteBTreeNodeInput = CTkEntry(dataStructuresTab, placeholder_text="Node...", width=75)
deleteBTreeNodeInput.place(x=150, y=105)

deleteBTreeNodeButton = CTkButton(
    dataStructuresTab,
    text="Delete",
    command=lambda: deleteBTreeNode(deleteBTreeNodeInput.get())
    if deleteBTreeNodeInput.get()
    else AlertPopup("Input box is empty"),
    width=45,
    fg_color="#D32F2F",
    hover_color="#B71C1C",
    text_color="white",
    font=("Arial", 12, "bold"),
)
deleteBTreeNodeButton.place(x=230, y=105)

searchBTreeNodeHeading = CTkLabel(
    dataStructuresTab, text="Search Node", font=("Arial", 14, "bold")
)
searchBTreeNodeHeading.place(x=295, y=75)

searchBTreeNodeInput = CTkEntry(dataStructuresTab, placeholder_text="Node...", width=75)
searchBTreeNodeInput.place(x=295, y=105)

searchBTreeNodeButton = CTkButton(
    dataStructuresTab,
    text="Search",
    command=lambda: searchBTreeNode(searchBTreeNodeInput.get())
    if searchBTreeNodeInput.get()
    else AlertPopup("Input box is empty"),
    width=45,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
)
searchBTreeNodeButton.place(x=375, y=105)

bTreeElementsList = []
bTreeElements = BTree(3)
loadBTreeOnStart()


#! B-TREE TASK
class Subscriber:
    def __init__(self, phone, name, type):
        self.phone = phone
        self.name = name
        self.type = type

    def toDict(self):
        return {
            "phone": self.phone,
            "name": self.name,
            "type": self.type,
        }


def updateBTreeTaskElementsContainer():
    for widget in bTreeTaskElementsContainer.winfo_children():
        widget.destroy()

    for subscriber in bTreeTaskSubscribers:
        currentLabelString = f"+{subscriber.phone} - {subscriber.name}"
        currentLabel = CTkLabel(bTreeTaskElementsContainer, text=currentLabelString)
        currentLabel.pack(padx=5, anchor="w")


def bTreeTaskSearchForSub(data):
    isFound, node, index = bTreeTaskElements.searchKey(data)

    if isFound:
        subInfo = node.keys[index][1]
        alertString = f"{subInfo['name']} was found:\nSubscription type: {subInfo['type']}\nPhone: +{subInfo['phone']}"
        AlertPopup(alertString)
    else:
        AlertPopup("Subscriber was not found in the database")


def loadBTreeTaskData(fileName):
    dataHolder = []
    try:
        with open(fileName, "r") as file:
            dataHolder = json.load(file)
    except:
        AlertPopup(f"Failed to load subscribers' data from {fileName}")

    for element in dataHolder:
        phone, name, type = element["phone"], element["name"], element["type"]
        currentSubObject = Subscriber(phone, name, type)
        bTreeTaskSubscribers.append(currentSubObject)

    for sub in bTreeTaskSubscribers:
        bTreeTaskElements.insert((sub.phone, sub.toDict()))
    updateBTreeTaskElementsContainer()


loadBTreeTaskDataHeading = CTkLabel(
    dataStructuresTab, text="Load subscribers JSON", font=("Arial", 14, "bold")
)
loadBTreeTaskDataHeading.place(x=5, y=145)

loadBTreeTaskDataInput = CTkEntry(
    dataStructuresTab, placeholder_text="Filename...", width=110
)
loadBTreeTaskDataInput.place(x=5, y=175)

loadBTreeTaskDataButton = CTkButton(
    dataStructuresTab,
    text="Load",
    width=45,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: loadBTreeTaskData(loadBTreeTaskDataInput.get())
    if loadBTreeTaskDataInput.get()
    else AlertPopup("Input box is empty"),
)
loadBTreeTaskDataButton.place(x=120, y=175)

bTreeTaskSearchForSubHeading = CTkLabel(
    dataStructuresTab, text="Search for subscriber", font=("Arial", 14, "bold")
)
bTreeTaskSearchForSubHeading.place(x=185, y=145)

bTreeTaskSearchForSubInput = CTkEntry(
    dataStructuresTab, placeholder_text="Number...", width=110
)
bTreeTaskSearchForSubInput.place(x=185, y=175)

bTreeTaskSearchForSubButton = CTkButton(
    dataStructuresTab,
    text="Search",
    width=45,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: bTreeTaskSearchForSub(bTreeTaskSearchForSubInput.get())
    if bTreeTaskSearchForSubInput.get()
    else AlertPopup("Input box is empty"),
)
bTreeTaskSearchForSubButton.place(x=300, y=175)

bTreeTaskSubscribers = []
bTreeTaskElements = BTree(3)


#! HASH TABLE TASK
def updateHashTaskElementsContainer():
    for widget in hashTaskElementsContainer.winfo_children():
        widget.destroy()

    for pair in hashTaskEmployeesList:
        name, position = pair.strip().split(",")
        elementText = f"{name} - {position}"
        currentLabel = CTkLabel(hashTaskElementsContainer, text=elementText)
        currentLabel.pack(padx=5, anchor="w")


def hashTaskLoadData(fileName):
    try:
        with open(fileName, "r") as file:
            for line in file:
                name, position = line.strip().split(",")
                key = sum(ord(c) for c in name)
                hashTaskEmployees.insert(key, (name, position))
                hashTaskEmployeesList.append(line)
            updateHashTaskElementsContainer()
    except:
        AlertPopup(f"Failed to load data from {fileName}")


def hashTaskSearch(givenName):
    convertedKey = sum(ord(c) for c in givenName)
    if hashTaskEmployees.search(convertedKey):
        position = None
        for employeeData in hashTaskEmployeesList:
            thisName, thisPosition = employeeData.strip().split(",")
            if thisName == givenName:
                position = thisPosition
                break
        AlertPopup(f"{givenName} is found. They work as {position}")
    else:
        AlertPopup(f"{givenName} is NOT found")


hashTaskLoadDataHeading = CTkLabel(
    dataStructuresTab, text="Load employees MD", font=("Arial", 14, "bold")
)
hashTaskLoadDataHeading.place(x=5, y=215)

hashTaskLoadDataInput = CTkEntry(
    dataStructuresTab, placeholder_text="Filename...", width=110
)
hashTaskLoadDataInput.place(x=5, y=245)

hashTaskLoadDataButton = CTkButton(
    dataStructuresTab,
    text="Load",
    width=45,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: hashTaskLoadData(hashTaskLoadDataInput.get())
    if hashTaskLoadDataInput.get()
    else AlertPopup("Input box is empty"),
)
hashTaskLoadDataButton.place(x=120, y=245)

hashTaskSearchHeading = CTkLabel(
    dataStructuresTab, text="Find position", font=("Arial", 14, "bold")
)
hashTaskSearchHeading.place(x=185, y=215)

hashTaskSearchInput = CTkEntry(
    dataStructuresTab, placeholder_text="Employee...", width=110
)
hashTaskSearchInput.place(x=185, y=245)

hashTaskSearchButton = CTkButton(
    dataStructuresTab,
    text="Search",
    width=45,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: hashTaskSearch(hashTaskSearchInput.get())
    if hashTaskSearchInput.get()
    else AlertPopup("Input box is empty"),
)
hashTaskSearchButton.place(x=300, y=245)

hashTaskEmployeesList = []
hashTaskEmployees = HashTable()


#! HUFFMAN CODING
class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

    def buildFrequencyDict(self, text):
        frequency = {}
        for char in text:
            if char not in frequency:
                frequency[char] = 0
            frequency[char] += 1
        return frequency

    def buildHeap(self, frequency):
        for key in frequency:
            node = self.HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def mergeNodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = self.HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def _buildCodesHelper(self, root, currentCode):
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = currentCode
            self.reverse_mapping[currentCode] = root.char
            return

        self._buildCodesHelper(root.left, currentCode + "0")
        self._buildCodesHelper(root.right, currentCode + "1")

    def buildCodes(self):
        root = heapq.heappop(self.heap)
        currentCode = ""
        self._buildCodesHelper(root, currentCode)

    def getEncodedText(self, text):
        encodedText = ""
        for char in text:
            encodedText += self.codes[char]
        return encodedText

    def padEncodedText(self, encodedText):
        extraPadding = 8 - len(encodedText) % 8
        for i in range(extraPadding):
            encodedText += "0"

        paddingInfo = "{0:08b}".format(extraPadding)
        encodedText = paddingInfo + encodedText
        return encodedText

    def getByteArray(self, paddedEncodedText):
        if len(paddedEncodedText) % 8 != 0:
            print("Encoded text not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0, len(paddedEncodedText), 8):
            byte = paddedEncodedText[i : i + 8]
            b.append(int(byte, 2))
        return b

    def compress(self, filePath):
        fileName, fileExtension = os.path.splitext(filePath)
        outputPath = fileName + ".bin"

        with open(filePath, "r+") as file, open(outputPath, "wb") as output:
            text = file.read()
            text = text.rstrip()

            frequency = self.buildFrequencyDict(text)
            self.buildHeap(frequency)
            self.mergeNodes()
            self.buildCodes()

            encodedText = self.getEncodedText(text)
            paddedEncodedText = self.padEncodedText(encodedText)

            b = self.getByteArray(paddedEncodedText)
            output.write(bytes(b))

        return outputPath

    def removePadding(self, paddedEncodedText):
        paddedInfo = paddedEncodedText[:8]
        extraPadding = int(paddedInfo, 2)

        paddedEncodedText = paddedEncodedText[8:]
        encodedText = paddedEncodedText[: -1 * extraPadding]

        return encodedText

    def decodeText(self, encodedText):
        currentCode = ""
        decodedText = ""

        for bit in encodedText:
            currentCode += bit
            if currentCode in self.reverse_mapping:
                character = self.reverse_mapping[currentCode]
                decodedText += character
                currentCode = ""

        return decodedText

    def decompress(self, filePath):
        fileName, fileExtension = os.path.splitext(filePath)
        outputPath = fileName + "_decompressed.txt"

        with open(filePath, "rb") as file, open(outputPath, "w") as output:
            bitString = ""

            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, "0")
                bitString += bits
                byte = file.read(1)

            encodedText = self.removePadding(bitString)
            decodedText = self.decodeText(encodedText)

            output.write(decodedText)

        return outputPath


greedyAlgosTabsContainer = CTkTabview(greedyAlgosTab)
greedyAlgosTabsContainer.add("Huffman Coding")
greedyAlgosTabsContainer.add("Greedy Algorithm Task")
greedyAlgosTabsContainer.pack(fill="both", expand=True)

huffmanCodingTab = greedyAlgosTabsContainer.tab("Huffman Coding")
greedyTaskTab = greedyAlgosTabsContainer.tab("Greedy Algorithm Task")


def huffmanLoadAndCompress(fileName):
    try:
        global huffmanInputFilePath
        huffmanInputFilePath = fileName
        huffmanInputFilePathLabel.configure(text=f"Loaded file: {fileName}")

        global huffmanCompressedFilePath
        huffmanCompressedFilePath = huffmanObject.compress(fileName)

        global huffmanOriginalFileWeight
        huffmanOriginalFileWeight = os.path.getsize(fileName)
        huffmanOriginalFileWeightLabel.configure(
            text=f"Original weight: {huffmanOriginalFileWeight/1024:.2f} KB or {huffmanOriginalFileWeight/1024/1024:.2f} MB"
        )

        global huffmanCompressedFileWeight
        huffmanCompressedFileWeight = os.path.getsize(huffmanCompressedFilePath)
        huffmanCompressedFileWeightLabel.configure(
            text=f"Compressed weight: {huffmanCompressedFileWeight/1024:.2f} KB or {huffmanCompressedFileWeight/1024/1024:.2f} MB"
        )

        global huffmanCompressionRatio
        huffmanCompressionRatio = huffmanCompressionRatio = (
            1 - huffmanCompressedFileWeight / huffmanOriginalFileWeight
        ) * 100
        huffmanCompressionRatioLabel.configure(
            text=f"Compression Ratio: {huffmanCompressionRatio:.2f}%"
        )
    except:
        AlertPopup("Failed to compress")


def huffmanDecompress():
    try:
        global huffmanDecompressedFilePath
        huffmanDecompressedFilePath = huffmanObject.decompress(
            huffmanCompressedFilePath
        )
        huffmanDecompressedFilePathLabel.configure(
            text=f"Decompressed file: {huffmanDecompressedFilePath}"
        )

        huffmanDecompressedFileWeightLabel.configure(
            text=f"Decompressed weight: {os.path.getsize(huffmanDecompressedFilePath)/1024:.2f} KB or {os.path.getsize(huffmanDecompressedFilePath)/1024/1024:.2f} MB"
        )
    except:
        AlertPopup("Failed to decompress")


huffmanLoadFileHeading = CTkLabel(
    huffmanCodingTab, text="Load Text File", font=("Arial", 14, "bold")
)
huffmanLoadFileHeading.place(x=0, y=0)

huffmanLoadFileInput = CTkEntry(
    huffmanCodingTab, placeholder_text="Filename...", width=120
)
huffmanLoadFileInput.place(x=0, y=30)

huffmanLoadFileButton = CTkButton(
    huffmanCodingTab,
    text="Load",
    width=60,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: huffmanLoadAndCompress(huffmanLoadFileInput.get())
    if huffmanLoadFileInput.get()
    else AlertPopup("Input box is empty"),
)
huffmanLoadFileButton.place(x=125, y=30)

huffmanDecompressFileButton = CTkButton(
    huffmanCodingTab,
    text="Decompress",
    width=80,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: huffmanDecompress()
    if huffmanCompressedFilePath
    else AlertPopup("No file loaded"),
)
huffmanDecompressFileButton.place(x=200, y=30)

huffmanInputFilePathLabel = CTkLabel(
    huffmanCodingTab,
    text="No file loaded",
    font=("Arial", 12),
)
huffmanInputFilePathLabel.place(x=0, y=70)

huffmanCompressedFileWeightLabel = CTkLabel(
    huffmanCodingTab,
    text="File weight: ",
    font=("Arial", 12),
)
huffmanCompressedFileWeightLabel.place(x=0, y=90)

huffmanOriginalFileWeightLabel = CTkLabel(
    huffmanCodingTab,
    text="Original file weight: ",
    font=("Arial", 12),
)
huffmanOriginalFileWeightLabel.place(x=0, y=110)

huffmanCompressionRatioLabel = CTkLabel(
    huffmanCodingTab,
    text="Compression ratio: ",
    font=("Arial", 12),
)
huffmanCompressionRatioLabel.place(x=0, y=130)

huffmanDecompressedFilePathLabel = CTkLabel(
    huffmanCodingTab,
    text="No file decompressed",
    font=("Arial", 12),
)
huffmanDecompressedFilePathLabel.place(x=0, y=160)

huffmanDecompressedFileWeightLabel = CTkLabel(
    huffmanCodingTab,
    text="Decompressed file weight: ",
    font=("Arial", 12),
)
huffmanDecompressedFileWeightLabel.place(x=0, y=180)

huffmanObject = HuffmanCoding()
huffmanInputFilePath = None
huffmanCompressedFilePath = None
huffmanDecompressedFilePath = None

huffmanOriginalFileWeight = None
huffmanCompressedFileWeight = None
huffmanCompressionRatio = None


#! GREEDY ALGORITHMS
class Shopkeeper:
    def __init__(self, products):
        self.products = products
        self.popularProducts = set()
        self.productsFreqency = {product: 0 for product in products}

    def solveProblem(self, customerOrder):
        queueTime = 0
        for product in customerOrder:
            if product not in self.productsFreqency:
                self.productsFreqency[product] = 0

            if product in self.popularProducts:
                queueTime += 1
            elif product in self.products:
                queueTime += 2
                self.productsFreqency[product] += 1
            else:
                queueTime += 3
        self.updatePopularProducts()
        return queueTime

    def updatePopularProducts(self):
        mostPopularProduct = max(self.productsFreqency, key=self.productsFreqency.get)
        self.popularProducts.add(mostPopularProduct)
        del self.productsFreqency[mostPopularProduct]

        greedyTaskUpdatePopularProductsContainer()

    def updateProducts(self, newProducts):
        self.products = newProducts
        greedyTaskUpdateProductsContainer()


def greedyTaskUpdatePopularProductsContainer():
    for widget in greedyTaskPopularProductsContainer.winfo_children():
        widget.destroy()

    for product in greedyTaskShop.popularProducts:
        CTkLabel(
            greedyTaskPopularProductsContainer,
            text=product,
        ).pack(padx=5, pady=5, anchor="w")


def greedyTaskUpdateProductsContainer():
    for widget in greedyTaskProductsContainer.winfo_children():
        widget.destroy()

    for product in greedyTaskShop.products:
        CTkLabel(
            greedyTaskProductsContainer,
            text=product,
        ).pack(padx=5, pady=5, anchor="w")


def greedyTaskLoadProductsFromFile(fileName):
    with open(fileName, "r") as file:
        products = json.load(file)
    greedyTaskShop.updateProducts(products)


def greedyTaskPlaceOrder(order):
    order = order.split(",")
    queueTime = greedyTaskShop.solveProblem(order)
    AlertPopup(f"Queue time: {queueTime}")


greedyTaskTabsContainer = CTkTabview(greedyTaskTab)
greedyTaskTabsContainer.add("Products")
greedyTaskTabsContainer.add("Popular Products")
greedyTaskTabsContainer.place(x=400, y=0)

greedyTaskProductsContainer = CTkScrollableFrame(
    greedyTaskTabsContainer.tab("Products")
)
greedyTaskProductsContainer.pack(side="left", fill="both", expand=True)

greedyTaskPopularProductsContainer = CTkScrollableFrame(
    greedyTaskTabsContainer.tab("Popular Products")
)
greedyTaskPopularProductsContainer.pack(side="left", fill="both", expand=True)


greedyTaskAddProductsHeading = CTkLabel(
    greedyTaskTab,
    text="Fill up shelves with products",
    font=("Arial", 14, "bold"),
)
greedyTaskAddProductsHeading.place(x=0, y=0)

greedyTaskAddProductsInput = CTkEntry(
    greedyTaskTab,
    placeholder_text="Products separated by comma...",
    width=300,
)
greedyTaskAddProductsInput.place(x=0, y=30)

greedyTaskAddProductsButton = CTkButton(
    greedyTaskTab,
    text="Add",
    width=60,
    command=lambda: greedyTaskShop.updateProducts(
        greedyTaskAddProductsInput.get().split(",")
    )
    if greedyTaskAddProductsInput.get()
    else AlertPopup("Enter products first"),
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
)
greedyTaskAddProductsButton.place(x=305, y=30)

greedyTaskLoadProductsHeading = CTkLabel(
    greedyTaskTab,
    text="or, Load products from JSON file",
    font=("Arial", 14, "bold"),
)
greedyTaskLoadProductsHeading.place(x=0, y=70)

greedyTaskLoadProductsInput = CTkEntry(
    greedyTaskTab,
    placeholder_text="Path to JSON file...",
    width=250,
)
greedyTaskLoadProductsInput.place(x=0, y=100)

greedyTaskLoadProductsButton = CTkButton(
    greedyTaskTab,
    text="Load from JSON",
    width=110,
    command=lambda: greedyTaskLoadProductsFromFile(greedyTaskLoadProductsInput.get())
    if greedyTaskLoadProductsInput.get()
    else AlertPopup("Enter path first"),
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
)
greedyTaskLoadProductsButton.place(x=255, y=100)

greedyTaskPlaceOrderHeading = CTkLabel(
    greedyTaskTab,
    text="Place order",
    font=("Arial", 14, "bold"),
)
greedyTaskPlaceOrderHeading.place(x=0, y=160)

greedyTaskPlaceOrderInput = CTkEntry(
    greedyTaskTab,
    placeholder_text="Products separated by comma...",
    width=300,
)
greedyTaskPlaceOrderInput.place(x=0, y=190)

greedyTaskPlaceOrderButton = CTkButton(
    greedyTaskTab,
    text="Place",
    width=60,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: greedyTaskPlaceOrder(greedyTaskPlaceOrderInput.get())
    if greedyTaskPlaceOrderInput.get()
    else AlertPopup("Enter products first"),
)
greedyTaskPlaceOrderButton.place(x=305, y=190)

greedyTaskShop = Shopkeeper([])

app.mainloop()
saveHeapOnExit()
saveLinkedListOnExit()
saveHashTableOnExit()
saveBTreeOnExit()
