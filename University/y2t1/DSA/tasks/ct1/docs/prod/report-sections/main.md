CONTEXT:
Final course project on Data Structures and Algorithms discipline. Consists of one program that is a combination of all the previous semester works. Sections are the following: Heap Demo, Linked List Demo, Heap Task, Hash Table Demo, B-Tree Demo, Hash Table Task, B-Tree Task, Huffman Coding Task, Greedy Algorithm Task, Robot Groups Dynamic Programming Task, Buildings Arrangements Dynamic Programming Task, BFS Demo, DFS Demo, Sum of Paths BFS Task, Min number of operations DFS Task, Hampton Maze Visualization Task, Dijkstra & Floyd-Warshall & Bellman-Ford Demo, Project Times Dijkstra Task, Path between A and B Dijkstra Task, Path to all nodes Floyd-Warshall Task. This combination is developed with GUI in Python. Now I need to write a report for this work and I need your help.

TASK:
I will give you a name of the section as well as the given description of what's to be in it. Given the section name and the description, fill in the section.

SECTION:

## Main body

The main body of the explanatory note consists of sections, subsections, paragraphs, and subparagraphs and contains the following sections:

- data structures;
- advanced methods of development and analysis;
- algorithms for working with graphs.

lets tackle algorithms for working with graphs now.

The section on algorithms for working with graphs should include the following information

- a brief description of graph traversal algorithms, peculiarities of own application of algorithms, description of software in terms of implementation of these algorithms with the corresponding screen forms, characteristics of algorithms;
- a brief description of shortest path search algorithms, peculiarities of their own application, description of software in terms of implementing these algorithms with the corresponding screen forms, characteristics of the algorithms;

here are the individual tasks given for the graph traversal algorithms:

- In a graph given by the user, each vertex is assigned an integer (can be either negative or positive). Determine the paths between pairs of vertices that result in the addition of all the numbers from each vertex to get the value specified by the user.
- Given a set of arithmetic operations (for example, add 3, multiply by 2) that can be performed on the operand. Determine the minimal set of operations that can be used to get from one given number a number b. If such a conversion cannot be performed using the set of operations specified by the user, print a corresponding message.
- Hampton Court Maze, a 60-acre maze, attracts many tourists. Before entering one of these mazes and demonstrating his skills, your friend decided to study the maze plan and asked you for help in finding his way through the maze. Model the maze using vertices corresponding to the entrance to the maze, the exit, dead ends, all points in the maze where there is a choice of paths, and connect these vertices with edges corresponding to the paths in the maze

regarding graph traversal, here's some code on that:

```python
def BFS(self, start):
    visited = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(set(self.graph[vertex]) - set(visited))

    return visited
```

```python
def bfsDemoStartBFS(sourceNode):
    if not BFSGraphObject:
        AlertPopup("Load graph edges first")
        return

    global bfsResults
    startTimer = time.time()
    visited = BFSGraphObject.BFS(sourceNode)
    time.sleep(0.1)
    timeTaken = time.time() - startTimer
    memoryTaken = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
    nodesList = ", ".join(map(str, visited))

    AlertPopup(
        f"BFS from node {sourceNode} visited {len(visited)} nodes\nFormed tree: {nodesList}"
    )
    console.log(f"Executed BFS, took {timeTaken:.2f} seconds")

    resultObject = {"time": timeTaken, "memory": memoryTaken}
    bfsResults.append(resultObject)

    def showResultsTable():
        resultsTable = Table(title="BFS Results")
        resultsTable.add_column("Iteration Number", style="white")
        resultsTable.add_column("Time - [cyan]seconds[/]")
        resultsTable.add_column("Memory - [cyan]bytes[/]")

        averageTime = sum([result["time"] for result in bfsResults]) / len(bfsResults)
        averageMemory = sum([result["memory"] for result in bfsResults]) / len(
            bfsResults
        )
        resultsTable.add_row(
            "[bold]Average[/]",
            f"[bold]{averageTime:.2f}[/]",
            f"[bold]{averageMemory:.2f}[/]",
        )

        for i, result in enumerate(bfsResults):
            resultsTable.add_row(
                f"{i+1}", f"{result['time']:.2f}", f"{result['memory']:.2f}"
            )

        console.print(resultsTable)

    showResultsTable()
```

