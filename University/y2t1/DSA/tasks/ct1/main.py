from customtkinter import *
import time
import json
import heapq
import os
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict, deque


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
    linkedListDemoTab, text="Add Linked List Node", font=("Arial", 14, "bold")
)
addLinkedListNodeHeading.place(x=0, y=0)

addLinkedListNodeInput = CTkEntry(
    linkedListDemoTab, placeholder_text="Node value...", width=300
)
addLinkedListNodeInput.place(x=0, y=30)

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
addLinkedListNodeButton.place(x=305, y=30)

deleteHeapNodeHeading = CTkLabel(
    linkedListDemoTab, text="Delete Linked List Node", font=("Arial", 14, "bold")
)
deleteHeapNodeHeading.place(x=0, y=70)

deleteLinkedListNodeInput = CTkEntry(
    linkedListDemoTab, placeholder_text="Node...", width=300
)
deleteLinkedListNodeInput.place(x=0, y=100)

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
deleteLinkedListNodeButton.place(x=305, y=100)

searchLinkedListNodeHeading = CTkLabel(
    linkedListDemoTab, text="Search Linked List Node", font=("Arial", 14, "bold")
)
searchLinkedListNodeHeading.place(x=0, y=140)

searchLinkedListNodeInput = CTkEntry(
    linkedListDemoTab, placeholder_text="Node...", width=300
)
searchLinkedListNodeInput.place(x=0, y=170)

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
searchLinkedListNodeButton.place(x=305, y=170)

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
heapTaskLoadEmployeesDataHeading.place(x=0, y=0)

heapTaskLoadEmployeesDataInput = CTkEntry(
    heapTaskTab, placeholder_text="Filename...", width=140
)
heapTaskLoadEmployeesDataInput.place(x=0, y=30)

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
heapTaskLoadEmployeesDataButton.place(x=150, y=30)

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
heapTaskShowResultsButton.place(x=220, y=30)

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


dataStructuresTabsContainer = CTkTabview(dataStructuresTab, width=210, height=290)
dataStructuresTabsContainer.add("Hash Table")
dataStructuresTabsContainer.add("B-Tree")
dataStructuresTabsContainer.add("Subscribers Search")
dataStructuresTabsContainer.add("Employees Search")
dataStructuresTabsContainer.pack(fill="both", expand=True)

hashTableDemoTab = dataStructuresTabsContainer.tab("Hash Table")
bTreeDemoTab = dataStructuresTabsContainer.tab("B-Tree")
bTreeTaskTab = dataStructuresTabsContainer.tab("Subscribers Search")
hashTaskTab = dataStructuresTabsContainer.tab("Employees Search")

hashTableElementsContainer = CTkScrollableFrame(hashTableDemoTab, width=240, height=270)
hashTableElementsContainer.place(x=400, y=0)

bTreeElementsContainer = CTkScrollableFrame(bTreeDemoTab, width=240, height=270)
bTreeElementsContainer.place(x=400, y=0)

hashTaskElementsContainer = CTkScrollableFrame(hashTaskTab, width=240, height=270)
hashTaskElementsContainer.place(x=400, y=0)

bTreeTaskElementsContainer = CTkScrollableFrame(bTreeTaskTab, width=240, height=270)
bTreeTaskElementsContainer.place(x=400, y=0)


addHashTableElementHeading = CTkLabel(
    hashTableDemoTab, text="Add Key-Value Pair", font=("Arial", 14, "bold")
)
addHashTableElementHeading.place(x=0, y=0)

addHashTableElementInput = CTkEntry(
    hashTableDemoTab, placeholder_text="Key & Val...", width=300
)
addHashTableElementInput.place(x=0, y=30)

