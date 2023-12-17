from customtkinter import *
import time
import json
import heapq
import os
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict, deque
from rich import print
from rich.console import Console
from rich.traceback import install
from rich.markdown import Markdown as md

install()
console = Console()


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

# Container for all of our tabs
appTabsContainer = CTkTabview(app)
appTabsContainer.pack(expand=True, fill="both")

appTabsContainer.add("Heap")
appTabsContainer.add("Data Structures")
appTabsContainer.add("Greedy Algorithms")
appTabsContainer.add("Dynamic Programming")
appTabsContainer.add("Graph Traversal")
appTabsContainer.add("Graph Shortest Path")

tabHeap = appTabsContainer.tab("Heap")
tabDataStructures = appTabsContainer.tab("Data Structures")
tabGreedyAlgorithms = appTabsContainer.tab("Greedy Algorithms")
tabDynamicProgramming = appTabsContainer.tab("Dynamic Programming")
tabGraphTraversalAlgorithms = appTabsContainer.tab("Graph Traversal")
tabGraphShortestPathsAlgorithms = appTabsContainer.tab("Graph Shortest Path")


#! HEAP
class Heap:
    def __init__(self):
        # Our heap is stored as an array, but is reordered on insertion or deletion to maintain the heap property (see _heapifyUp and _heapifyDown)
        self.heap = []

    def insert(self, value):
        # Add the new element to the end of the heap
        self.heap.append(value)

        # Adjust new element's position to maintain the heap property
        # The last element of the heap is the new element, hence the index of length(heap)-1
        self._heapifyUp(givenIndex=len(self.heap) - 1)

    def delete(self):
        # Check if heap is empty, meaning there are no elements to delete
        if len(self.heap) == 0:
            return None

        # Swap the root with the last element
        # The root is always at the beginning of the heap, hence the index of 0
        self._swap(0, len(self.heap) - 1)

        # Get the root element by removing the last element, which we just swapped with the root
        root = self.heap.pop()

        # Adjust the position of our last element which is now in root
        self._heapifyDown(parentIndex=0)

        return root

    def sort(self):
        # For storing all our sorted items
        sortedItems = []

        # Run through the entire heap
        for _ in range(len(self.heap)):
            # Add the root element to the sorted items
            # Root because in MAX heap the root is always the biggest element
            sortedItems.append(self.delete())

        return sortedItems

    def buildHeap(self, arr):
        # Assigning the heap to our given array
        self.heap = arr

        # Starting from the middle of the heap because the last half is all the leaves
        # and we don't need to heapify leaves as their position is already correct
        start = len(arr) // 2

        # Run through our new heap from the middle to the first element in reversed order
        for i in reversed(range(start + 1)):
            # Adjust the position of each element
            self._heapifyDown(parentIndex=i)

        # Returning self to be able to chain methods
        return self

    def _heapifyUp(self, givenIndex):
        # Getting the index of the parent by formula
        parentIndex = (givenIndex - 1) // 2

        # Check if the parent node exists
        # and if the current value is greater than the parent's value
        if parentIndex >= 0 and self.heap[givenIndex] > self.heap[parentIndex]:
            # Swap the two elements
            self._swap(parentIndex, givenIndex)

            # Adjust the position of our new element further
            self._heapifyUp(givenIndex=parentIndex)

    def _heapifyDown(self, parentIndex):
        # All the indeces are calculated by the appropriate formula
        leftChildIndex = 2 * parentIndex + 1
        rightChildIndex = 2 * parentIndex + 2

        # Assume the parent to be the largest one
        largest = parentIndex

        # Check if the left child exists
        # and if its value is greater than the parent's
        if (
            leftChildIndex < len(self.heap)
            and self.heap[leftChildIndex] > self.heap[largest]
        ):
            # Reassign largest value to be this child
            largest = leftChildIndex

        # Check if the right child exists
        # and its value is greater then the current largest
        # And the current largest can now be either the parent or the left child
        if (
            rightChildIndex < len(self.heap)
            and self.heap[rightChildIndex] > self.heap[largest]
        ):
            # Reassign largest value to be this child
            largest = rightChildIndex

        # Check if the parent is not the largest one anymore
        if largest != parentIndex:
            # Swap the parent with the largest
            # So the parent of this subtree is now the largest element
            # and the previous parent is now at the position where the largest element was
            self._swap(parentIndex, largest)

            # Adjust the position of our previous parent further
            self._heapifyDown(parentIndex=largest)

    def _swap(self, i, j):
        # Just swap the values at indices i and j in the heap list
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def updateHeapElementsContainer():
    # Run through each possible UI element in the elements container
    for widget in heapElementsContainer.winfo_children():
        # And destroy it
        widget.destroy()

    # Run through each heap node
    for heapNode in heapElements.heap:
        # And add it to the elements container
        CTkLabel(heapElementsContainer, text=heapNode).pack(padx=5, anchor="w")


def addHeapElement(element):
    # Insert our given element into the heap
    heapElements.insert(element)

    # And update the elements container
    updateHeapElementsContainer()


def deleteHeapElement():
    # Delete the root element
    heapElements.delete()

    # And update the elements container
    updateHeapElementsContainer()