here's some BFS:

```python
def DFS(self, source):
    visited = []
    stack = [source]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(self.graph[vertex]) - set(visited))

    return visited
```

```python
def dfsDemoStartDFS(source):
    if not DFSGraphObject:
        AlertPopup("Load Graph Edges first")

    global dfsResults
    startTimer = time.time()
    visited = DFSGraphObject.DFS(source)
    time.sleep(0.1)
    timeTaken = time.time() - startTimer
    memoryTaken = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
    nodesList = ", ".join(map(str, visited))

    AlertPopup(
        f"DFS from node {source} visited {len(visited)} nodes\nFormed tree: {nodesList}"
    )
    console.log(f"Executed DFS, took {timeTaken:.2f} seconds")

    resultObject = {"time": timeTaken, "memory": memoryTaken}
    dfsResults.append(resultObject)

    def showResultsTable():
        resultsTable = Table(title="DFS Results")
        resultsTable.add_column("Iteration Number", style="white")
        resultsTable.add_column("Time - [cyan]seconds[/]")
        resultsTable.add_column("Memory - [cyan]bytes[/]")

        averageTime = sum([result["time"] for result in dfsResults]) / len(dfsResults)
        averageMemory = sum([result["memory"] for result in dfsResults]) / len(
            dfsResults
        )
        resultsTable.add_row(
            "[bold]Average[/]",
            f"[bold]{averageTime:.2f}[/]",
            f"[bold]{averageMemory:.2f}[/]",
        )

        for i, result in enumerate(dfsResults):
            resultsTable.add_row(
                f"{i+1}",
                f"{result['time']:.2f}",
                f"{result['memory']:.2f}",
            )
        console.print(resultsTable)

    showResultsTable()
```

here's some on the first individual task about finding a path that is the given sum:

```python
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
```

```python
def sumPathsTaskGetResults(source, targetSum):
    res = sumPathsTaskGraph.findPaths(source, targetSum)
    if res:
        pathsList = ""
        for path in res:
            pathsList += f"{path}\n"
        AlertPopup(f"Paths with sum {targetSum}:\n{pathsList}")
    else:
        AlertPopup(f"No paths with sum {targetSum} found")
    console.log(
        f"Executed Sum of Paths Task. {f'Found {len(res)} valid paths' if res else 'No paths found'}"
    )
```

here's some on the second individual task about finding the minimum number of operations:

```python
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
```

```python
def minOperationsTaskSolve(a, b):
    minOperationsTaskGraphObject = MinOperationsGraph()
    res = minOperationsTaskGraphObject.solveTask(a, b, minOperationsTaskOperationsList)
    AlertPopup(
        f"Minimum number of operations to get from {a} to {b} is {len(res)}\nOperations: {', '.join(res)}"
    ) if res else AlertPopup("There is no way to get from {a} to {b}")
    console.log(
        f"Minimum number of operations calculated. {f'It took {len(res)} operations' if res else f'Path from {a} to {b} never found'}"
    )
```

and now onto the shortest paths algorithms. here are the individual tasks given:

- The list of tasks to be performed in the course of work on a project by a group of specialists and their planned duration are determined by the user. After that, the user defines the relationship between these tasks, identifying the tasks that must be completed before the start of each task. Determine the minimum period of time it will take to complete the project.
- The map shows the roadways of a certain part of the city of Zaporizhzhia. Some streets have one-way traffic, and some may experience traffic jams. Using this information and taking into account the speed limits on the streets, determine the shortest path to get from one given point in Zaporizhzhia to another at a given time.
- Determine the shortest paths between all points on the map of Zaporizhzhia using the constraints of the previous task.

now here's some code on the algorithms themselves:

```python
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
```

```python
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
```

```python
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
```

```python
def graphAlgosPerformDijkstra(start, end):
    startTimer = time.time()
    shortestPath = graphAlgosGraphObject.dijkstra(start, end)
    time.sleep(0.1)
    timeTaken = time.time() - startTimer
    memoryTaken = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024

    AlertPopup(
        f"No Path from {start} to {end} Found"
    ) if not shortestPath else graphAlgosGraphObject.drawGraph(shortestPath)
    console.log(f"Executed Dijkstra, took {timeTaken:.2f} seconds")

    resultObject = {"type": "Dijkstra", "time": timeTaken, "memory": memoryTaken}
    graphAlgosResults.append(resultObject)
    graphAlgosShowResultsTable()
```

