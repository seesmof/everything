import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Data Structures and Algorithms")
root.wm_iconphoto(False, tk.PhotoImage(file="./images/logo.png"))

mainContainer = ttk.Notebook(root)
mainContainer.pack(expand=1, fill="both")

heapSortFrame = ttk.Frame(mainContainer)
mainContainer.add(heapSortFrame, text="Heap Sort")
heapSortHeading = ttk.Label(heapSortFrame, text="Heap Sort", font=("Arial", 18, "bold"))
heapSortHeading.pack(pady=20)

dataStructuresFrame = ttk.Frame(mainContainer)
mainContainer.add(dataStructuresFrame, text="Data Structures")
dataStructuresHeading = ttk.Label(
    dataStructuresFrame, text="Data Structures", font=("Arial", 18, "bold")
)
dataStructuresHeading.pack(pady=20)

greedyAlgosFrame = ttk.Frame(mainContainer)
mainContainer.add(greedyAlgosFrame, text="Greedy Algorithms")
greedyAlgosHeading = ttk.Label(
    greedyAlgosFrame, text="Greedy Algorithms", font=("Arial", 18, "bold")
)
greedyAlgosHeading.pack(pady=20)

dynamicProgrammingFrame = ttk.Frame(mainContainer)
mainContainer.add(dynamicProgrammingFrame, text="Dynamic Programming")
dynamicProgrammingHeading = ttk.Label(
    dynamicProgrammingFrame, text="Dynamic Programming", font=("Arial", 18, "bold")
)
dynamicProgrammingHeading.pack(pady=20)

graphTraversalFrame = ttk.Frame(mainContainer)
mainContainer.add(graphTraversalFrame, text="Graph Traversal")
graphTraversalHeading = ttk.Label(
    graphTraversalFrame, text="Graph Traversal", font=("Arial", 18, "bold")
)
graphTraversalHeading.pack(pady=20)

graphShortestPathFrame = ttk.Frame(mainContainer)
mainContainer.add(graphShortestPathFrame, text="Graph Shortest Path")
graphShortestPathHeading = ttk.Label(
    graphShortestPathFrame, text="Graph Shortest Path", font=("Arial", 18, "bold")
)
graphShortestPathHeading.pack(pady=20)

root.mainloop()
