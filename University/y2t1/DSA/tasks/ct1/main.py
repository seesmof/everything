import tkinter as tk
from tkinter import ttk

# Root Window
root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Data Structures and Algorithms")
root.wm_iconphoto(False, tk.PhotoImage(file="./images/logo.png"))

# Main Container
mainContainer = ttk.Notebook(root)
mainContainer.pack(expand=1, fill="both")

# ! Heap Sort Frame
heapSortFrame = ttk.Frame(mainContainer)
mainContainer.add(heapSortFrame, text="Heap Sort")
heapSortHeading = ttk.Label(heapSortFrame, text="Heap Sort", font=("Arial", 18, "bold"))
heapSortHeading.pack(pady=10, padx=10, anchor="w")

someRandomHeapJustForDemo = [
    31,
    59,
    61,
    12,
    60,
    71,
    45,
    82,
    92,
    43,
    56,
    71,
    42,
    65,
    17,
    34,
    78,
]
heapElementsList = tk.Listbox(heapSortFrame)
heapElementsList.pack(padx=10, anchor="e")
for element in someRandomHeapJustForDemo:
    heapElementsList.insert(tk.END, element)

# ! Data Structures Frame
dataStructuresFrame = ttk.Frame(mainContainer)
mainContainer.add(dataStructuresFrame, text="Data Structures")
dataStructuresHeading = ttk.Label(
    dataStructuresFrame, text="Data Structures", font=("Arial", 18, "bold")
)
dataStructuresHeading.pack(pady=10, padx=10, anchor="w")

# ! Greedy Algorithms Frame
greedyAlgosFrame = ttk.Frame(mainContainer)
mainContainer.add(greedyAlgosFrame, text="Greedy Algorithms")
greedyAlgosHeading = ttk.Label(
    greedyAlgosFrame, text="Greedy Algorithms", font=("Arial", 18, "bold")
)
greedyAlgosHeading.pack(pady=10, padx=10, anchor="w")

# ! Dynamic Programming Frame
dynamicProgrammingFrame = ttk.Frame(mainContainer)
mainContainer.add(dynamicProgrammingFrame, text="Dynamic Programming")
dynamicProgrammingHeading = ttk.Label(
    dynamicProgrammingFrame, text="Dynamic Programming", font=("Arial", 18, "bold")
)
dynamicProgrammingHeading.pack(pady=10, padx=10, anchor="w")

# ! Graph Traversal Frame
graphTraversalFrame = ttk.Frame(mainContainer)
mainContainer.add(graphTraversalFrame, text="Graph Traversal")
graphTraversalHeading = ttk.Label(
    graphTraversalFrame, text="Graph Traversal", font=("Arial", 18, "bold")
)
graphTraversalHeading.pack(pady=10, padx=10, anchor="w")

# ! Graph Shortest Paths Frame
graphShortestPathFrame = ttk.Frame(mainContainer)
mainContainer.add(graphShortestPathFrame, text="Graph Shortest Path")
graphShortestPathHeading = ttk.Label(
    graphShortestPathFrame, text="Graph Shortest Path", font=("Arial", 18, "bold")
)
graphShortestPathHeading.pack(pady=10, padx=10, anchor="w")

root.mainloop()