```python
def graphAlgosPerformBellmanFord(start, end):
    startTimer = time.time()
    shortestPath = graphAlgosGraphObject.bellmanFord(start, end)
    time.sleep(0.1)
    timeTaken = time.time() - startTimer
    memoryTaken = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024

    AlertPopup(
        f"No Path from {start} to {end} Found"
    ) if not shortestPath else graphAlgosGraphObject.drawGraph(shortestPath)
    console.log(f"Executed BellmanFord, took {timeTaken:.2f} seconds")

    resultObject = {"type": "Bellman-Ford", "time": timeTaken, "memory": memoryTaken}
    graphAlgosResults.append(resultObject)
    graphAlgosShowResultsTable()
```

```python
def graphAlgosPerformFordWarshall(start, end):
    startTimer = time.time()
    shortestPath = graphAlgosGraphObject.shortestPath(start, end)
    time.sleep(0.1)
    timeTaken = time.time() - startTimer
    memoryTaken = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024

    AlertPopup(
        f"No Path from {start} to {end} Found"
    ) if not shortestPath else graphAlgosGraphObject.drawGraph(shortestPath)
    console.log(f"Executed FordWarshall, took {timeTaken:.2f} seconds")

    resultObject = {"type": "Ford-Warshall", "time": timeTaken, "memory": memoryTaken}
    graphAlgosResults.append(resultObject)
    graphAlgosShowResultsTable()
```

and now here's some on the first individual task regarding finding project minimal time to complete:

```python
def calculateMinimumTime(self):
    totalTime = 0
    for edges in self.edges.values():
        for edge in edges:
            totalTime += edge[1]
    return totalTime
```

```python
def minimalTaskTimesGetResults():
    res = minimalTaskTimesGraphObject.calculateMinimumTime()
    AlertPopup(f"Minimal Time to Complete Tasks: {res}") if res else AlertPopup(
        "Failed to Calculate Minimal Time"
    )
    console.log(
        f"Solved Project Minimal Times task. {f'Time taken was {res}' if res else 'Failed to Calculate Minimal Time'}"
    )
```

here's some on the second individual task regarding finding shortest path between two points on the map:

```python
def shortestPathFromTwoPoints(start, end):
    shortestPath = shortestPathFromTwoPointsGraphObject.dijkstra(start, end)
    AlertPopup(
        f"No Path from {start} to {end} Found"
    ) if not shortestPath else shortestPathFromTwoPointsGraphObject.drawGraph(
        shortestPath
    )
    console.log(
        f"Executed shortest path from two points algorithm. {f'No path between {start} and {end} found' if not shortestPath else ' -> '.join(shortestPath)}"
    )
```

and here's some, finally, on the third individual task regarding finding shortest paths between all points on the map:

```python
def shortestPathToAll(start):
    if len(shortestPathToAllGraphObject.edges) == 0:
        AlertPopup("Please Load Graph First")
        console.log("Failed to show all paths, no graph loaded")
        return

    for currentNode in shortestPathToAllGraphObject.edges:
        if currentNode != start:
            currentPath = shortestPathToAllGraphObject.shortestPath(start, currentNode)
            shortestPathToAllGraphObject.drawGraph(
                currentPath
            ) if currentPath else shortestPathToAllGraphObject.drawGraph(
                [start, currentNode]
            )
```

---

## Стуктури даних

### Алгоритм пірамідального сортування (Heap Sort)

Сортування купою - це алгоритм сортування на основі порівняння, який використовує структуру даних у вигляді купи. Він працює, розділяючи вхідні дані на відсортовану та невідсортовану області, та ітеративно зменшує невідсортовану область, виділяючи найбільший елемент і переміщуючи його до відсортованої області. Часова складність цього алгоритму становить O(n log n) у всіх випадках (найкращому, середньому та найгіршому), що робить його досить ефективним для великих наборів даних.

