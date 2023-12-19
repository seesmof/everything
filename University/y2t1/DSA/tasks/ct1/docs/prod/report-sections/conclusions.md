Introduction.

Algorithms and Data Structures (ADS) are of fundamental importance for computer science, as they are the basis for developing efficient software and solving complex problems. The current state of the art in ATDS is quite advanced, and many problems have been practically solved. However, there are still knowledge gaps in the field, especially in areas such as quantum computing and artificial intelligence-related algorithms.
Leading companies and researchers in the field are constantly working on new algorithms and data structures in an effort to improve efficiency and solve new problems. They are also engaged in teaching and research, contributing to global trends in problem solving.
This work is relevant and necessary due to the increasing complexity of tasks in various fields such as artificial intelligence, data science, and computer graphics. It is also the basis for many software and hardware projects.
The purpose of this paper is to demonstrate the application of various concepts of Atascade through a combination of demonstration examples and tasks. These include heap, linked list, hash table, B-tree, Huffman coding, greedy algorithms, dynamic programming, BFS, DFS, Dijkstra, Floyd-Warshall, and Bellman-Ford algorithms. This work can also be used in other works in the field of computer science, such as the development of new programming languages, databases, and software systems.

The main part
Data structures
Heap Sort algorithm

Heap sort is a comparison-based sorting algorithm that uses a heap structure. It works by dividing the input data into a sorted and unsorted area, and iteratively reduces the unsorted area by selecting the largest element and moving it to the sorted area. The time complexity of this algorithm is O(n log n) in all cases (best, average, and worst), which makes it quite efficient for large datasets.
For an individual task, we implemented Heap Sort in Python, visualizing the sorting process using a graphical interface. The program allowed the user to enter an array of numbers and displayed it before and after sorting. The implementation of the Heap Sort algorithm was performed using the list data structure built into Python. The results showed that the Heap Sort algorithm is able to efficiently sort the array in ascending order.
The program also allowed the user to compare the effectiveness of the Heap Sort algorithm with other sorting algorithms, such as Quick Sort and Python's built-in sort function. The results showed that the Heap Sort algorithm was generally faster than the other two algorithms, especially for large datasets.
The code snippets and results of the algorithms are shown below in the form of screenshots.

Hashing and B-trees

Hashing and B-trees are two different types of data structures that can be used to store and retrieve data. Hashing is a technique used to uniquely identify a specific object from a group of similar objects. It uses a hash function to calculate an index in an array of cells or slots from which the desired value can be found.
B-trees, on the other hand, are a type of self-balancing tree-like data structure that supports sorted data and allows you to efficiently perform insert, delete, and search operations. They are especially useful for systems with large amounts of data that require quick access.
For an individual task, we implemented a hash table and a B-tree in Python, again using a graphical interface for visualization. The software allowed the user to enter key-value pairs, and it displayed the table or tree before and after insertion. The results showed that both data structures are capable of storing and retrieving data efficiently.
As for the individual tasks, the first task involves creating a hash table that uses a chain method to resolve collisions and a hash multiplication function. The hash table is filled in based on a sample of information from a text file containing the names of the company's employees and their positions. Then the position of a particular employee is determined.
The second task involves forming a tree from the relevant information about subscribers, providing a search for information about a subscriber by his or her phone number, and determining the number of connections for each tariff.
These solutions show how these tasks can be implemented in Python. The first solution uses a hash table to store employee data and then uses the hash multiplication function to resolve collisions. The second solution uses a B-tree to store subscriber data and then uses a search function to find a subscriber by their phone number. The number of connections for each rate is determined by counting the number of occurrences of each rate in the data sets.
The code snippets related to the algorithms and the results are shown below in the form of screenshots.

Advanced development and analysis methods
Greedy algorithms

Greedy algorithms are a type of algorithmic paradigm that uses a heuristic problem-solving scheme that consists of choosing a locally optimal solution at each stage in the hope of finding a global optimum. The goal of these algorithms is to find the best solution in the most efficient way.
For the individual greedy algorithm problem, we implemented the Huffman algorithm to compress the text file data. The Huffman algorithm is a greedy algorithm used for data compression. It works by assigning variable length codes to the input characters, the length of which depends on the frequency of the corresponding characters. The most frequent character gets the smallest code, and the least frequent character gets the largest code.
The program allowed the user to input a text file and then compressed it using the Huffman algorithm. The results showed that the Huffman algorithm effectively compresses the text file.
The second task concerned a store clerk who had to decide whether to keep an item close by to speed up the customer queue. To make this decision, the seller used a greedy algorithm. The algorithm worked by comparing the time it would take to get an item that was currently out of stock (which would slow the queue) with the time it would take to get an item that was currently in stock (which would speed up the queue). The algorithm decided to keep the item in stock if it would speed up the queue.
The results showed that the greedy algorithm was able to help the seller decide which items to keep in stock to speed up the queue.
The code snippets and results of individual tasks are shown below in the form of screenshots.

Dynamic programming

Dynamic programming is a method of solving complex problems by breaking them down into simpler subtasks. It is applied to problems that have overlapping subtasks and an optimal substructure.
For an individual dynamic programming task, we implemented a solution to the problem of dividing robots into groups. The problem was solved using a dynamic programming approach, where for each possible number of robots and groups, the number of ways to divide the robots into groups was calculated.
The program allowed the user to enter the number of robots and the number of groups, and the program calculated the number of ways to divide the robots into groups. The results showed that the dynamic programming approach could effectively solve the problem.
The second problem was to locate houses on a street based on a given matrix. The problem was solved using a dynamic programming method, where for each possible number of houses and types of houses, the number of ways to place houses was calculated.
The results showed that dynamic programming methods can effectively solve the task.
The code snippets and results of individual tasks are shown below in the form of screenshots.