addHashTableElementButton = CTkButton(
    hashTableDemoTab,
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
addHashTableElementButton.place(x=305, y=30)

deleteHashTableElementHeading = CTkLabel(
    hashTableDemoTab, text="Delete Hash Table Key", font=("Arial", 14, "bold")
)
deleteHashTableElementHeading.place(x=0, y=70)

deleteHashTableElementInput = CTkEntry(
    hashTableDemoTab, placeholder_text="Key...", width=300
)
deleteHashTableElementInput.place(x=0, y=100)

deleteHashTableElementButton = CTkButton(
    hashTableDemoTab,
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
deleteHashTableElementButton.place(x=305, y=100)

searchHashTableElementHeading = CTkLabel(
    hashTableDemoTab, text="Search Hash Table Key", font=("Arial", 14, "bold")
)
searchHashTableElementHeading.place(x=0, y=140)

searchHashTableElementInput = CTkEntry(
    hashTableDemoTab, placeholder_text="Key...", width=300
)
searchHashTableElementInput.place(x=0, y=170)

searchHashTableElementButton = CTkButton(
    hashTableDemoTab,
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
searchHashTableElementButton.place(x=305, y=170)

hashTableElementsList = []
hashTableElements = HashTable()
loadHashTableOnStart()


#! B-TREE
# TODO fix deletion not working - understand it truly
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

    def delete(self, key):
        nodeA, index = self.searchKey(key)
        if nodeA is not None:
            if nodeA.leaf:
                nodeA.keys.pop(index)
            return True
        else:
            return False

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


def deleteBTreeNode(data):
    bTreeElements.delete(data)
    bTreeElementsList.remove(data)
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
    bTreeDemoTab, text="Add B-Tree Node", font=("Arial", 14, "bold")
)
addBTreeNodeHeading.place(x=0, y=0)

addBTreeNodeInput = CTkEntry(bTreeDemoTab, placeholder_text="Node...", width=300)
addBTreeNodeInput.place(x=0, y=30)

addBTreeNodeButton = CTkButton(
    bTreeDemoTab,
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
addBTreeNodeButton.place(x=305, y=30)

deleteBTreeNodeHeading = CTkLabel(
    bTreeDemoTab, text="Delete B-Tree Node", font=("Arial", 14, "bold")
)
deleteBTreeNodeHeading.place(x=0, y=70)

deleteBTreeNodeInput = CTkEntry(bTreeDemoTab, placeholder_text="Node...", width=300)
deleteBTreeNodeInput.place(x=0, y=100)

deleteBTreeNodeButton = CTkButton(
    bTreeDemoTab,
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
deleteBTreeNodeButton.place(x=305, y=100)

searchBTreeNodeHeading = CTkLabel(
    bTreeDemoTab, text="Search B-Tree Node", font=("Arial", 14, "bold")
)
searchBTreeNodeHeading.place(x=0, y=140)

searchBTreeNodeInput = CTkEntry(bTreeDemoTab, placeholder_text="Node...", width=300)
searchBTreeNodeInput.place(x=0, y=170)

searchBTreeNodeButton = CTkButton(
    bTreeDemoTab,
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
searchBTreeNodeButton.place(x=305, y=170)

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
    bTreeTaskTab, text="Load subscribers JSON", font=("Arial", 14, "bold")
)
loadBTreeTaskDataHeading.place(x=0, y=0)

loadBTreeTaskDataInput = CTkEntry(
    bTreeTaskTab, placeholder_text="Filename...", width=300
)
loadBTreeTaskDataInput.place(x=0, y=30)

loadBTreeTaskDataButton = CTkButton(
    bTreeTaskTab,
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
loadBTreeTaskDataButton.place(x=305, y=30)

bTreeTaskSearchForSubHeading = CTkLabel(
    bTreeTaskTab, text="Search for subscriber", font=("Arial", 14, "bold")
)
bTreeTaskSearchForSubHeading.place(x=0, y=70)

bTreeTaskSearchForSubInput = CTkEntry(
    bTreeTaskTab, placeholder_text="Number...", width=300
)
bTreeTaskSearchForSubInput.place(x=0, y=100)

bTreeTaskSearchForSubButton = CTkButton(
    bTreeTaskTab,
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
bTreeTaskSearchForSubButton.place(x=305, y=100)

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
    hashTaskTab, text="Load employees MD", font=("Arial", 14, "bold")
)
hashTaskLoadDataHeading.place(x=0, y=0)

hashTaskLoadDataInput = CTkEntry(hashTaskTab, placeholder_text="Filename...", width=300)
hashTaskLoadDataInput.place(x=0, y=30)

hashTaskLoadDataButton = CTkButton(
    hashTaskTab,
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
hashTaskLoadDataButton.place(x=305, y=30)

hashTaskSearchHeading = CTkLabel(
    hashTaskTab, text="Find position of an employee", font=("Arial", 14, "bold")
)
hashTaskSearchHeading.place(x=0, y=70)

hashTaskSearchInput = CTkEntry(hashTaskTab, placeholder_text="Employee...", width=300)
hashTaskSearchInput.place(x=0, y=100)

hashTaskSearchButton = CTkButton(
    hashTaskTab,
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
hashTaskSearchButton.place(x=305, y=100)

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
        productTimes = []
        for product in customerOrder:
            originalTime = queueTime
            if product not in self.productsFreqency:
                self.productsFreqency[product] = 0

            if product in self.popularProducts:
                queueTime += 1
            elif product in self.products:
                queueTime += 2
                self.productsFreqency[product] += 1
            else:
                queueTime += 3
            takenTime = queueTime - originalTime
            productTimes.append(f"{product[0].upper() + product[1:]} - {takenTime}")
        self.updatePopularProducts()
        return queueTime, productTimes

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


def greedyTaskUpdateOrdersContainer():
    for widget in greedyTaskOrdersContainer.winfo_children():
        widget.destroy()

    for order in greedyTaskOrders:
        orderString = ", ".join(order)
        CTkLabel(
            greedyTaskOrdersContainer,
            text=orderString,
        ).pack(padx=5, pady=5, anchor="w")


def greedyTaskLoadProductsFromFile(fileName):
    with open(fileName, "r") as file:
        products = json.load(file)
    greedyTaskShop.updateProducts(products)


def greedyTaskPlaceOrder(order):
    order = order.split(",")
    queueTime, productTimes = greedyTaskShop.solveProblem(order)
    productTimesString = "\nTime taken to fetch each product:"
    for product in productTimes:
        productTimesString += f"\n{product} minutes"
    AlertPopup(f"Queue time: {queueTime}\n{productTimesString}")

    greedyTaskOrders.append(order)
    greedyTaskUpdateOrdersContainer()


greedyTaskTabsContainer = CTkTabview(greedyTaskTab)
greedyTaskTabsContainer.add("Products")
greedyTaskTabsContainer.add("Popular Products")
greedyTaskTabsContainer.add("Orders")
greedyTaskTabsContainer.place(x=380, y=0)

greedyTaskProductsContainer = CTkScrollableFrame(
    greedyTaskTabsContainer.tab("Products")
)
greedyTaskProductsContainer.pack(side="left", fill="both", expand=True)

greedyTaskPopularProductsContainer = CTkScrollableFrame(
    greedyTaskTabsContainer.tab("Popular Products")
)
greedyTaskPopularProductsContainer.pack(side="left", fill="both", expand=True)

greedyTaskOrdersContainer = CTkScrollableFrame(greedyTaskTabsContainer.tab("Orders"))
greedyTaskOrdersContainer.pack(side="left", fill="both", expand=True)

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

greedyTaskOrders = []
greedyTaskShop = Shopkeeper([])


#! ROBOTS TASK
# TODO add ability to load from JSON
class RobotGroup:
    def __init__(self, num_robots, speeds, num_groups):
        self.robotsCount = num_robots
        self.speeds = speeds
        self.groupsCount = num_groups
        self.dp = [[-1] * (num_robots + 1) for _ in range(num_groups + 1)]

    def countWays(self):
        return self._countWaysHelper(self.groupsCount, self.robotsCount)

    def _countWaysHelper(self, groups, robots):
        if groups == 0 and robots == 0:
            return 1
        if groups == 0 or robots == 0:
            return 0
        if self.dp[groups][robots] != -1:
            return self.dp[groups][robots]

        ways = 0
        for i in range(1, robots + 1):
            ways += self._countWaysHelper(groups - 1, i - 1)
        self.dp[groups][robots] = ways
        return ways


def solveRobotsTask(robotsCount, speeds, groupsCount):
    robotGroup = RobotGroup(robotsCount, speeds, groupsCount)
    res = robotGroup.countWays()
    AlertPopup(f"Number of ways to arrange {groupsCount} groups is {res}")


dynamicProgrammingTabsContainer = CTkTabview(dynamicProgrammingTab)
dynamicProgrammingTabsContainer.add("Robot Groups")
dynamicProgrammingTabsContainer.add("Buildings' Arrangements")
dynamicProgrammingTabsContainer.pack(expand=True, fill="both")

robotsTaskTab = dynamicProgrammingTabsContainer.tab("Robot Groups")
buildingsTaskTab = dynamicProgrammingTabsContainer.tab("Buildings' Arrangements")


robotsTaskGetRobotsCountHeading = CTkLabel(
    robotsTaskTab,
    text="Enter number of robots",
    font=("Arial", 14, "bold"),
)
robotsTaskGetRobotsCountHeading.place(x=0, y=0)

robotsTaskGetRobotsCountInput = CTkEntry(
    robotsTaskTab,
    placeholder_text="Number of robots...",
    width=300,
)
robotsTaskGetRobotsCountInput.place(x=0, y=30)

robotsTaskGetRobotsSpeedsHeading = CTkLabel(
    robotsTaskTab,
    text="Enter speeds of the robots",
    font=("Arial", 14, "bold"),
)
robotsTaskGetRobotsSpeedsHeading.place(x=0, y=70)

robotsTaskGetRobotsSpeedsInput = CTkEntry(
    robotsTaskTab,
    placeholder_text="Speeds of the robots separated by comma...",
    width=300,
)
robotsTaskGetRobotsSpeedsInput.place(x=0, y=100)

robotsTaskGetGroupsCountHeading = CTkLabel(
    robotsTaskTab,
    text="Enter number of groups",
    font=("Arial", 14, "bold"),
)
robotsTaskGetGroupsCountHeading.place(x=0, y=140)

robotsTaskGetGroupsCountInput = CTkEntry(
    robotsTaskTab,
    placeholder_text="Number of groups...",
    width=300,
)
robotsTaskGetGroupsCountInput.place(x=0, y=170)

robotsTaskShowResultsButton = CTkButton(
    robotsTaskTab,
    text="Show results",
    width=110,
    text_color="white",
    font=("Arial", 12, "bold"),
    fg_color="#28A228",
    hover_color="#1F7D1F",
    command=lambda: solveRobotsTask(
        int(robotsTaskGetRobotsCountInput.get()),
        list(map(int, robotsTaskGetRobotsSpeedsInput.get().split(","))),
        int(robotsTaskGetGroupsCountInput.get()),
    )
    if robotsTaskGetRobotsCountInput.get()
    and robotsTaskGetRobotsSpeedsInput.get()
    and robotsTaskGetGroupsCountInput.get()
    else AlertPopup("Fill in all the fields first"),
)
robotsTaskShowResultsButton.place(x=0, y=220)


#! BUILDINGS' ARRANGEMENTS
class BuildingArrangement:
    def __init__(self, matrix):
        self.matrix = matrix
        self.memo = {}

    def solveTask(self, buildingsCount):
        return self._solveTaskUtil(buildingsCount, "Residential")

    def _solveTaskUtil(self, n, buildingType):
        if n == 0:
            return 1

        if (n, buildingType) in self.memo:
            return self.memo[(n, buildingType)]

        count = 0
        for previousBuildingType in ["Residential", "Industrial", "Office"]:
            if self.matrix[previousBuildingType][buildingType]:
                count += self._solveTaskUtil(n - 1, previousBuildingType)

        self.memo[(n, buildingType)] = count
        return count


def buildingsTaskSolve(
    residentialToResidential,
    residentialToIndustrial,
    residentialToOffice,
    industrialToResidential,
    industrialToIndustrial,
    industrialToOffice,
    officeToResidential,
    officeToIndustrial,
    officeToOffice,
    buildingsCount,
):
    matrix = {
        "Residential": {
            "Residential": residentialToResidential,
            "Industrial": residentialToIndustrial,
            "Office": residentialToOffice,
        },
        "Industrial": {
            "Residential": industrialToResidential,
            "Industrial": industrialToIndustrial,
            "Office": industrialToOffice,
        },
        "Office": {
            "Residential": officeToResidential,
            "Industrial": officeToIndustrial,
            "Office": officeToOffice,
        },
    }
    arrangements = BuildingArrangement(matrix)
    res = arrangements.solveTask(int(buildingsCount))
    AlertPopup(f"Number of arrangements: {res}")


buildingsTaskGetMatrixForResidentialHeading = CTkLabel(
    buildingsTaskTab,
    text="Can be built next to residential buildings",
    font=("Arial", 12),
)
buildingsTaskGetMatrixForResidentialHeading.place(x=0, y=0)

buildingsTaskGetInputResidentialToResidential = CTkCheckBox(
    buildingsTaskTab, text="Residential", onvalue=1, offvalue=0
)
buildingsTaskGetInputResidentialToResidential.place(x=0, y=30)

buildingsTaskGetInputResidentialToIndustrial = CTkCheckBox(
    buildingsTaskTab, text="Industrial", onvalue=1, offvalue=0
)
buildingsTaskGetInputResidentialToIndustrial.place(x=110, y=30)

buildingsTaskGetInputResidentialToOffice = CTkCheckBox(
    buildingsTaskTab, text="Office", onvalue=1, offvalue=0
)
buildingsTaskGetInputResidentialToOffice.place(x=210, y=30)

buildingsTaskGetMatrixForIndustrialHeading = CTkLabel(
    buildingsTaskTab,
    text="Can be built next to industrial buildings",
    font=("Arial", 12),
)
buildingsTaskGetMatrixForIndustrialHeading.place(x=0, y=70)

buildingsTaskGetInputIndustrialToResidential = CTkCheckBox(
    buildingsTaskTab, text="Residential", onvalue=1, offvalue=0
)
buildingsTaskGetInputIndustrialToResidential.place(x=0, y=100)

buildingsTaskGetInputIndustrialToIndustrial = CTkCheckBox(
    buildingsTaskTab, text="Industrial", onvalue=1, offvalue=0
)
buildingsTaskGetInputIndustrialToIndustrial.place(x=110, y=100)

buildingsTaskGetInputIndustrialToOffice = CTkCheckBox(
    buildingsTaskTab, text="Office", onvalue=1, offvalue=0
)
buildingsTaskGetInputIndustrialToOffice.place(x=210, y=100)

buildingsTaskGetMatrixForOfficeHeading = CTkLabel(
    buildingsTaskTab,
    text="Can be built next to office buildings",
    font=("Arial", 12),
)
buildingsTaskGetMatrixForOfficeHeading.place(x=0, y=140)

buildingsTaskGetInputOfficeToResidential = CTkCheckBox(
    buildingsTaskTab, text="Residential", onvalue=1, offvalue=0
)
buildingsTaskGetInputOfficeToResidential.place(x=0, y=170)

buildingsTaskGetInputOfficeToIndustrial = CTkCheckBox(
    buildingsTaskTab, text="Industrial", onvalue=1, offvalue=0
)
buildingsTaskGetInputOfficeToIndustrial.place(x=110, y=170)

buildingsTaskGetInputOfficeToOffice = CTkCheckBox(
    buildingsTaskTab, text="Office", onvalue=1, offvalue=0
)
buildingsTaskGetInputOfficeToOffice.place(x=210, y=170)

buildingsTaskGetResultsHeading = CTkLabel(
    buildingsTaskTab,
    text="Enter the number of buildings you want to build",
    font=("Arial", 14, "bold"),
)
buildingsTaskGetResultsHeading.place(x=0, y=210)

buildingsTaskGetResultsInput = CTkEntry(
    buildingsTaskTab,
    placeholder_text="Number of Buildings...",
    width=180,
)
buildingsTaskGetResultsInput.place(x=0, y=240)

buildingsTaskGetResultsButton = CTkButton(
    buildingsTaskTab,
    text="Solve",
    width=60,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: buildingsTaskSolve(
        buildingsTaskGetInputResidentialToResidential.get(),
        buildingsTaskGetInputResidentialToIndustrial.get(),
        buildingsTaskGetInputResidentialToOffice.get(),
        buildingsTaskGetInputIndustrialToResidential.get(),
        buildingsTaskGetInputIndustrialToIndustrial.get(),
        buildingsTaskGetInputIndustrialToOffice.get(),
        buildingsTaskGetInputOfficeToResidential.get(),
        buildingsTaskGetInputOfficeToIndustrial.get(),
        buildingsTaskGetInputOfficeToOffice.get(),
        buildingsTaskGetResultsInput.get(),
    )
    if buildingsTaskGetResultsInput.get()
    else AlertPopup("Enter the number of buildings you want to build"),
)
buildingsTaskGetResultsButton.place(x=185, y=240)


#! BFS
class BFSGraph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def BFS(self, start):
        visited = []
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.append(vertex)
                queue.extend(set(self.graph[vertex]) - set(visited))

        return visited

    def getList(self):
        list = []
        for key, value in self.graph.items():
            chainString = (
                f"{key} 🔗 {', '.join(map(str, value))}"
                if not self.directed
                else f"{key} → {', '.join(map(str, value))}"
            )
            list.append(chainString)
        return list


graphTraversalTabsContainer = CTkTabview(
    graphTraversalTab,
)
graphTraversalTabsContainer.add("Breadth First Search")
graphTraversalTabsContainer.add("Depth First Search")
graphTraversalTabsContainer.add("Sum of Paths")
graphTraversalTabsContainer.add("Min number of Operations")
graphTraversalTabsContainer.add("Hampton Court Maze")
graphTraversalTabsContainer.pack(fill="both", expand=True)

bfsTab = graphTraversalTabsContainer.tab("Breadth First Search")
dfsTab = graphTraversalTabsContainer.tab("Depth First Search")
pathsSumTab = graphTraversalTabsContainer.tab("Sum of Paths")
operationsTab = graphTraversalTabsContainer.tab("Min number of Operations")
mazeTab = graphTraversalTabsContainer.tab("Hampton Court Maze")


def bfsDemoUpdateEdgesContainer():
    for widget in bfsEdgesContainer.winfo_children():
        widget.destroy()

    for edge in BFSGraphObject.getList():
        CTkLabel(
            bfsEdgesContainer,
            text=edge,
        ).pack(padx=5, anchor="w")


def bfsDemoLoadGraphEdges(fileName, isDirected):
    global BFSGraphObject
    BFSGraphObject = BFSGraph(isDirected)
    with open(fileName, "r") as file:
        for line in file:
            u, v = map(int, line.strip().split())
            BFSGraphObject.addEdge(u, v)
    bfsDemoUpdateEdgesContainer()


def bfsDemoStartBFS(sourceNode):
    if not BFSGraphObject:
        AlertPopup("Load graph edges first")
        return

    visited = BFSGraphObject.BFS(sourceNode)
    nodesList = ", ".join(map(str, visited))

    AlertPopup(
        f"BFS from node {sourceNode} visited {len(visited)} nodes\nFormed tree: {nodesList}"
    )


bfsEdgesContainer = CTkScrollableFrame(bfsTab, width=240, height=270)
bfsEdgesContainer.place(x=400, y=0)

bfsDemoLoadGraphEdgesHeading = CTkLabel(
    bfsTab,
    text="Load Graph Edges from File",
    font=("Arial", 14, "bold"),
)
bfsDemoLoadGraphEdgesHeading.place(x=0, y=0)

bfsDemoIsDirected = CTkCheckBox(
    bfsTab,
    text="Directed",
    onvalue=1,
    offvalue=0,
)
bfsDemoIsDirected.place(x=0, y=30)

bfsDemoFileNameInput = CTkEntry(
    bfsTab,
    placeholder_text="Graph edges file...",
    width=180,
)
bfsDemoFileNameInput.place(x=100, y=30)

bfsDemoLoadFileButton = CTkButton(
    bfsTab,
    text="Load",
    width=60,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: bfsDemoLoadGraphEdges(
        bfsDemoFileNameInput.get(), bfsDemoIsDirected.get()
    ),
)
bfsDemoLoadFileButton.place(x=285, y=30)

bfsDemoSetInitialNodeHeading = CTkLabel(
    bfsTab,
    text="Set Source Node",
    font=("Arial", 14, "bold"),
)
bfsDemoSetInitialNodeHeading.place(x=0, y=70)

bfsDemoSetInitialNodeInput = CTkEntry(
    bfsTab,
    placeholder_text="Source Node...",
    width=180,
)
bfsDemoSetInitialNodeInput.place(x=0, y=100)

bfsDemoSetInitialNodeButton = CTkButton(
    bfsTab,
    text="Set and Start BFS",
    width=100,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: bfsDemoStartBFS(int(bfsDemoSetInitialNodeInput.get()))
    if bfsDemoSetInitialNodeInput.get()
    and bfsDemoSetInitialNodeInput.get().isdigit()
    and int(bfsDemoSetInitialNodeInput.get()) in BFSGraphObject.graph
    else AlertPopup("Enter a valid source node"),
)
bfsDemoSetInitialNodeButton.place(x=185, y=100)

BFSGraphObject = None


#! DFS
class DFSGraph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def DFS(self, source):
        visited = []
        stack = [source]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                stack.extend(set(self.graph[vertex]) - set(visited))

        return visited

    def getList(self):
        list = []
        for key, value in self.graph.items():
            chainString = (
                f"{key} 🔗 {', '.join(map(str, value))}"
                if not self.directed
                else f"{key} → {', '.join(map(str, value))}"
            )
            list.append(chainString)
        return list


def dfsDemoUpdateEdgesContainer():
    for item in dfsEdgesContainer.winfo_children():
        item.destroy()

    for item in DFSGraphObject.getList():
        CTkLabel(
            dfsEdgesContainer,
            text=item,
        ).pack(padx=5, anchor="w")


def dfsDemoLoadGraphEdges(fileName, isDirected):
    global DFSGraphObject
    DFSGraphObject = DFSGraph(isDirected)
    with open(fileName, "r") as file:
        for line in file:
            u, v = map(int, line.strip().split())
            DFSGraphObject.addEdge(u, v)
    dfsDemoUpdateEdgesContainer()


def dfsDemoStartDFS(source):
    if not DFSGraphObject:
        AlertPopup("Load Graph Edges first")

    visited = DFSGraphObject.DFS(source)
    nodesList = ", ".join(map(str, visited))

    AlertPopup(
        f"DFS from node {source} visited {len(visited)} nodes\nFormed tree: {nodesList}"
    )


dfsEdgesContainer = CTkScrollableFrame(dfsTab, width=240, height=270)
dfsEdgesContainer.place(x=400, y=0)

dfsDemoLoadGraphEdgesHeading = CTkLabel(
    dfsTab,
    text="Load Graph Edges from File",
    font=("Arial", 14, "bold"),
)
dfsDemoLoadGraphEdgesHeading.place(x=0, y=0)

dfsDemoIsDirected = CTkCheckBox(
    dfsTab,
    text="Directed",
    onvalue=1,
    offvalue=0,
)
dfsDemoIsDirected.place(x=0, y=30)

dfsDemoFileNameInput = CTkEntry(
    dfsTab,
    placeholder_text="Graph edges file...",
    width=180,
)
dfsDemoFileNameInput.place(x=100, y=30)

dfsDemoLoadFileButton = CTkButton(
    dfsTab,
    text="Load",
    width=60,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: dfsDemoLoadGraphEdges(
        dfsDemoFileNameInput.get(), dfsDemoIsDirected.get()
    ),
)
dfsDemoLoadFileButton.place(x=285, y=30)

dfsDemoSetInitialNodeHeading = CTkLabel(
    dfsTab,
    text="Set Source Node",
    font=("Arial", 14, "bold"),
)
dfsDemoSetInitialNodeHeading.place(x=0, y=70)

dfsDemoSetInitialNodeInput = CTkEntry(
    dfsTab,
    placeholder_text="Source Node...",
    width=180,
)
dfsDemoSetInitialNodeInput.place(x=0, y=100)

dfsDemoSetInitialNodeButton = CTkButton(
    dfsTab,
    text="Set and Start DFS",
    width=100,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: dfsDemoStartDFS(int(dfsDemoSetInitialNodeInput.get()))
    if dfsDemoSetInitialNodeInput.get()
    and dfsDemoSetInitialNodeInput.get().isdigit()
    and int(dfsDemoSetInitialNodeInput.get()) in DFSGraphObject.graph
    else AlertPopup("Enter a valid source node"),
)
dfsDemoSetInitialNodeButton.place(x=185, y=100)

DFSGraphObject = None


#! SUM OF PATHS
class SumGraph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def findPaths(self, start, targetSum):
        visited = set()
        path = []
        result = []
        self._findPathsHelper(start, targetSum, visited, path, result)
        return result

    def _findPathsHelper(self, vertex, targetSum, visited, path, result):
        visited.add(vertex)
        path.append(vertex)

        if sum(path) == targetSum:
            result.append(" -> ".join(map(str, path)))

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._findPathsHelper(neighbor, targetSum, visited, path, result)

        path.pop()
        visited.remove(vertex)

    def getList(self):
        list = []
        for key, value in self.graph.items():
            chainString = (
                f"{key} 🔗 {', '.join(map(str, value))}"
                if not self.directed
                else f"{key} → {', '.join(map(str, value))}"
            )
            list.append(chainString)
        return list


def sumPathsTaskLoadGraphEdges(fileName, isDirected):
    global sumPathsTaskGraph
    sumPathsTaskGraph = SumGraph(isDirected)
    with open(fileName, "r") as file:
        for line in file:
            u, v = map(int, line.strip().split())
            sumPathsTaskGraph.addEdge(u, v)
    sumPathsTaskUpdateEdgesContainer()


def sumPathsTaskUpdateEdgesContainer():
    for widget in sumPathsTaskEdgesContainer.winfo_children():
        widget.destroy()

    for edge in sumPathsTaskGraph.getList():
        CTkLabel(
            sumPathsTaskEdgesContainer,
            text=edge,
        ).pack(padx=5, anchor="w")


def sumPathsTaskGetResults(source, targetSum):
    res = sumPathsTaskGraph.findPaths(source, targetSum)
    if res:
        pathsList = ""
        for path in res:
            pathsList += f"{path}\n"
        AlertPopup(f"Paths with sum {targetSum}:\n{pathsList}")
    else:
        AlertPopup(f"No paths with sum {targetSum} found")


sumPathsTaskEdgesContainer = CTkScrollableFrame(pathsSumTab, width=240, height=270)
sumPathsTaskEdgesContainer.place(x=400, y=0)

sumPathsTaskLoadGraphEdgesHeading = CTkLabel(
    pathsSumTab,
    text="Load Graph Edges from File",
    font=("Arial", 14, "bold"),
)
sumPathsTaskLoadGraphEdgesHeading.place(x=0, y=0)

sumPathsTaskIsDirected = CTkCheckBox(
    pathsSumTab,
    text="Directed",
    onvalue=1,
    offvalue=0,
)
sumPathsTaskIsDirected.place(x=0, y=30)

sumPathsTaskFileNameInput = CTkEntry(
    pathsSumTab,
    placeholder_text="Graph edges file...",
    width=180,
)
sumPathsTaskFileNameInput.place(x=100, y=30)

sumPathsTaskLoadFileButton = CTkButton(
    pathsSumTab,
    text="Load",
    width=60,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: sumPathsTaskLoadGraphEdges(
        sumPathsTaskFileNameInput.get(), sumPathsTaskIsDirected.get()
    ),
)
sumPathsTaskLoadFileButton.place(x=285, y=30)

sumPathsTaskSetInitialNodeHeading = CTkLabel(
    pathsSumTab,
    text="Set Source Node",
    font=("Arial", 14, "bold"),
)
sumPathsTaskSetInitialNodeHeading.place(x=0, y=70)

sumPathsTaskSetInitialNodeInput = CTkEntry(
    pathsSumTab,
    placeholder_text="Source Node...",
    width=300,
)
sumPathsTaskSetInitialNodeInput.place(x=0, y=100)

sumPathsTaskSetWantedSumHeading = CTkLabel(
    pathsSumTab,
    text="Set Wanted Sum",
    font=("Arial", 14, "bold"),
)
sumPathsTaskSetWantedSumHeading.place(x=0, y=140)

sumPathsTaskSetWantedSumInput = CTkEntry(
    pathsSumTab,
    placeholder_text="Wanted Sum...",
    width=300,
)
sumPathsTaskSetWantedSumInput.place(x=0, y=170)

sumPathsTaskGetResultsButton = CTkButton(
    pathsSumTab,
    text="Get Results",
    width=120,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: sumPathsTaskGetResults(
        int(sumPathsTaskSetInitialNodeInput.get()),
        int(sumPathsTaskSetWantedSumInput.get()),
    )
    if sumPathsTaskSetInitialNodeInput.get() and sumPathsTaskSetWantedSumInput.get()
    else AlertPopup("Fill in both fields"),
)
sumPathsTaskGetResultsButton.place(x=0, y=210)

SumPathsTaskGraphObject = None


#! MIN OPERATIONS
class MinOperationsGraph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def solveTask(self, a, b, operations):
        queue = deque([(a, [])])

        while queue:
            num, ops = queue.popleft()

            if num == b:
                return ops

            for op, operationString in operations:
                newNum = op(num)
                if newNum not in ops:
                    queue.append((newNum, ops + [operationString]))

        return None


def minOperationsTaskSolve(a, b):
    minOperationsTaskGraphObject = MinOperationsGraph()
    res = minOperationsTaskGraphObject.solveTask(a, b, minOperationsTaskOperationsList)
    if res:
        AlertPopup(
            f"Minimum number of operations to get from {a} to {b} is {len(res)}\nOperations: {', '.join(res)}"
        )
    else:
        AlertPopup("There is no way to get from {a} to {b}")


minOperationsTaskGetFirstNumberHeading = CTkLabel(
    operationsTab,
    text="Get First Number",
    font=("Arial", 14, "bold"),
)
minOperationsTaskGetFirstNumberHeading.place(x=0, y=0)

minOperationsTaskGetFirstNumberInput = CTkEntry(
    operationsTab,
    placeholder_text="First Number...",
    width=300,
)
minOperationsTaskGetFirstNumberInput.place(x=0, y=30)

minOperationsTaskGetFirstNumberHeading = CTkLabel(
    operationsTab,
    text="Get Second Number",
    font=("Arial", 14, "bold"),
)
minOperationsTaskGetFirstNumberHeading.place(x=0, y=70)

minOperationsTaskGetSecondNumberInput = CTkEntry(
    operationsTab,
    placeholder_text="Second Number...",
    width=300,
)
minOperationsTaskGetSecondNumberInput.place(x=0, y=100)

minOperationsTaskSolveButton = CTkButton(
    operationsTab,
    text="Solve",
    width=120,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: minOperationsTaskSolve(
        int(minOperationsTaskGetFirstNumberInput.get()),
        int(minOperationsTaskGetSecondNumberInput.get()),
    )
    if minOperationsTaskGetFirstNumberInput.get()
    and minOperationsTaskGetSecondNumberInput.get()
    else AlertPopup("Fill in both fields"),
)
minOperationsTaskSolveButton.place(x=0, y=140)

minOperationsTaskOperationsList = [
    (lambda x: x + 1, "+1"),
    (lambda x: x - 1, "-1"),
    (lambda x: x * 2, "*2"),
    (lambda x: x // 2, "/2"),
    (lambda x: x * 3, "*3"),
    (lambda x: x // 3, "/3"),
    (lambda x: x**2, "^2"),
    (lambda x: x**3, "^3"),
]


#! HAMPTON MAZE
class MazeGraph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def drawGraph(self):
        G = nx.Graph() if not self.directed else nx.DiGraph()

        for u, edges in self.graph.items():
            for v in edges:
                G.add_edge(u, v)

        nodeColors = [
            "red" if node == 1 else "lightgreen" if node == 0 else "lightgray"
            for node in G.nodes()
        ]
        nx.draw(G, with_labels=True, node_color=nodeColors, edge_color="gray")
        plt.show()

    def getList(self):
        list = []
        for key, value in self.graph.items():
            chainString = (
                f"{key} 🔗 {', '.join(map(str, value))}"
                if not self.directed
                else f"{key} → {', '.join(map(str, value))}"
            )
            list.append(chainString)
        return list


def mazeTaskUpdateElementsContainer():
    for widget in mazeTaskElementsContainer.winfo_children():
        widget.destroy()

    for edge in mazeTaskGraphObject.getList():
        CTkLabel(
            mazeTaskElementsContainer,
            text=edge,
        ).pack(padx=5, anchor="w")


def mazeTaskLoadGraphEdges(fileName, isDirected):
    global mazeTaskGraphObject
    mazeTaskGraphObject = MazeGraph(isDirected)
    with open(fileName, "r") as file:
        for line in file:
            u, v = map(int, line.strip().split())
            mazeTaskGraphObject.addEdge(u, v)
    mazeTaskUpdateElementsContainer()


def mazeTaskBuildGraph():
    if not mazeTaskGraphObject:
        AlertPopup("Load maze edges first")
        return

    mazeTaskGraphObject.drawGraph()


mazeTaskElementsContainer = CTkScrollableFrame(mazeTab, width=240, height=270)
mazeTaskElementsContainer.place(x=400, y=0)

mazeTaskLoadGraphEdgesHeading = CTkLabel(
    mazeTab,
    text="Load Maze Edges from File",
    font=("Arial", 14, "bold"),
)
mazeTaskLoadGraphEdgesHeading.place(x=0, y=0)

mazeTaskIsDirected = CTkCheckBox(
    mazeTab,
    text="Directed",
    onvalue=1,
    offvalue=0,
)
mazeTaskIsDirected.place(x=0, y=30)

mazeTaskFileNameInput = CTkEntry(
    mazeTab,
    placeholder_text="Maze edges file...",
    width=180,
)
mazeTaskFileNameInput.place(x=100, y=30)

mazeTaskLoadFileButton = CTkButton(
    mazeTab,
    text="Load",
    width=60,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: mazeTaskLoadGraphEdges(
        mazeTaskFileNameInput.get(), mazeTaskIsDirected.get()
    ),
)
mazeTaskLoadFileButton.place(x=285, y=30)

mazeTaskSolveTask = CTkButton(
    mazeTab,
    text="Visualize Maze",
    width=120,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: mazeTaskBuildGraph()
    if mazeTaskGraphObject
    else AlertPopup("Load maze edges first"),
)
mazeTaskSolveTask.place(x=0, y=70)

mazeTaskGraphObject = None

app.mainloop()
saveHeapOnExit()
saveLinkedListOnExit()
saveHashTableOnExit()
saveBTreeOnExit()