Для індивідуального завдання ми реалізували Heap Sort на Python, візуалізувавши процес сортування за допомогою графічного інтерфейсу. Програма дозволяла користувачеві вводити масив чисел, і відображала його до і після сортування. Реалізація алгоритму Heap Sort була виконана з використанням вбудованої в Python структури даних у вигляді списку. Результати показали, що алгоритм Heap Sort здатен ефективно сортувати масив за зростанням.

Програма також дозволила користувачеві порівняти ефективність алгоритму Heap Sort з іншими алгоритмами сортування, такими як Quick Sort і вбудована функція сортування Python. Результати показали, що алгоритм Heap Sort загалом був швидшим за інші два алгоритми, особливо для великих наборів даних.

Фрагменти коду та результати роботи алгоритмів наведено нижче у вигляді знімків з екрану.

### Гешування та B-дерева

Гешування та B-дерева - це два різних типи структур даних, які можна використовувати для зберігання та пошуку даних. Гешування - це техніка, яка використовується для унікальної ідентифікації конкретного об'єкта з групи схожих об'єктів. Вона використовує геш-функцію для обчислення індексу в масиві комірок або слотів, з якого можна знайти потрібне значення.

B-дерева, з іншого боку, є типом самобалансуючої деревоподібної структури даних, яка підтримує відсортовані дані і дозволяє ефективно виконувати операції вставки, видалення та пошуку. Вони особливо корисні для систем з великими обсягами даних, які потребують швидкого доступу.

Для індивідуального завдання ми реалізували геш-таблицю та B-дерево на Python, знову ж таки з використанням графічного інтерфейсу для візуалізації. Програмне забезпечення дозволяло користувачеві вводити пари ключ-значення, і воно відображало таблицю або дерево до і після вставки. Результати показали, що обидві структури даних здатні ефективно зберігати та отримувати дані.

Що стосується індивідуальних завдань, то перше завдання передбачає створення геш-таблиці, яка використовує ланцюговий метод для вирішення колізій і функцію множення гешів. Геш-таблиця заповнюється на основі вибірки інформації з текстового файлу, який містить імена співробітників компанії та їхні посади. Потім визначається посада конкретного співробітника.

Друга задача передбачає формування дерева з відповідної інформації про абонентів, забезпечення пошуку інформації про абонента за його номером телефону та визначення кількості з'єднань для кожного з тарифів.

Наведені рішення показують, як ці задачі можуть бути реалізовані мовою Python. Перше рішення використовує геш-таблицю для зберігання даних про співробітників, а потім використовує функцію множення гешів для вирішення колізій. Друге рішення використовує B-дерево для зберігання даних про абонентів, а потім використовує функцію пошуку для пошуку абонента за його номером телефону. Кількість з'єднань для кожного тарифу визначається шляхом підрахунку кількості входжень кожного тарифу в масивах даних.

Фрагменти коду, що стосуються алгоритмів, та результати роботи наведено нижче у вигляді знімків з екрану.

## Удосконалені методи розробки та аналізу

### Жадібні алгоритми

Жадібні алгоритми - це тип алгоритмічної парадигми, яка використовує евристичну схему розв'язання задач, що полягає у виборі локально оптимального рішення на кожному етапі з надією знайти глобальний оптимум. Метою цих алгоритмів є пошук найкращого рішення у найефективніший спосіб.

Для індивідуальної задачі з жадібним алгоритмом ми реалізували алгоритм Гаффмана для стиснення даних текстового файлу. Алгоритм Гаффмана - це жадібний алгоритм, який використовується для стиснення даних. Він працює шляхом присвоєння вхідним символам кодів змінної довжини, довжина яких залежить від частоти відповідних символів. Найчастіший символ отримує найменший код, а найбільш рідкісний символ - найбільший код.

Програма дозволяла користувачеві вводити текстовий файл, а потім стискала його за алгоритмом Гаффмана. Результати показали, що алгоритм Гаффмана ефективно стискає текстовий файл.

Друга задача стосувалась продавця у магазині, який повинен був вирішити, чи варто тримати товар поруч, щоб прискорити чергу покупців. Для прийняття цього рішення продавець використав жадібний алгоритм. Алгоритм працював, порівнюючи час, який знадобився б, щоб дістати товар, якого в даний момент немає в наявності (що сповільнило б чергу), з часом, який знадобився б, щоб дістати товар, який в даний момент є в наявності (що прискорило б чергу). Алгоритм вирішив тримати товар в наявності, якщо це призведе до прискорення черги.