def quickSortUtil(arr):
    # Get the length of our given array
    n = len(arr)

    # See if there are 1 or 0 elements in it
    if n < 2:
        # If so just return it, since it's already sorted
        # This is our base case for the recursion
        return arr

    # Choose the pivot element to be the middle one
    pivot = arr[n // 2]

    # Get all the elements that are less than the pivot
    # using list comprehension
    less = [x for x in arr if x < pivot]

    # Get all the elements that are equal to the pivot
    equal = [x for x in arr if x == pivot]

    # Get all the elements that are greater than the pivot
    more = [x for x in arr if x > pivot]

    # Recursively sort the lesser elements, combined with equal element, and the greater elements
    return quickSortUtil(more) + equal + quickSortUtil(less)


def sortHeap(sortingType: str):
    # Start the timer to measure the sorting time
    startTimer = time.time()

    # Perform the appropriate sorting type based on the recieved parameter
    heapElements.heap = (
        heapElements.sort()
        if sortingType == "Heap Sort"
        else quickSortUtil(heapElements.heap)
        if sortingType == "Quick Sort"
        else sorted(heapElements.heap, reverse=True)
    )

    # Wait for 100ms to let the user see the sorting time
    # Without it the results will always be 0 for some reason
    time.sleep(0.1)

    # Calculate the sorting time by stopping the timer and subtracting it from the start
    sortingTime = time.time() - startTimer

    # Update the heap elements to reflect the sorting
    updateHeapElementsContainer()

    # Show the sorting time alert
    AlertPopup(
        f"Sorting took {sortingTime:.2f} seconds or {sortingTime*1000:.2f} milliseconds"
    )


def saveHeapOnExit():
    # If the heap is empty there is nothing to save
    if len(heapElements.heap) == 0:
        # So we just exit out of the function
        return

    # Open the heap file in write mode
    with open("heap.json", "w") as file:
        # And write the heap into it
        json.dump(heapElements.heap, file)


def loadHeapOnStart():
    try:
        # Open the heap file in read mode
        with open("heap.json", "r") as file:
            # Load the heap from the file into the temporary array
            heapArray = json.load(file)
            # And build the heap from it
            heapElements.buildHeap(arr=heapArray)

            # Update the elements container to reflect the loaded heap
            updateHeapElementsContainer()
    except:
        # Show an alert popup if the heap fails to load
        AlertPopup("Failed to load heap")


tabHeap_SubTabsContainer = CTkTabview(tabHeap)
tabHeap_SubTabsContainer.add("Heap")
tabHeap_SubTabsContainer.add("Linked List")
tabHeap_SubTabsContainer.add("Task")
tabHeap_SubTabsContainer.pack(fill="both", expand=True)

subtabHeap = tabHeap_SubTabsContainer.tab("Heap")
subtabLinkedList = tabHeap_SubTabsContainer.tab("Linked List")
subtabHeapTask = tabHeap_SubTabsContainer.tab("Task")

heapElementsContainer = CTkScrollableFrame(subtabHeap, width=240, height=270)
heapElementsContainer.place(x=400, y=0)

linkedListElementsContainer = CTkScrollableFrame(
    subtabLinkedList, width=240, height=270
)
linkedListElementsContainer.place(x=400, y=0)

heapTaskElementsContainer = CTkScrollableFrame(subtabHeapTask, width=240, height=270)
heapTaskElementsContainer.place(x=400, y=0)


addHeapElementHeading = CTkLabel(
    subtabHeap, text="Add to Heap", font=("Arial", 14, "bold")
)
addHeapElementHeading.place(x=0, y=0)

addHeapElementInput = CTkEntry(
    subtabHeap, placeholder_text="Enter element...", width=300
)
addHeapElementInput.place(x=0, y=30)

addHeapElementButton = CTkButton(
    subtabHeap,
    text="Add",
    command=lambda: addHeapElement(int(addHeapElementInput.get()))
    if addHeapElementInput.get()
    else AlertPopup("Please enter an element to add"),
    width=60,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
)
addHeapElementButton.place(x=305, y=30)

sortHeapHeading = CTkLabel(subtabHeap, text="Sort Heap", font=("Arial", 14, "bold"))
sortHeapHeading.place(x=0, y=70)

sortHeapButton_DefaultSort = CTkButton(
    subtabHeap,
    text="Default Sort",
    command=lambda: sortHeap("Default Sort")
    if len(heapElements.heap) > 0
    else AlertPopup("Heap is empty, so there is nothing to sort"),
    width=60,
    text_color="white",
    font=("Arial", 12, "bold"),
    fg_color="#8F00FF",
    hover_color="#7500D1",
)
sortHeapButton_DefaultSort.place(x=0, y=100)

sortHeapButton_QuickSort = CTkButton(
    subtabHeap,
    text="Quick Sort",
    command=lambda: sortHeap("Quick Sort")
    if len(heapElements.heap) > 0
    else AlertPopup("Heap is empty, so there is nothing to sort"),
    width=60,
    text_color="white",
    font=("Arial", 12, "bold"),
    fg_color="#8F00FF",
    hover_color="#7500D1",
)
sortHeapButton_QuickSort.place(x=90, y=100)

sortHeapButton_HeapSort = CTkButton(
    subtabHeap,
    text="Heap Sort",
    command=lambda: sortHeap("Heap Sort")
    if len(heapElements.heap) > 0
    else AlertPopup("Heap is empty, so there is nothing to sort"),
    width=60,
    text_color="white",
    font=("Arial", 12, "bold"),
    fg_color="#8F00FF",
    hover_color="#7500D1",
)
sortHeapButton_HeapSort.place(x=170, y=100)

deleteFromHeapHeading = CTkLabel(
    subtabHeap, text="Delete from Heap", font=("Arial", 14, "bold")
)
deleteFromHeapHeading.place(x=0, y=140)

deleteFromHeapButton = CTkButton(
    subtabHeap,
    text="Delete Element",
    command=lambda: deleteHeapElement()
    if len(heapElements.heap) > 0
    else AlertPopup("Heap is already empty"),
    width=120,
    fg_color="#BF181D",
    hover_color="#961316",
    text_color="white",
    font=("Arial", 12, "bold"),
)
deleteFromHeapButton.place(x=0, y=170)

heapElements = Heap()
loadHeapOnStart()


#! DOUBLY LINKED LIST
class DoublyLinkedList:
    class LinkedListNode:
        def __init__(self, data=None):
            # Since its a doubly linked list, we have a pointer to previous and next nodes
            # And also the data, of course
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        # Our class will hold only the head pointer
        self.head = None

    def append(self, data):
        # Check if the linked list is empty
        if self.head is None:
            # If so, create a new node and set it as the head
            self.head = self.LinkedListNode(data)

        else:
            # Create a temporary node to traverse the linked list
            # And set it to the head, since the list is not empty, we know it
            currentNode = self.head

            # Traverse the entire linked list until our node doesn't have a next pointer
            # Which means that there are no nodes after it
            while currentNode.next is not None:
                currentNode = currentNode.next

            # Declare our new node object with the given data we recieved as a parameter
            newNode = self.LinkedListNode(data)

            # Set our last node's next pointer to our new node
            currentNode.next = newNode

            # And set our new node's previous pointer to our last node
            # Thus linking them together and making our new node a part of the list
            newNode.prev = currentNode

    def search(self, data) -> bool:
        # Set the temporary node to the head
        # It will be used to traverse the list
        currentNode = self.head

        # Traverse the entire list until we find our node
        while currentNode is not None:
            # Check if our node has the data we're looking for
            # And this is pretty much the standard linear search that we can apply to the regular array as well. But as linked list doesn't allow index accessing, we cannot use Binary Search on it
            if currentNode.data == data:
                # If we found the node we're looking for, we return True
                return True
            # Otherwise, we move to the next node
            currentNode = currentNode.next

        # If we exited out of the loop without finding our node, we return False
        # Since we obviously haven't found the node we were looking for, which means it is not in the list
        return False

    def delete(self, data) -> bool:
        # Set our temporary node to the head
        # Will be used for traversing the list, once again
        currentNode = self.head

        # Traverse the entire linked list
        while currentNode is not None:
            # Check if we found our node that holds the data we need to delete
            if currentNode.data == data:
                # Check if there are nodes before the node we want to delete
                if currentNode.prev is not None:
                    # If so, set our previous node's next pointer to our next node
                    # Meaning to the node that is after our node we want to delete
                    currentNode.prev.next = currentNode.next

                # Check if there are nodes after the node we want to delete
                if currentNode.next is not None:
                    # If so, set our next node's previous pointer to our previous node
                    currentNode.next.prev = currentNode.prev

                # Check if the node we want to delete is the head
                if currentNode == self.head:
                    # If so, set the next node to be the head
                    self.head = currentNode.next

                # And return true to indicate we found and deleted the node
                return True

            # Otherwise, we move to the next node
            currentNode = currentNode.next

        # If we haven't found and deleted our node, we return false
        return False

    def getList(self):
        # Declare the list of nodes
        list = []

        # Set our current temporaray node to the head
        currentNode = self.head

        # Start traversing the list until we reach the end
        while currentNode is not None:
            # And append all the nodes to the list
            list.append(currentNode.data)

            # Move to the next node
            currentNode = currentNode.next

        # Return the retrieved list of nodes
        return list

    def buildList(self, inputList):
        # Given a list of nodes, build the linked list

        # By traversing the given list
        for element in inputList:
            # And appending each node to our linked list
            self.append(element)


def updateLinkedListElementsContainer():
    # For each existing UI element in the elements container
    for widget in linkedListElementsContainer.winfo_children():
        # Delete it
        widget.destroy()

    # Run through each node in the linked list
    for node in linkedListElements.getList():
        # And append it to the container
        CTkLabel(linkedListElementsContainer, text=node).pack(padx=5, anchor="w")


def addLinkedListNode(data):
    # Check if the given element already exists in the linked list
    if linkedListElements.search(data):
        # If so, we cannot add it again
        # And we display an alert warning the user
        AlertPopup(f"{data} already exists in linked list")

        # Exiting out of the function afterwards
        return

    # Otherwise, we can add it to the list
    linkedListElements.append(data)

    # And update the container that displays the linked list elements
    updateLinkedListElementsContainer()


def deleteLinkedListNode(data):
    # Check if the given element doesn't exist in the linked list
    if not linkedListElements.delete(data):
        # If so, we cannot delete it
        # So warn the user about it by showing the alert
        AlertPopup(f"{data} is NOT found in a list")

        # Exiting out of the function afterwards
        return

    # Otherwise, we can delete it from the list
    # And update the container that displays the linked list elements
    updateLinkedListElementsContainer()


def searchLinkedListNode(data):
    # Simply perform a search for a given node
    if linkedListElements.search(data):
        # And if its found
        # Display an alert informing the user
        AlertPopup(f"{data} is found in a list")
    else:
        # Otherwise, display an alert informing the user that the node was not found
        AlertPopup(f"{data} is NOT found in a list")


def saveLinkedListOnExit():
    # Check if the linked list is empty
    if len(linkedListElements.getList()) == 0:
        # If so, we cannot save anything to the file
        # So we exit out of the function
        return

    # Otherwise, open the local file and write the list to it
    with open("linkedList.json", "w") as f:
        # By using the JSON module and the appropriate function
        json.dump(linkedListElements.getList(), f)


def loadLinkedListOnStart():
    try:
        # Open the local file that should contain the linked list
        with open("linkedList.json", "r") as f:
            # Load the list from the file
            list = json.load(f)
            # And build a new linked list
            linkedListElements.buildList(list)

            # Update the container that displays the linked list elements
            updateLinkedListElementsContainer()
    except:
        # If we can't find the file or any other error occurs
        # We display an alert informing the user
        AlertPopup("Failed to load Linked List data")


addLinkedListNodeHeading = CTkLabel(
    subtabLinkedList, text="Add Linked List Node", font=("Arial", 14, "bold")
)
addLinkedListNodeHeading.place(x=0, y=0)

addLinkedListNodeInput = CTkEntry(
    subtabLinkedList, placeholder_text="Node value...", width=300
)
addLinkedListNodeInput.place(x=0, y=30)

addLinkedListNodeButton = CTkButton(
    subtabLinkedList,
    text="Add",
    command=lambda: addLinkedListNode(int(addLinkedListNodeInput.get()))
    if addLinkedListNodeInput.get()
    else AlertPopup("Please enter the value to add"),
    width=45,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
)
addLinkedListNodeButton.place(x=305, y=30)

deleteHeapNodeHeading = CTkLabel(
    subtabLinkedList, text="Delete Linked List Node", font=("Arial", 14, "bold")
)
deleteHeapNodeHeading.place(x=0, y=70)

deleteLinkedListNodeInput = CTkEntry(
    subtabLinkedList, placeholder_text="Node...", width=300
)
deleteLinkedListNodeInput.place(x=0, y=100)

deleteLinkedListNodeButton = CTkButton(
    subtabLinkedList,
    text="Delete",
    command=lambda: deleteLinkedListNode(int(deleteLinkedListNodeInput.get()))
    if deleteLinkedListNodeInput.get()
    else AlertPopup("Please enter the value to delete"),
    width=45,
    fg_color="#D32F2F",
    hover_color="#B71C1C",
    text_color="white",
    font=("Arial", 12, "bold"),
)
deleteLinkedListNodeButton.place(x=305, y=100)

searchLinkedListNodeHeading = CTkLabel(
    subtabLinkedList, text="Search Linked List Node", font=("Arial", 14, "bold")
)
searchLinkedListNodeHeading.place(x=0, y=140)

searchLinkedListNodeInput = CTkEntry(
    subtabLinkedList, placeholder_text="Node...", width=300
)
searchLinkedListNodeInput.place(x=0, y=170)

searchLinkedListNodeButton = CTkButton(
    subtabLinkedList,
    text="Search",
    command=lambda: searchLinkedListNode(int(searchLinkedListNodeInput.get()))
    if searchLinkedListNodeInput.get()
    else AlertPopup("Please enter the value to search for"),
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
    # For every UI element in the elements container
    for widget in heapTaskElementsContainer.winfo_children():
        # Delete it, clearing the container
        widget.destroy()

    # Run through each employee
    for employee in heapTaskEmployeesData:
        # And add it to the elements container
        CTkLabel(
            heapTaskElementsContainer,
            text=f"{employee['name']} - {employee['disease']}",
        ).pack(padx=5, anchor="w")


def heapTaskLoadEmployeesData(filename: str):
    try:
        # Open the local file that should contain the employees' data
        with open(filename, "r", encoding="utf-8") as file:
            # Load the data from the file into the temporaray list
            data = json.load(file)

        global heapTaskEmployeesData
        # And assign it to the global list
        heapTaskEmployeesData = data["employees"]
    except:
        # If we can't find the file or any other error occurs
        # We display an alert informing the user
        AlertPopup(f"Failed to load data from {filename}")

    # Otherwise we update the elements container
    updateHeapTaskElementsContainer()


def heapTaskShowResults():
    def countDiseaseCases():
        # A dictionary for keeping track of the occurences of each disease
        diseasesCount = dict()

        # Run through each employee in the data list
        for employee in heapTaskEmployeesData:
            # Check if the disease is not yet in the dictionary
            if employee["disease"] not in diseasesCount:
                # If so, add it with a count of 1, since we just encrounced it
                diseasesCount[employee["disease"]] = 1
            else:
                # If we've encountered the disease before
                # Just increment the count
                diseasesCount[employee["disease"]] += 1

        return diseasesCount

    def sortDiseasesList(arr):
        # Check if the list is empty
        if len(arr) == 0:
            # Just return an empty list
            return arr

        # Otherwise we sort the list by using Heap sort
        sortedArr = Heap().buildHeap(arr).sort()

        # And return it
        return sortedArr

    # Count the occurences of each disease
    diseasesCount = countDiseaseCases()

    # Form a list of the diseases and their occurences
    diseasesCountList = [
        (occurences, name) for name, occurences in diseasesCount.items()
    ]

    # Sort the list by occurences
    diseasesCountList = sortDiseasesList(diseasesCountList)

    # And forming the output message
    resultsString = f"Employees' Diseases sorted by Occurences:\n"

    # By running through each disease in the list
    for occurence, name in diseasesCountList:
        # And adding its name as well as the number of occurences
        currentDisease = f"{name}: {occurence} times\n"

        # To the resulting string
        resultsString += currentDisease

    # Show the results as a popup message
    AlertPopup(resultsString)


heapTaskLoadEmployeesDataHeading = CTkLabel(
    subtabHeapTask, text="Load employees JSON file", font=("Arial", 14, "bold")
)
heapTaskLoadEmployeesDataHeading.place(x=0, y=0)

heapTaskLoadEmployeesDataInput = CTkEntry(
    subtabHeapTask, placeholder_text="Filename...", width=140
)
heapTaskLoadEmployeesDataInput.place(x=0, y=30)

heapTaskLoadEmployeesDataButton = CTkButton(
    subtabHeapTask,
    text="Load",
    width=60,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: heapTaskLoadEmployeesData(heapTaskLoadEmployeesDataInput.get())
    if heapTaskLoadEmployeesDataInput.get()
    else AlertPopup("Please enter the filename to load data from"),
)
heapTaskLoadEmployeesDataButton.place(x=150, y=30)

heapTaskShowResultsButton = CTkButton(
    subtabHeapTask,
    text="Show Results",
    width=120,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: heapTaskShowResults()
    if len(heapTaskEmployeesData) > 0
    else AlertPopup("Please load employees data first"),
)
heapTaskShowResultsButton.place(x=220, y=30)

heapTaskEmployeesData = []


#! HASH TABLE
class HashTable:
    def __init__(self, size=15):
        # Set the initial size of our hash table to the given one
        # Or to the default value of 15 if none is given
        self.size = size

        # Declare our hash table as a list of lists
        # We declare a list of lists to handle any possible collisions
        # And we don't use a linked list because a Python array is easier to search through and use in general
        self.table = [[] for _ in range(self.size)]

    def hash(self, key):
        # Given a key, we compute its hash value
        # We use the Golden Ratio to improve the distribution of our hash values
        # And we multiply it by the size of our hash table
        return int((key * ((5**0.5 - 1) / 2) % 1) * self.size)

    def insert(self, key, value):
        # When inserting a new key-value pair, we first compute the hashed key, and then insert our pair into the corresponding position, which is a list in our case
        self.table[self.hash(key)].append((key, value))

    def delete(self, key):
        # When deleting we need to access the corresponding chain that the key is in
        # We do that by computing key's hash and accessing the corresponding list from our hash table
        chain = self.table[self.hash(key)]

        # Run through each key-value pair in the chain
        for index, keyValuePair in enumerate(chain):
            # And check if the key matches with the given one
            if keyValuePair[0] == key:
                # If it does, we delete our pair from the chain
                del chain[index]
                # And we return True to indicate that the key was found and deleted
                return True

        # If we exit out of the loop without returning, then the key was not found nor deleted
        # Which we indicate by returning False
        return False

    def search(self, key):
        # When searching for a key we first compute its hash value
        # And then access the chain that the key is in
        chain = self.table[self.hash(key)]

        # Run through the entire chain
        for keyValuePair in chain:
            # And see if the key matches
            if keyValuePair[0] == key:
                # If it does, we return True to indicate that the key was found
                return True

        # If we exit without returning, the key was never found
        # Which we indicate by returning False
        return False


def updateHashTableElementsContainer():
    # For each UI element in the elements container
    for widget in hashTableElementsContainer.winfo_children():
        # Delete it
        widget.destroy()

    # Run through each pair of keys and their corresponding values in the elements list
    for pair in hashTableElementsList:
        # Compute the key and value from the pair, since they are stored in the list as "key value" strings
        key, value = pair.split(" ")

        # And add it to the elements container
        CTkLabel(hashTableElementsContainer, text=f"{key} - {value}").pack(
            padx=5, anchor="w"
        )


def addHashTableElement(keyValuePair):
    # Add the given key-value pair into our local list
    hashTableElementsList.append(keyValuePair)

    # Split them into key and value variables
    key, value = keyValuePair.split(" ")
    # Calculate the key's hash value
    key = sum(ord(c) for c in key)

    # And insert it into our hash table
    hashTableElements.insert(key, value)

    # Update the elements container to show the new element
    updateHashTableElementsContainer()


def deleteHashTableKey(key):
    # We first form a list of all keys in our hash table
    # By taking each key-value pair in the local elements list, and extracting the key from it by splitting it and taking the first element
    keysList = [keyValuePair.split(" ")[0] for keyValuePair in hashTableElementsList]

    # Then checking if the given key is not in that list
    if key not in keysList:
        # If so, we alert the user
        AlertPopup(f"{key} is not in the dictionary")

        # And exit out of the function immediately as further processing is not needed
        return

    # If we are still here, we first remove the key-value pair from our local list
    # By running through each pair of keys and their corresponding values
    for el in hashTableElementsList:
        # And checking if the key matches
        if el.split(" ")[0] == key:
            # If it does, we remove it from the list
            hashTableElementsList.remove(el)
            # And we break out of the loop
            break

    # Next we delete the key from our hash table
    # By first converting the key to an integer of its ASCII values
    convertedKey = sum(ord(c) for c in key)

    # And then deleting it from our hash table
    _ = hashTableElements.delete(convertedKey)

    # Then updating the elements container to reflect the changes
    updateHashTableElementsContainer()


def searchHashTableKey(key):
    # We first convert our given key to an integer of its ASCII values
    convertedKey = sum(ord(c) for c in key)

    # Then run a search for it
    res = hashTableElements.search(convertedKey)

    # And output the result to the user via an alert
    AlertPopup(f"{key} is in the dictionary") if res else AlertPopup(
        f"{key} is NOT in the dictionary"
    )


def saveHashTableOnExit():
    # We check if our local list is empty
    if len(hashTableElementsList) == 0:
        # Then we just exit out of the function, as there is nothing to save
        return

    # Open the local file in write mode
    with open("hashTable.json", "w") as f:
        # And write our local list to it in JSON format
        json.dump(hashTableElementsList, f)


def loadHashTableOnStart():
    try:
        # Open the local file in read mode
        with open("hashTable.json", "r") as f:
            # Load our list of key-value pairs from it into a temporaray variable
            res = json.load(f)

            # For each key-value pair in the temporary variable
            for pair in res:
                # We add it into the hash table
                addHashTableElement(pair)
    except:
        # If we fail to load the file, we alert the user
        AlertPopup("Failed to load Hash Table data")


tabDataStructures_SubTabsContainer = CTkTabview(
    tabDataStructures, width=210, height=290
)
tabDataStructures_SubTabsContainer.add("Hash Table")
tabDataStructures_SubTabsContainer.add("B-Tree")
tabDataStructures_SubTabsContainer.add("Employees Search")
tabDataStructures_SubTabsContainer.add("Subscribers Search")
tabDataStructures_SubTabsContainer.pack(fill="both", expand=True)

subtabHashTable = tabDataStructures_SubTabsContainer.tab("Hash Table")
subtabBTree = tabDataStructures_SubTabsContainer.tab("B-Tree")
subtabBTreeTask = tabDataStructures_SubTabsContainer.tab("Subscribers Search")
subtabHashTableTask = tabDataStructures_SubTabsContainer.tab("Employees Search")

hashTableElementsContainer = CTkScrollableFrame(subtabHashTable, width=240, height=270)
hashTableElementsContainer.place(x=400, y=0)

bTreeElementsContainer = CTkScrollableFrame(subtabBTree, width=240, height=270)
bTreeElementsContainer.place(x=400, y=0)

hashTaskElementsContainer = CTkScrollableFrame(
    subtabHashTableTask, width=240, height=270
)
hashTaskElementsContainer.place(x=400, y=0)

bTreeTaskElementsContainer = CTkScrollableFrame(subtabBTreeTask, width=240, height=270)
bTreeTaskElementsContainer.place(x=400, y=0)


addHashTableElementHeading = CTkLabel(
    subtabHashTable, text="Add Key-Value Pair", font=("Arial", 14, "bold")
)
addHashTableElementHeading.place(x=0, y=0)

addHashTableElementInput = CTkEntry(
    subtabHashTable, placeholder_text="Key & Val...", width=300
)
addHashTableElementInput.place(x=0, y=30)

addHashTableElementButton = CTkButton(
    subtabHashTable,
    text="Add",
    width=45,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: addHashTableElement(addHashTableElementInput.get())
    if addHashTableElementInput.get()
    else AlertPopup("Please enter key and value to add"),
)
addHashTableElementButton.place(x=305, y=30)

deleteHashTableElementHeading = CTkLabel(
    subtabHashTable, text="Delete Hash Table Key", font=("Arial", 14, "bold")
)
deleteHashTableElementHeading.place(x=0, y=70)

deleteHashTableElementInput = CTkEntry(
    subtabHashTable, placeholder_text="Key...", width=300
)
deleteHashTableElementInput.place(x=0, y=100)

deleteHashTableElementButton = CTkButton(
    subtabHashTable,
    text="Delete",
    width=45,
    fg_color="#D32F2F",
    hover_color="#B71C1C",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: deleteHashTableKey(deleteHashTableElementInput.get())
    if deleteHashTableElementInput.get()
    else AlertPopup("Please enter key to delete"),
)
deleteHashTableElementButton.place(x=305, y=100)

searchHashTableElementHeading = CTkLabel(
    subtabHashTable, text="Search Hash Table Key", font=("Arial", 14, "bold")
)
searchHashTableElementHeading.place(x=0, y=140)

searchHashTableElementInput = CTkEntry(
    subtabHashTable, placeholder_text="Key...", width=300
)
searchHashTableElementInput.place(x=0, y=170)

searchHashTableElementButton = CTkButton(
    subtabHashTable,
    text="Search",
    width=45,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: searchHashTableKey(searchHashTableElementInput.get())
    if searchHashTableElementInput.get()
    else AlertPopup("Please enter key to search"),
)
searchHashTableElementButton.place(x=305, y=170)

hashTableElementsList = []
hashTableElements = HashTable()
loadHashTableOnStart()


#! B-TREE
class BTreeNode:
    def __init__(self, leaf=True):
        # For keeping track of whether the node is a leaf or not, meaning whether it has children or not
        # By default it is a leaf, hence the empty children list initialization
        self.leaf = leaf
        # In the B-Tree we need to have a list of keys
        self.keys = []
        # and a list of children nodes
        self.children = []


class BTree:
    def __init__(self, t=3):
        # In the B-Tree class we need to keep track of our root node and the degree of the tree
        self.root = BTreeNode()
        # Which is set to 3 by default if no value is passed
        self.t = t

    def search(self, key, currentNode=None):
        # We first set our current node to be the root if not provided, or the value passed
        currentNode = currentNode or self.root
        # and declare an index variable for traversing the list of keys
        index = 0

        # Traverse the list of keys either until it reaches the end or we find a key that is greater than or equal to the provided key
        while index < len(currentNode.keys) and key > currentNode.keys[index]:
            index += 1

        # If we found the key we want, return True
        if index < len(currentNode.keys) and key == currentNode.keys[index]:
            return True

        # If the current node is a leaf, return False as the key will not be found
        elif currentNode.leaf:
            return False

        # Else recursively call the search function on the child node at the current index
        else:
            return self.search(key, currentNode.children[index])

    def insert(self, key):
        # Start by assigning the root node to a variable for convenience
        root = self.root

        # Check if the root node is full
        # If it is, we need to create a new root node
        if len(root.keys) == (2 * self.t) - 1:
            # Create a new root node with the leaf set to False, as we immediately have children for it
            newRoot = BTreeNode(leaf=False)

            # Append the current root node as the first child of the new root
            newRoot.children.append(self.root)

            # Split the first and only child of the new root
            self._splitChild(newRoot, 0)

            # Set the global root to be the new root node
            self.root = newRoot

            # And insert the key into the new root node (which is not full and has only one child)
            self._insertNotFull(newRoot, key)
        else:
            # Else we simply insert the key into the root node
            self._insertNotFull(root, key)

    def _insertNotFull(self, currentNode, key):
        # Set index to the position where the key should be inserted
        index = len(currentNode.keys) - 1

        if currentNode.leaf:
            # If the node is a leaf, we insert a temporary zero to make space for our key
            currentNode.keys.append(0)

            # Then traverse the list of keys and shift all greater keys to the right
            while index >= 0 and key < currentNode.keys[index]:
                # Set the key at the current index to be the key at the next index
                currentNode.keys[index + 1] = currentNode.keys[index]
                # Move further to the left
                index -= 1
            # After choosing the correct position, insert the key
            currentNode.keys[index + 1] = key
        else:
            # If the node is not a leaf, but an internal node instead
            # We find the position where the key should be inserted
            while index >= 0 and key < currentNode.keys[index]:
                index -= 1
            index += 1

            # Check if the current child is full
            if len(currentNode.children[index].keys) == (2 * self.t) - 1:
                # If so, split it
                self._splitChild(currentNode, index)
                # Adjust the index if the new key is greater than the current key
                if key > currentNode.keys[index]:
                    index += 1

            # Recursively call to continue to process until the leaf node is reached
            self._insertNotFull(currentNode.children[index], key)

    def _splitChild(self, parent, index):
        # Get the degree of our tree for convenience
        t = self.t

        # Get the child node to be split
        child = parent.children[index]

        # Create a new node for the child
        newNode = BTreeNode(leaf=child.leaf)

        # Insert the new node into the parent node
        parent.children.insert(index + 1, newNode)

        # Insert the middle key of the child node into the parent node
        parent.keys.insert(index, child.keys[t - 1])

        # Assign keys to the right of the middle key to the new node
        newNode.keys = child.keys[t:]

        # Retain the keys to the left of the middle key in the original node
        child.keys = child.keys[: t - 1]

        if not child.leaf:
            # If the child node is not a leaf, redistribute the children across the new node and the original child node
            newNode.children = child.children[t:]
            child.children = child.children[:t]

    def delete(self, key):
        # Get the root node
        root = self.root

        # Delete teh key from the tree
        self._delete(root, key)

        if len(root.keys) == 0 and not root.leaf:
            # If the root is empty and is not a leaf
            # Replace the root with its first child
            self.root = root.children[0]

    def _delete(self, parent, key):
        # Get the degree of our tree for convenience
        t = self.t

        # Set the index to traverse the keys in the parent node
        index = 0

        # Find the position in the parent node where the key should be
        while index < len(parent.keys) and key > parent.keys[index]:
            index += 1

        if parent.leaf:
            # If the parent node is a leaf node
            # Check if the key is found in the parent node
            if index < len(parent.keys) and key == parent.keys[index]:
                # Remove it, if found
                parent.keys.pop(index)
            else:
                # Otherwise, show an error message
                AlertPopup(f"Key {key} was not found")

        else:
            if index < len(parent.keys) and key == parent.keys[index]:
                # If the key is found in the parent node
                # Delete it from the internal node
                self._deleteInternalNode(parent, index)

            else:
                if len(parent.children[index].keys) >= t:
                    # If the child node has enough keys, recursively delete the key from that child node
                    self._delete(parent.children[index], key)
                else:
                    if index > 0 and len(parent.children[index - 1].keys) >= t:
                        # If the previous sibling has enough keys, borrow a key from it
                        self._borrowFromPrevious(parent, index)
                    elif (
                        index < len(parent.children) - 1
                        and len(parent.children[index + 1].keys) >= t
                    ):
                        # Else check if the next sibling has enough keys, borrow a key from it
                        self._borrowFromNext(parent, index)
                    else:
                        # And if neither borrowing is an option
                        # Merge the current child node with its adjacent sibling
                        self._merge(parent, index)
                        # And continue the deletion process in the merged child node
                        self._delete(parent.children[index], key)

    def _deleteInternalNode(self, parent, index):
        # Get the degree of our tree for convenience
        t = self.t
        # Get the key of the parent node at the given index
        key = parent.keys[index]

        # Check if the child at given index has enough keys to borrow from
        if len(parent.children[index].keys) >= t:
            # Get the predecessor key from it
            predecessor = self._getPredecessor(parent.children[index])

            # Replace the key at the given index with the predecessor key
            parent.keys[index] = predecessor

            # Delete the predecessor key from the left child
            self._delete(parent.children[index], predecessor)

        # Check if the parent's right child has enough keys to borrow from
        elif len(parent.children[index + 1].keys) >= t:
            # Get the successor key from it
            successor = self._getSuccessor(parent.children[index + 1])

            # Replace the key at the given index with the successor key
            parent.keys[index] = successor

            # Delete the successor key from the right child
            self._delete(parent.children[index + 1], successor)

        # If both the left and right children don't have enough keys to borrow from
        else:
            # Merge the child at the given index with its right sibling
            self._merge(parent, index)

            # And delete the key from the merged child
            self._delete(parent.children[index], key)

    def _getPredecessor(self, parent):
        # Traverse the tree until the rightmost leaf is reached
        while not parent.leaf:
            # Get the rightmost child of the current parent
            parent = parent.children[-1]

        # Return the rightmost key of the rightmost leaf
        return parent.keys[-1]

    def _getSuccessor(self, parent):
        # Traverse the tree until the leftmost leaf is reached
        while not parent.leaf:
            # Get the leftmost child of the current parent
            parent = parent.children[0]

        # Return the leftmost key of the leftmost leaf
        return parent.keys[0]

    def _borrowFromPrevious(self, parent, index):
        # Get the parent's child node at the given index
        child = parent.children[index]
        # Get child's left sibiling node - or a previous sibling
        sibling = parent.children[index - 1]

        # Move the key from the parent to the child
        child.keys.insert(0, parent.keys[index - 1])

        # Move the key from the left sibling to the parent
        parent.keys[index - 1] = sibling.keys.pop()

        if not child.leaf:
            # Check if the child not is not a leaf
            # If so, move a child from the left sibling to the child
            child.children.insert(0, sibling.children.pop())

    def _borrowFromNext(self, parent, index):
        # Get the parent's child node at the given index
        child = parent.children[index]
        # Get child's right sibiling node - or a next sibling
        sibling = parent.children[index + 1]

        # Move the key from the parent to the child
        child.keys.append(parent.keys[index])

        # Move the key from the sibiling to the parent
        parent.keys[index] = sibling.keys.pop(0)

        if not child.leaf:
            # Check if the child not is not a leaf
            # If so, move a child from the right sibling to the child
            child.children.append(sibling.children.pop(0))

    def _merge(self, parent, index):
        # Get the child node at index i
        child = parent.children[index]
        # Get the sibling node next to the child node
        sibling = parent.children[index + 1]

        # Append the key from the current node to the child node
        child.keys.append(parent.keys[index])
        # Extend the keys of the child node with the keys of the sibling node
        child.keys.extend(sibling.keys)

        # If the child node is not a leaf node
        if not child.leaf:
            # Extend the children of the child node with the children of the sibling node
            child.children.extend(sibling.children)

        # Remove the key from the current node at index i
        parent.keys.pop(index)
        # Remove the child node at index i+1 from the current node
        parent.children.pop(index + 1)

    def getList(self, node=None):
        # If no node is provided, set the node to the root
        node = node or self.root
        # Initialize an empty list to store the keys
        keys = []

        # Run through all the children of the current node
        for child in node.children:
            # Recursively add the keys of the children to the list
            keys.extend(self.getList(child))

        # Add the keys of the current node to the list
        keys.extend(node.keys)
        # And return the final list
        return keys


def addBTreeNode(data):
    # Add the given data to the B-Tree
    bTreeElements.insert(data)

    # Insert it into the local list
    bTreeElementsList.append(data)

    # And update the B-Tree elements container to reflect the changes
    updateBTreeElementsContainer()


def deleteBTreeNode(data):
    # Check if the given data is in the B-Tree
    if data not in bTreeElementsList:
        # If its not, show an error message
        AlertPopup(f"{data} is NOT in the B-Tree")
        # And exit out of the function
        return

    # Delete the given data from the B-Tree
    bTreeElements.delete(data)

    # Remove it from the local list
    bTreeElementsList.remove(data)

    # And update the B-Tree elements container to reflect the changes
    updateBTreeElementsContainer()


def searchBTreeNode(data):
    # Search for a given data in the B-Tree
    isFound = bTreeElements.search(data)

    # And show the appropriate popup message
    AlertPopup(f"{data} is in the B-Tree") if isFound else AlertPopup(
        f"{data} is NOT in the B-Tree"
    )


def updateBTreeElementsContainer():
    # For each UI element in the B-Tree elements container
    for widget in bTreeElementsContainer.winfo_children():
        # Delete it
        widget.destroy()

    # Run through each node in the B-Tree
    for node in bTreeElementsList:
        # Append it to the container
        CTkLabel(bTreeElementsContainer, text=node).pack(padx=5, anchor="w")


def saveBTreeOnExit():
    # Check if our list is empty
    if len(bTreeElementsList) == 0:
        # If so, we cannot save anything to the file
        return

    # Otherwise, open a local file in write mode
    with open("bTree.json", "w") as file:
        # And write the list into it
        json.dump(bTreeElementsList, file)


def loadBTreeOnStart():
    try:
        # Open the local file in read mode
        with open("bTree.json", "r") as file:
            # Load the contents of the file into temporaray list
            res = json.load(file)

            # Run through each element in the list
            for element in res:
                # And add it to the B-Tree
                addBTreeNode(element)
    except:
        # If we fail to load the file, show an error message
        AlertPopup("Failed to load B-Tree elements")


addBTreeNodeHeading = CTkLabel(
    subtabBTree, text="Add B-Tree Node", font=("Arial", 14, "bold")
)
addBTreeNodeHeading.place(x=0, y=0)

addBTreeNodeInput = CTkEntry(subtabBTree, placeholder_text="Node...", width=300)
addBTreeNodeInput.place(x=0, y=30)

addBTreeNodeButton = CTkButton(
    subtabBTree,
    text="Add",
    command=lambda: addBTreeNode(addBTreeNodeInput.get())
    if addBTreeNodeInput.get()
    else AlertPopup("Please enter a value to add"),
    width=45,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
)
addBTreeNodeButton.place(x=305, y=30)

deleteBTreeNodeHeading = CTkLabel(
    subtabBTree, text="Delete B-Tree Node", font=("Arial", 14, "bold")
)
deleteBTreeNodeHeading.place(x=0, y=70)

deleteBTreeNodeInput = CTkEntry(subtabBTree, placeholder_text="Node...", width=300)
deleteBTreeNodeInput.place(x=0, y=100)

deleteBTreeNodeButton = CTkButton(
    subtabBTree,
    text="Delete",
    command=lambda: deleteBTreeNode(deleteBTreeNodeInput.get())
    if deleteBTreeNodeInput.get()
    else AlertPopup("Please enter a value to delete"),
    width=45,
    fg_color="#D32F2F",
    hover_color="#B71C1C",
    text_color="white",
    font=("Arial", 12, "bold"),
)
deleteBTreeNodeButton.place(x=305, y=100)

searchBTreeNodeHeading = CTkLabel(
    subtabBTree, text="Search B-Tree Node", font=("Arial", 14, "bold")
)
searchBTreeNodeHeading.place(x=0, y=140)

searchBTreeNodeInput = CTkEntry(subtabBTree, placeholder_text="Node...", width=300)
searchBTreeNodeInput.place(x=0, y=170)

searchBTreeNodeButton = CTkButton(
    subtabBTree,
    text="Search",
    command=lambda: searchBTreeNode(searchBTreeNodeInput.get())
    if searchBTreeNodeInput.get()
    else AlertPopup("Please enter a value to search"),
    width=45,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
)
searchBTreeNodeButton.place(x=305, y=170)

bTreeElementsList = []
bTreeElements = BTree()
loadBTreeOnStart()


#! B-TREE TASK
def updateBTreeTaskElementsContainer():
    # For each UI element in the elements container
    for widget in bTreeTaskElementsContainer.winfo_children():
        # Delete it
        widget.destroy()

    # Run through each subscriber in the list
    for subscriber in subscribersTaskElementsList:
        # Add it to the elements container
        CTkLabel(
            bTreeTaskElementsContainer,
            text=f"+{subscriber['phone']} - {subscriber['name']}",
        ).pack(padx=5, anchor="w")


def bTreeTaskSearchForSub(data):
    def retrieveSubscribersData(phoneNumber):
        # Run through all the subscribers in the list
        for currentSubscriber in subscribersTaskElementsList:
            # Check if current subscriber has the same phone number
            if currentSubscriber["phone"] == phoneNumber:
                # Return the data of the current subscriber
                return currentSubscriber

        # If we haven't found the subscriber, return None
        return None

    # Check if the data is found in the employeesTaskElements tree
    if not subscribersTaskElementsList or len(subscribersTaskElementsList) == 0:
        # If not, show an error message
        console.log("No subscribers found in the database")
        AlertPopup("No subscribers found in the database")

    # Search for the data in the employeesTaskElements tree
    isFound = subscribersTaskElements.search(data)
    # Retrieve the subscriber data based on the data (phone number)
    subscriberData = retrieveSubscribersData(data)

    # Output the appropriate message depending on whether the data was found or not
    AlertPopup(
        f"+{data} was found in the database\nName - {subscriberData['name']}, Type - {subscriberData['type']}"
    ) if isFound else AlertPopup(f"+{data} was NOT found in the database")
    console.log(f"+{data} {'was' if isFound else 'was not'} found in the database")


def loadBTreeTaskData(fileName):
    # For loading the subscribers' data from a JSON file
    subscribersDataHolder = []
    try:
        # Open the local JSON file in read mode
        with open(fileName, "r") as file:
            # And load the data from it
            subscribersDataHolder = json.load(file)
    except:
        # If we fail to load the data, show an error message
        AlertPopup(f"Failed to load subscribers' data from {fileName}")
        console.log(f"Failed to load subscribers' data from {fileName}")

    # Run through each element in the retrieved list
    for element in subscribersDataHolder:
        # Add phone number to the B-Tree
        subscribersTaskElements.insert(element["phone"])

    # Run through each element in the retrieved list again
    for element in subscribersDataHolder:
        # To now append the subscriber's data to the list
        subscribersTaskElementsList.append(
            {
                "phone": element["phone"],
                "name": element["name"],
                "type": element["type"],
            }
        )

    # And update the elements container
    updateBTreeTaskElementsContainer()
    console.log(f"Loaded subscribers data from {fileName}")


loadBTreeTaskDataHeading = CTkLabel(
    subtabBTreeTask, text="Load subscribers JSON", font=("Arial", 14, "bold")
)
loadBTreeTaskDataHeading.place(x=0, y=0)

loadBTreeTaskDataInput = CTkEntry(
    subtabBTreeTask, placeholder_text="Filename...", width=300
)
loadBTreeTaskDataInput.place(x=0, y=30)

loadBTreeTaskDataButton = CTkButton(
    subtabBTreeTask,
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
    subtabBTreeTask, text="Search for subscriber", font=("Arial", 14, "bold")
)
bTreeTaskSearchForSubHeading.place(x=0, y=70)

bTreeTaskSearchForSubInput = CTkEntry(
    subtabBTreeTask, placeholder_text="Number...", width=300
)
bTreeTaskSearchForSubInput.place(x=0, y=100)

bTreeTaskSearchForSubButton = CTkButton(
    subtabBTreeTask,
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

subscribersTaskElementsList = []
subscribersTaskElements = BTree()


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
    subtabHashTableTask, text="Load employees MD", font=("Arial", 14, "bold")
)
hashTaskLoadDataHeading.place(x=0, y=0)

hashTaskLoadDataInput = CTkEntry(
    subtabHashTableTask, placeholder_text="Filename...", width=300
)
hashTaskLoadDataInput.place(x=0, y=30)

hashTaskLoadDataButton = CTkButton(
    subtabHashTableTask,
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
    subtabHashTableTask, text="Find position of an employee", font=("Arial", 14, "bold")
)
hashTaskSearchHeading.place(x=0, y=70)

hashTaskSearchInput = CTkEntry(
    subtabHashTableTask, placeholder_text="Employee...", width=300
)
hashTaskSearchInput.place(x=0, y=100)

hashTaskSearchButton = CTkButton(
    subtabHashTableTask,
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
            console.log("Encoded text not padded properly", log_locals=True)
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


greedyAlgosTabsContainer = CTkTabview(tabGreedyAlgorithms)
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
    fg_color="#8F00FF",
    hover_color="#7500D1",
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


dynamicProgrammingTabsContainer = CTkTabview(tabDynamicProgramming)
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
    tabGraphTraversalAlgorithms,
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


#! GRAPH SHORTEST PATHS ALGOS
class PathsGraph:
    def __init__(self, directed=False):
        self.edges = defaultdict(list)
        self.directed = directed

    def addEdge(self, u, v, weight):
        self.edges[u].append((v, weight))
        if not self.directed:
            self.edges[v].append((u, weight))

    def drawGraph(self, shortest_path=None):
        G = nx.Graph() if not self.directed else nx.DiGraph()
        for u, edges in self.edges.items():
            for v, weight in edges:
                G.add_edge(u, v, weight=weight)
        pos = nx.spring_layout(G, k=0.5)

        if shortest_path:
            nodeColors = [
                "red"
                if node == shortest_path[-1]
                else "lightgreen"
                if node == shortest_path[0]
                else "lightgray"
                for node in G.nodes()
            ]
            nx.draw_networkx_nodes(G, pos, node_color=nodeColors)

            plt.text(
                0.00,
                1.13,
                "Red: End",
                transform=plt.gca().transAxes,
                fontsize=10,
                verticalalignment="top",
                bbox=dict(boxstyle="round", facecolor="red", alpha=0.5),
            )
            plt.text(
                0.00,
                1.06,
                "Green: Start",
                transform=plt.gca().transAxes,
                fontsize=10,
                verticalalignment="top",
                bbox=dict(boxstyle="round", facecolor="lightgreen", alpha=0.5),
            )
        else:
            nx.draw_networkx_nodes(G, pos, node_color="lightblue")
        nx.draw_networkx_edges(
            G, pos, arrowstyle="->"
        ) if self.directed else nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos, font_weight="bold")

        if shortest_path:
            edges = [
                (shortest_path[i], shortest_path[i + 1])
                for i in range(len(shortest_path) - 1)
            ]
            nx.draw_networkx_edges(
                G, pos, edgelist=edges, edge_color="red", arrowstyle="->", width=2
            ) if self.directed else nx.draw_networkx_edges(
                G, pos, edgelist=edges, edge_color="red", width=2
            )

        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def floydWarshall(self):
        dist = defaultdict(lambda: defaultdict(lambda: float("inf")))
        nextNode = defaultdict(dict)

        for u in self.edges:
            dist[u][u] = 0
            for v, weight in self.edges[u]:
                dist[u][v] = weight
                nextNode[u][v] = v

        for k in self.edges:
            for i in self.edges:
                for j in self.edges:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        nextNode[i][j] = nextNode[i][k]

        return dist, nextNode

    def shortestPath(self, start, end):
        distances, nextNode = self.floydWarshall()

        if nextNode[start][end] is None:
            return None
        path = [start]
        while start != end:
            start = nextNode[start][end]
            path.append(start)
        return path

    def dijkstra(self, start, end):
        queue = [(0, start, [])]
        seen = set()

        while queue:
            (cost, node, path) = heapq.heappop(queue)

            if node not in seen:
                seen.add(node)
                path = path + [node]
                if node == end:
                    return path
                for nextNode, c in self.edges[node]:
                    if nextNode not in seen:
                        newCost = cost + c
                        heapq.heappush(queue, (newCost, nextNode, path))

        return []

    def bellmanFord(self, start, end):
        distance = {node: float("infinity") for node in self.edges}
        distance[start] = 0

        predecessor = {node: None for node in self.edges}

        for _ in range(len(self.edges) - 1):
            for node in self.edges:
                for neighbour, weight in self.edges[node]:
                    if distance[node] + weight < distance[neighbour]:
                        distance[neighbour] = distance[node] + weight
                        predecessor[neighbour] = node

        for node in self.edges:
            for neighbour, weight in self.edges[node]:
                assert (
                    distance[node] + weight >= distance[neighbour]
                ), "Graph contains a negative-weight cycle"

        path = []
        currentNode = end
        while currentNode is not None:
            path.append(currentNode)
            currentNode = predecessor[currentNode]
        path.reverse()

        return path

    def getList(self):
        list = []
        for key, value in self.edges.items():
            for node in value:
                list.append(
                    f"{key} -> {node[0]} : {node[1]}"
                ) if self.directed else list.append(f"{key} 🔗 {node[0]} : {node[1]}")
        return list


graphPathsTabsContainer = CTkTabview(
    tabGraphShortestPathsAlgorithms,
)
graphPathsTabsContainer.add("Algorithms")
graphPathsTabsContainer.add("Project Times")
graphPathsTabsContainer.add("Path between Two Points")
graphPathsTabsContainer.add("Path to All Points")
graphPathsTabsContainer.pack(expand=True, fill="both")

graphPathAlogsTab = graphPathsTabsContainer.tab("Algorithms")
graphProjectTimesTab = graphPathsTabsContainer.tab("Project Times")
graphPathFromTwoPointsTab = graphPathsTabsContainer.tab("Path between Two Points")
graphPathFromAllPointsTab = graphPathsTabsContainer.tab("Path to All Points")


def graphAlgosLoadGraph(fileName, isDirected):
    global graphAlgosGraphObject
    graphAlgosGraphObject = PathsGraph(isDirected)
    with open(fileName, "r") as file:
        for line in file:
            u, v, w = map(int, line.strip().split())
            graphAlgosGraphObject.addEdge(u, v, int(w))
    graphAlgosUpdateElementsContainer()


def graphAlgosUpdateElementsContainer():
    for widget in graphAlgosElementsContainer.winfo_children():
        widget.destroy()

    for edge in graphAlgosGraphObject.getList():
        CTkLabel(
            graphAlgosElementsContainer,
            text=edge,
        ).pack(padx=5, anchor="w")


def graphAlgosPerformDijkstra(start, end):
    shortestPath = graphAlgosGraphObject.dijkstra(start, end)
    if not shortestPath:
        AlertPopup(f"No Path from {start} to {end} Found")
    else:
        graphAlgosGraphObject.drawGraph(shortestPath)


def graphAlgosPerformBellmanFord(start, end):
    shortestPath = graphAlgosGraphObject.bellmanFord(start, end)
    if not shortestPath:
        AlertPopup(f"No Path from {start} to {end} Found")
    else:
        graphAlgosGraphObject.drawGraph(shortestPath)


def graphAlgosPerformFordWarshall(start, end):
    shortestPath = graphAlgosGraphObject.shortestPath(start, end)
    if not shortestPath:
        AlertPopup(f"No Path from {start} to {end} Found")
    else:
        graphAlgosGraphObject.drawGraph(shortestPath)


graphAlgosElementsContainer = CTkScrollableFrame(
    graphPathAlogsTab, width=240, height=240
)
graphAlgosElementsContainer.place(x=400, y=0)


graphAlgosDrawGraphButton = CTkButton(
    graphPathAlogsTab,
    text="Draw Graph",
    width=260,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: graphAlgosGraphObject.drawGraph()
    if graphAlgosGraphObject
    else AlertPopup("Please Load Graph First"),
)
graphAlgosDrawGraphButton.place(x=400, y=260)

graphAlgosLoadGraphHeading = CTkLabel(
    graphPathAlogsTab, text="Load Graph from File", font=("Arial", 14, "bold")
)
graphAlgosLoadGraphHeading.place(x=0, y=0)

graphAlgosIsDirected = CTkCheckBox(
    graphPathAlogsTab,
    text="Is Directed?",
    onvalue=True,
    offvalue=False,
)
graphAlgosIsDirected.place(x=0, y=30)

graphAlgosLoadGraphInput = CTkEntry(
    graphPathAlogsTab, width=180, placeholder_text="Graph File Path..."
)
graphAlgosLoadGraphInput.place(x=120, y=30)

graphAlgosLoadGraphButton = CTkButton(
    graphPathAlogsTab,
    text="Load",
    width=60,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: graphAlgosLoadGraph(
        graphAlgosLoadGraphInput.get(), graphAlgosIsDirected.get()
    )
    if graphAlgosLoadGraphInput.get()
    else AlertPopup("Please Enter Graph File Path"),
)
graphAlgosLoadGraphButton.place(x=305, y=30)

graphAlgosPerformDijkstraHeading = CTkLabel(
    graphPathAlogsTab, text="Perform Dijkstra", font=("Arial", 14, "bold")
)
graphAlgosPerformDijkstraHeading.place(x=0, y=70)

graphAlgosPerformDijkstraStart = CTkEntry(
    graphPathAlogsTab, width=145, placeholder_text="Start Point"
)
graphAlgosPerformDijkstraStart.place(x=0, y=100)

graphAlgosPerformDijkstraEnd = CTkEntry(
    graphPathAlogsTab, width=145, placeholder_text="End Point"
)
graphAlgosPerformDijkstraEnd.place(x=150, y=100)

graphAlgosPerformDijkstraButton = CTkButton(
    graphPathAlogsTab,
    text="Run",
    width=60,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: graphAlgosPerformDijkstra(
        int(graphAlgosPerformDijkstraStart.get()),
        int(graphAlgosPerformDijkstraEnd.get()),
    )
    if graphAlgosPerformDijkstraStart.get() and graphAlgosPerformDijkstraEnd.get()
    else AlertPopup("Please Enter Start and End Points"),
)
graphAlgosPerformDijkstraButton.place(x=305, y=100)

graphAlgosPerformBellmanFordHeading = CTkLabel(
    graphPathAlogsTab, text="Perform Bellman Ford", font=("Arial", 14, "bold")
)
graphAlgosPerformBellmanFordHeading.place(x=0, y=140)

graphAlgosPerformBellmanFordStart = CTkEntry(
    graphPathAlogsTab, width=145, placeholder_text="Start Point"
)
graphAlgosPerformBellmanFordStart.place(x=0, y=170)

graphAlgosPerformBellmanFordEnd = CTkEntry(
    graphPathAlogsTab, width=145, placeholder_text="End Point"
)
graphAlgosPerformBellmanFordEnd.place(x=150, y=170)

graphAlgosPerformBellmanFordButton = CTkButton(
    graphPathAlogsTab,
    text="Run",
    width=60,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: graphAlgosPerformBellmanFord(
        int(graphAlgosPerformBellmanFordStart.get()),
        int(graphAlgosPerformBellmanFordEnd.get()),
    )
    if graphAlgosPerformBellmanFordStart.get() and graphAlgosPerformBellmanFordEnd.get()
    else AlertPopup("Please Enter Start and End Points"),
)
graphAlgosPerformBellmanFordButton.place(x=305, y=170)

graphAlgosPerformFordWarshallHeading = CTkLabel(
    graphPathAlogsTab, text="Perform Ford Warshall", font=("Arial", 14, "bold")
)
graphAlgosPerformFordWarshallHeading.place(x=0, y=210)

graphAlgosPerformFordWarshallStart = CTkEntry(
    graphPathAlogsTab, width=145, placeholder_text="Start Point"
)
graphAlgosPerformFordWarshallStart.place(x=0, y=240)

graphAlgosPerformFordWarshallEnd = CTkEntry(
    graphPathAlogsTab, width=145, placeholder_text="End Point"
)
graphAlgosPerformFordWarshallEnd.place(x=150, y=240)

graphAlgosPerformFordWarshallButton = CTkButton(
    graphPathAlogsTab,
    text="Run",
    width=60,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: graphAlgosPerformFordWarshall(
        int(graphAlgosPerformFordWarshallStart.get()),
        int(graphAlgosPerformFordWarshallEnd.get()),
    )
    if graphAlgosPerformFordWarshallStart.get()
    and graphAlgosPerformFordWarshallEnd.get()
    else AlertPopup("Please Enter Start and End Points"),
)
graphAlgosPerformFordWarshallButton.place(x=305, y=240)

graphAlgosGraphObject = None


#! PROJECT MINIMAL TIMES
class TasksGraph:
    def __init__(self, directed=False):
        self.edges = defaultdict(list)
        self.directed = directed

    def addEdge(self, u, v, weight):
        self.edges[u].append((v, weight))
        if not self.directed:
            self.edges[v].append((u, weight))

    def drawGraph(self, tasks=None):
        G = nx.Graph()
        for u, edges in self.edges.items():
            for v, weight in edges:
                G.add_edge(u, v, weight=weight)
        pos = nx.spring_layout(G, k=0.15)

        if tasks:
            nodeColors = [
                "red"
                if node == tasks[-1]
                else "lightgreen"
                if node == tasks[0]
                else "lightgray"
                for node in G.nodes()
            ]
            nx.draw_networkx_nodes(G, pos, node_color=nodeColors)

            plt.text(
                0.00,
                1.13,
                "Red: Last Task",
                transform=plt.gca().transAxes,
                fontsize=10,
                verticalalignment="top",
                bbox=dict(boxstyle="round", facecolor="red", alpha=0.5),
            )
            plt.text(
                0.00,
                1.06,
                "Green: First Task",
                transform=plt.gca().transAxes,
                fontsize=10,
                verticalalignment="top",
                bbox=dict(boxstyle="round", facecolor="lightgreen", alpha=0.5),
            )
        else:
            nx.draw_networkx_nodes(G, pos, node_color="lightblue")
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos, font_weight="bold")
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def calculateMinimumTime(self):
        totalTime = 0
        for edges in self.edges.values():
            for edge in edges:
                totalTime += edge[1]
        return totalTime

    def getList(self):
        list = []

        for task, subtasks in self.edges.items():
            for subtask in subtasks:
                list.append(f"{task} -> {subtask[0]} : {subtask[1]}")

        return list


def minimalTaskTimesUpdateElementsContainer():
    for widget in minimalTaskTimesElementsContainer.winfo_children():
        widget.destroy()

    for task in minimalTaskTimesGraphObject.getList():
        CTkLabel(
            minimalTaskTimesElementsContainer,
            text=task,
        ).pack(padx=5, anchor="w")


def minimalTaskTimesLoadGraph(fileName, isDirected):
    global minimalTaskTimesGraphObject
    minimalTaskTimesGraphObject = TasksGraph(isDirected)
    with open(fileName, "r") as file:
        for line in file:
            try:
                u, v, w = line.strip().split()
                minimalTaskTimesGraphObject.addEdge(int(u), int(v), int(w))
            except ValueError:
                console.log(f"Skipping line {line}", log_locals=True)
    minimalTaskTimesUpdateElementsContainer()


def minimalTaskTimesGetResults():
    res = minimalTaskTimesGraphObject.calculateMinimumTime()
    if res:
        AlertPopup(f"Minimal Time to Complete Tasks: {res}")
    else:
        AlertPopup("Failed to Calculate Minimal Time")


minimalTaskTimesElementsContainer = CTkScrollableFrame(
    graphProjectTimesTab, width=240, height=240
)
minimalTaskTimesElementsContainer.place(x=400, y=0)

minimalTaskTimesDrawGraphButton = CTkButton(
    graphProjectTimesTab,
    text="Draw Graph",
    width=260,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: minimalTaskTimesGraphObject.drawGraph([1, 0])
    if minimalTaskTimesGraphObject
    else AlertPopup("Please Load Graph First"),
)
minimalTaskTimesDrawGraphButton.place(x=400, y=260)

minimalTaskTimesLoadGraphHeading = CTkLabel(
    graphProjectTimesTab, text="Load Graph", font=("Arial", 14, "bold")
)
minimalTaskTimesLoadGraphHeading.place(x=0, y=0)

minimalTaskTimesIsDirected = CTkCheckBox(
    graphProjectTimesTab,
    text="Is Directed?",
    onvalue=True,
    offvalue=False,
)
minimalTaskTimesIsDirected.place(x=0, y=30)

minimalTaskTimesLoadGraphInput = CTkEntry(
    graphProjectTimesTab,
    width=180,
    placeholder_text="Graph File Path...",
)
minimalTaskTimesLoadGraphInput.place(x=120, y=30)

minimalTaskTimesLoadGraphButton = CTkButton(
    graphProjectTimesTab,
    text="Load",
    width=60,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: minimalTaskTimesLoadGraph(
        minimalTaskTimesLoadGraphInput.get(), minimalTaskTimesIsDirected.get()
    )
    if minimalTaskTimesLoadGraphInput.get()
    else AlertPopup("Please Enter Graph File Path"),
)
minimalTaskTimesLoadGraphButton.place(x=305, y=30)

minimalTaskTimesGetResultsButton = CTkButton(
    graphProjectTimesTab,
    text="Get Results",
    width=120,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: minimalTaskTimesGetResults()
    if minimalTaskTimesGraphObject
    else AlertPopup("Please Load Graph First"),
)
minimalTaskTimesGetResultsButton.place(x=0, y=70)

minimalTaskTimesGraphObject = None


#! SHORTEST PATH FROM TWO POINTS
def shortestPathFromTwoPointsLoadGraph(fileName, isDirected):
    global shortestPathFromTwoPointsGraphObject
    shortestPathFromTwoPointsGraphObject = PathsGraph(isDirected)
    with open(fileName, "r") as file:
        for line in file:
            try:
                u, v, w = line.strip().split()
                shortestPathFromTwoPointsGraphObject.addEdge(int(u), int(v), int(w))
            except ValueError:
                console.log(f"Skipping line {line}", log_locals=True)
    shortestPathFromTwoPointsUpdateElementsContainer()


def shortestPathFromTwoPointsUpdateElementsContainer():
    for widget in shortestPathFromTwoPointsElementsContainer.winfo_children():
        widget.destroy()

    for task in shortestPathFromTwoPointsGraphObject.getList():
        CTkLabel(
            shortestPathFromTwoPointsElementsContainer,
            text=task,
        ).pack(padx=5, anchor="w")


def shortestPathFromTwoPoints(start, end):
    shortestPath = shortestPathFromTwoPointsGraphObject.dijkstra(start, end)
    if not shortestPath:
        AlertPopup(f"No Path from {start} to {end} Found")
    else:
        shortestPathFromTwoPointsGraphObject.drawGraph(shortestPath)


shortestPathFromTwoPointsElementsContainer = CTkScrollableFrame(
    graphPathFromTwoPointsTab, width=240, height=240
)
shortestPathFromTwoPointsElementsContainer.place(x=400, y=0)

shortestPathFromTwoPointsDrawGraphButton = CTkButton(
    graphPathFromTwoPointsTab,
    text="Draw Graph",
    width=260,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: shortestPathFromTwoPointsGraphObject.drawGraph()
    if shortestPathFromTwoPointsGraphObject
    else AlertPopup("Please Load Graph First"),
)
shortestPathFromTwoPointsDrawGraphButton.place(x=400, y=260)

shortestPathFromTwoPointsLoadGraphHeading = CTkLabel(
    graphPathFromTwoPointsTab, text="Load Graph", font=("Arial", 14, "bold")
)
shortestPathFromTwoPointsLoadGraphHeading.place(x=0, y=0)

shortestPathFromTwoPointsIsDirected = CTkCheckBox(
    graphPathFromTwoPointsTab,
    text="Is Directed?",
    onvalue=True,
    offvalue=False,
)
shortestPathFromTwoPointsIsDirected.place(x=0, y=30)

shortestPathFromTwoPointsLoadGraphInput = CTkEntry(
    graphPathFromTwoPointsTab,
    width=180,
    placeholder_text="Graph File Path...",
)
shortestPathFromTwoPointsLoadGraphInput.place(x=120, y=30)

shortestPathFromTwoPointsLoadGraphButton = CTkButton(
    graphPathFromTwoPointsTab,
    text="Load",
    width=60,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: shortestPathFromTwoPointsLoadGraph(
        shortestPathFromTwoPointsLoadGraphInput.get(),
        shortestPathFromTwoPointsIsDirected.get(),
    )
    if shortestPathFromTwoPointsLoadGraphInput.get()
    else AlertPopup("Please Enter Graph File Path"),
)
shortestPathFromTwoPointsLoadGraphButton.place(x=305, y=30)

shortestPathFromTwoPointsGetStartHeading = CTkLabel(
    graphPathFromTwoPointsTab, text="Enter Starting Node", font=("Arial", 14, "bold")
)
shortestPathFromTwoPointsGetStartHeading.place(x=0, y=70)

shortestPathFromTwoPointsGetStartInput = CTkEntry(
    graphPathFromTwoPointsTab,
    width=300,
    placeholder_text="Start Point...",
)
shortestPathFromTwoPointsGetStartInput.place(x=0, y=100)

shortestPathFromTwoPointsGetEndHeading = CTkLabel(
    graphPathFromTwoPointsTab, text="Enter Ending Node", font=("Arial", 14, "bold")
)
shortestPathFromTwoPointsGetEndHeading.place(x=0, y=140)

shortestPathFromTwoPointsGetEndInput = CTkEntry(
    graphPathFromTwoPointsTab,
    width=300,
    placeholder_text="End Point...",
)
shortestPathFromTwoPointsGetEndInput.place(x=0, y=170)

shortestPathFromTwoPointsPerformButton = CTkButton(
    graphPathFromTwoPointsTab,
    text="Get Results",
    width=120,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: shortestPathFromTwoPoints(
        int(shortestPathFromTwoPointsGetStartInput.get()),
        int(shortestPathFromTwoPointsGetEndInput.get()),
    )
    if shortestPathFromTwoPointsGetStartInput.get()
    and shortestPathFromTwoPointsGetEndInput.get()
    else AlertPopup("Please Enter Start and End Points"),
)
shortestPathFromTwoPointsPerformButton.place(x=0, y=210)

shortestPathFromTwoPointsGraphObject = None


#! SHORTEST PATHS TO ALL NODES
def shortestPathToAllLoadGraph(fileName, isDirected):
    global shortestPathToAllGraphObject
    shortestPathToAllGraphObject = PathsGraph(isDirected)
    with open(fileName, "r") as file:
        for line in file:
            try:
                u, v, w = line.strip().split()
                shortestPathToAllGraphObject.addEdge(int(u), int(v), int(w))
            except ValueError:
                console.log(f"Skipping line {line}", log_locals=True)
    shortestPathToAllUpdateElementsContainer()


def shortestPathToAllUpdateElementsContainer():
    for widget in shortestPathToAllElementsContainer.winfo_children():
        widget.destroy()

    for element in shortestPathToAllGraphObject.getList():
        CTkLabel(shortestPathToAllElementsContainer, text=element).pack(
            padx=5, anchor="w"
        )


def shortestPathToAll(start):
    for currentNode in shortestPathToAllGraphObject.edges:
        if currentNode != start:
            currentPath = shortestPathToAllGraphObject.shortestPath(start, currentNode)
            if currentPath:
                shortestPathToAllGraphObject.drawGraph(currentPath)
            else:
                shortestPathToAllGraphObject.drawGraph([start, currentNode])


shortestPathToAllElementsContainer = CTkScrollableFrame(
    graphPathFromAllPointsTab,
    width=240,
    height=240,
)
shortestPathToAllElementsContainer.place(x=400, y=0)

shortestPathToAllDrawGraphButton = CTkButton(
    graphPathFromAllPointsTab,
    text="Draw Graph",
    width=260,
    fg_color="#28A228",
    hover_color="#1F7D1F",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: shortestPathToAllGraphObject.drawGraph()
    if shortestPathToAllGraphObject
    else AlertPopup("Please Load Graph First"),
)
shortestPathToAllDrawGraphButton.place(x=400, y=260)

shortestPathToAllLoadGraphHeading = CTkLabel(
    graphPathFromAllPointsTab, text="Load Graph", font=("Arial", 14, "bold")
)
shortestPathToAllLoadGraphHeading.place(x=0, y=0)

shortestPathToAllIsDirected = CTkCheckBox(
    graphPathFromAllPointsTab,
    text="Is Directed?",
    onvalue=True,
    offvalue=False,
)
shortestPathToAllIsDirected.place(x=0, y=30)

shortestPathToAllLoadGraphInput = CTkEntry(
    graphPathFromAllPointsTab,
    width=180,
    placeholder_text="Graph File Path...",
)
shortestPathToAllLoadGraphInput.place(x=120, y=30)

shortestPathToAllLoadGraphButton = CTkButton(
    graphPathFromAllPointsTab,
    text="Load",
    width=60,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: shortestPathToAllLoadGraph(
        shortestPathToAllLoadGraphInput.get(),
        shortestPathToAllIsDirected.get(),
    )
    if shortestPathToAllLoadGraphInput.get()
    else AlertPopup("Please Enter Graph File Path"),
)
shortestPathToAllLoadGraphButton.place(x=305, y=30)

shortestPathToAllGetStartHeading = CTkLabel(
    graphPathFromAllPointsTab, text="Enter Starting Node", font=("Arial", 14, "bold")
)
shortestPathToAllGetStartHeading.place(x=0, y=70)

shortestPathToAllGetStartInput = CTkEntry(
    graphPathFromAllPointsTab,
    width=300,
    placeholder_text="Start Point...",
)
shortestPathToAllGetStartInput.place(x=0, y=100)

shortestPathToAllPerformButton = CTkButton(
    graphPathFromAllPointsTab,
    text="Get Results",
    width=120,
    fg_color="#1976D2",
    hover_color="#0D47A1",
    text_color="white",
    font=("Arial", 12, "bold"),
    command=lambda: shortestPathToAll(
        int(shortestPathToAllGetStartInput.get()),
    )
    if shortestPathToAllGetStartInput.get()
    else AlertPopup("Please Enter Start Point"),
)
shortestPathToAllPerformButton.place(x=0, y=140)

shortestPathToAllGraphObject = None

app.mainloop()
saveHeapOnExit()
saveLinkedListOnExit()
saveHashTableOnExit()
saveBTreeOnExit()