Algorithms for working with graphs
Graph traversal algorithms

Graph traversal algorithms are designed to visit each vertex of a graph once. The two most common types of traversals are breadth-first search (BFS) and depth-first search (DFS). These algorithms are used in many applications, including network routing, social network analysis, and many others.
In the BFS algorithm, we start with a selected node (usually the root node) and visit all of its neighboring nodes. Then, for each of these closest nodes, we visit their unvisited neighbors, and so on, until we have visited every node in the graph. The BFS algorithm uses a queue data structure to keep track of the vertices to be visited.
DFS is another graph traversal algorithm that visits every vertex in the graph. In DFS, we start at the selected vertex, then go as far as possible along each path before returning back. DFS uses a stack to remember to start searching from the next vertex when a deadlock occurs at any iteration.
For some tasks, we implemented these algorithms in Python, visualizing the process using a graphical interface. The program allowed the user to input a graph, and it displayed the graph before and after applying the BFS or DFS algorithm. The results showed that these algorithms are able to traverse the graph efficiently.
The code snippets and the results of individual tasks are shown below in the form of screenshots.

Algorithms for finding the shortest path

Shortest path algorithms are designed to find the shortest path between two vertices in a graph. The most common algorithms for this purpose are the Dijkstra algorithm, the Bellman-Ford algorithm, and the Floyd-Warshall algorithm.
The Dijkstra algorithm works by creating a tree of shortest paths from the initial vertex to all other points in the graph. The Bellman-Ford algorithm works by iteratively relaxing the edges of the graph, which gradually leads to finding the shortest path. The Floyd-Warshall algorithm works by breaking the problem into smaller subproblems, which are then solved in a bottom-up fashion.
For individual tasks, we implemented these algorithms in Python, visualizing the process using a graphical interface. The program allowed the user to input a graph, and it displayed the graph before and after applying the shortest path algorithm. The results showed that these algorithms are capable of finding the shortest path efficiently.
The code snippets and results of individual tasks are shown below in the form of screenshots.

---

## Висновки

Вивчення алгоритмів та структур даних (АтаСД) є фундаментальним аспектом інформатики, оскільки це є основою для розробки ефективного програмного забезпечення та розв'язання складних задач. Сучасний стан науки про АтаСД є досить розвиненим, і багато проблем вже практично вирішено. Однак у цій галузі все ще існують прогалини в знаннях, особливо в таких сферах, як квантові обчислення та алгоритми, пов'язані зі штучним інтелектом. Провідні компанії та дослідники в цій галузі постійно працюють над новими алгоритмами та структурами даних, намагаючись підвищити ефективність та вирішити нові проблеми. Вони також займаються викладанням та дослідженнями, роблячи свій внесок у світові тенденції вирішення проблем.

Ця робота є актуальною і необхідною через зростання складності завдань у різних галузях, таких як штучний інтелект, наука про дані та комп'ютерна графіка. Вона також є основою для багатьох програмних та апаратних проектів. Метою даної роботи є демонстрація застосування різних концепцій АтаСД через поєднання демонстраційних прикладів та задач. До них відносяться купа, зв'язаний список, хеш-таблиця, B-дерево, кодування Хаффмана, жадібні алгоритми, динамічне програмування, алгоритми BFS, DFS, Дейкстри, Флойда-Уоршалла та Беллмана-Форда. Ця робота також може бути використана в інших роботах в галузі комп'ютерних наук, таких як розробка нових мов програмування, баз даних та програмних систем.

Результати, отримані в даній роботі, показують, що реалізовані алгоритми та структури даних здатні ефективно розв'язувати поставлені задачі. Алгоритм Heap Sort зміг відсортувати масиви за зростанням, хеш-таблиця та B-дерево змогли ефективно зберігати та отримувати дані, а підходи жадібного та динамічного програмування змогли ефективно розв'язати поставлені задачі. Алгоритми обходу графа та пошуку найкоротшого шляху змогли ефективно обходити граф та знаходити найкоротший шлях у ньому.

Результати цього дослідження мають декілька потенційних застосувань. Вони можуть бути використані при розробці нових мов програмування, баз даних та програмних систем. Вони також можуть бути використані при аналізі складних проблем у різних галузях, таких як штучний інтелект, наука про дані та комп'ютерна графіка.

Економічне значення роботи полягає в тому, що вона може призвести до розробки більш ефективного програмного та апаратного забезпечення, що може призвести до економії коштів та підвищення продуктивності праці. Наукове значення роботи полягає в тому, що вона робить внесок в область інформатики, демонструючи застосування різних алгоритмів і структур даних. Соціальне значення цієї роботи полягає в тому, що вона може призвести до розробки більш ефективних і результативних рішень складних проблем.

Таким чином, дане дослідження демонструє застосування різних алгоритмів і структур даних при вирішенні складних завдань. Результати показують, що ці алгоритми та структури даних здатні ефективно розв'язувати поставлені задачі. Результати цього дослідження мають декілька потенційних застосувань і мають важливе економічне, наукове та соціальне значення.