Результати показали, що жадібний алгоритм зміг допомогти продавцю вирішити, які товари тримати в наявності, щоб прискорити чергу.

Фрагменти коду та результати виконання індивідуальних завдань наведено нижче у вигляді знімків з екрану.

### Динамічне програмування

Динамічне програмування - це метод розв'язання складних задач шляхом розбиття їх на простіші підзадачі. Він застосовується до задач, що мають ознаки підзадач, що перекриваються, та оптимальної підструктури.

Для індивідуального завдання з динамічного програмування було реалізовано розв'язання задачі розподілу роботів на групи. Задача була вирішена з використанням підходу динамічного програмування, де для кожної можливої кількості роботів і груп розраховувалася кількість способів розбиття роботів на групи.

Програма дозволяла користувачеві вводити кількість роботів і кількість груп, а програма обчислювала кількість способів розбиття роботів на групи. Результати показали, що підхід динамічного програмування здатен ефективно вирішити проблему.

Друга задача полягала в розташуванні будинків на вулиці на основі заданої матриці. Задача була розв'язана за допомогою методу динамічного програмування, де для кожної можливої кількості будинків і типів будинків було розраховано кількість способів розміщення будинків.

Результати показали, що методи динамічного програмування дозволяють ефективно розв'язувати поставлені задачі.

Фрагменти коду та результати виконання індивідуальних завдань наведено нижче у вигляді знімків з екрану.

## Алгоритми роботи з графами

### Алгоритми обходу графа

Алгоритми обходу графів призначені для відвідування кожної вершини графа один раз. Два найпоширеніші типи обходів - це пошук в ширину (BFS) та пошук в глибину (DFS). Ці алгоритми використовуються в багатьох застосунках, включаючи мережеву маршрутизацію, аналіз соціальних мереж та багато інших.

В алгоритмі BFS ми починаємо з обраної вершини (зазвичай кореневої) і відвідуємо всі сусідні з нею вершини. Потім для кожної з цих найближчих вершин ми відвідуємо їхніх невідвіданих сусідів, і так далі, поки не відвідаємо кожну вершину графа. Алгоритм BFS використовує структуру даних у вигляді черги для відстеження вершин, які потрібно відвідати.

DFS - ще один алгоритм обходу графа, який відвідує кожну вершину графа. У DFS ми починаємо з обраної вершини, потім проходимо якомога далі вздовж кожного шляху, перш ніж повернутися назад. DFS використовує стек, щоб не забути почати пошук з наступної вершини, коли на будь-якій ітерації виникає глухий кут.

Для окремих завдань ми реалізували ці алгоритми на Python, візуалізуючи процес за допомогою графічного інтерфейсу. Програма дозволяла користувачеві вводити граф, і вона відображала граф до і після застосування алгоритму BFS або DFS. Результати показали, що ці алгоритми здатні ефективно обходити граф.

Фрагменти коду та результати виконання індивідуальних завдань наведено нижче у вигляді знімків з екрану.

### Алгоритми пошуку найкоротшого шляху

Алгоритми пошуку найкоротшого шляху призначені для пошуку найкоротшого шляху між двома вершинами графа. Найпоширенішими алгоритмами для цієї мети є алгоритм Дейкстри, алгоритм Беллмана-Форда та алгоритм Флойда-Уоршалла.

Алгоритм Дейкстри працює шляхом створення дерева найкоротших шляхів від початкової вершини до всіх інших точок графа. Алгоритм Беллмана-Форда працює шляхом ітеративного розслаблення ребер графа, що поступово призводить до знаходження найкоротшого шляху. Алгоритм Флойда-Уоршалла працює шляхом розбиття задачі на менші підзадачі, які потім вирішуються за принципом "знизу вгору".

Для окремих завдань ми реалізували ці алгоритми мовою Python, візуалізуючи процес за допомогою графічного інтерфейсу. Програма дозволяла користувачеві вводити граф, і вона відображала граф до і після застосування алгоритму найкоротшого шляху. Результати показали, що ці алгоритми здатні ефективно знаходити найкоротший шлях.

Фрагменти коду та результати виконання індивідуальних завдань наведено нижче у вигляді знімків з екрану.
