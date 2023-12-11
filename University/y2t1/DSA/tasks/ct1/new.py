from customtkinter import *

app = CTk()
app.title("Data Structures and Algorithms")
app.geometry("700x400")
app.resizable(False, False)

tabsContainer = CTkTabview(app)
tabsContainer.pack(expand=1, fill="both")

tabsContainer.add("Heap Sort")
tabsContainer.add("Data Structures")
tabsContainer.add("Greedy Algorithms")
tabsContainer.add("Dynamic Programming")
tabsContainer.add("Graph Traversal")
tabsContainer.add("Graph Shortest Path")

heapTab = tabsContainer.tab("Heap Sort")
dataStructuresTab = tabsContainer.tab("Data Structures")
greedyAlgosTab = tabsContainer.tab("Greedy Algorithms")
dynamicProgrammingTab = tabsContainer.tab("Dynamic Programming")
graphTraversalTab = tabsContainer.tab("Graph Traversal")
graphShortestPathTab = tabsContainer.tab("Graph Shortest Path")


def updateHeapElementsContainer(newLabels: [int]):
    for widget in heapElementsContainer.winfo_children():
        widget.destroy()

    for _, element in enumerate(newLabels):
        currentLabel = CTkLabel(heapElementsContainer, text=element)
        currentLabel.pack(padx=5, anchor="w")


def addHeapElement(element):
    heapElements.append(element)
    updateHeapElementsContainer(heapElements)


def deleteHeapElement(element):
    if element in heapElements:
        heapElements.remove(element)
    else:
        print(f"{element} not in heap")
    updateHeapElementsContainer(heapElements)


heapElements = []

addHeapElementHeading = CTkLabel(
    heapTab, text="Add Heap Element", font=("Arial", 14, "bold")
)
addHeapElementHeading.place(x=5, y=5)
addHeapElementInput = CTkEntry(heapTab, placeholder_text="Enter element", width=350)
addHeapElementInput.place(x=5, y=35)
addHeapElementButton = CTkButton(
    heapTab,
    text="Add",
    command=lambda: addHeapElement(int(addHeapElementInput.get())),
    width=60,
)
addHeapElementButton.place(x=360, y=35)

deleteHeapElementHeading = CTkLabel(
    heapTab, text="Delete Heap Element", font=("Arial", 14, "bold")
)
deleteHeapElementHeading.place(x=5, y=80)
deleteHeapElementInput = CTkEntry(heapTab, placeholder_text="Enter index", width=350)
deleteHeapElementInput.place(x=5, y=110)
deleteHeapElementButton = CTkButton(
    heapTab,
    text="Delete",
    command=lambda: deleteHeapElement(int(deleteHeapElementInput.get())),
    width=60,
)
deleteHeapElementButton.place(x=360, y=110)

heapElementsHeading = CTkLabel(
    heapTab, text="Heap Elements", font=("Arial", 14, "bold")
)
heapElementsHeading.place(x=440, y=5)
heapElementsContainer = CTkScrollableFrame(heapTab, width=200, height=300)
heapElementsContainer.place(x=440, y=35)

updateHeapElementsContainer(heapElements)

app.mainloop()
