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

lets tackle advanced methods of development and analysis now.

The section on advanced methods of development and analysis should contain the following data:

- individual task, features of using the greedy algorithm and, in particular, the Huffman algorithm to solve the problem, a description of the software in terms of implementing this algorithm with the corresponding screen forms, results of solving the problem, characteristics of the algorithm;
- an individual task, features of using dynamic programming to solve the task, a description of the software in terms of implementing this algorithm with the corresponding screen forms, results of solving the task, characteristics of the algorithm.

so regarding the greedy algorithms, here are the individual tasks we tackled:

- A shop assistant in a small store has a habit of keeping the most popular products on hand to speed up the queue of customers. The number of such goods is determined additionally. Each customer orders an item in turn, and the seller checks to see if the item is available. If the product is not available, the seller takes it off the shelves, which takes more time. At the same time, for each such product, the seller must decide whether it should be placed among the most popular products instead of one of the existing ones. Help the salesperson make this decision as the entire customer order queue progresses, if they want to reduce the time it takes for the entire queue to leave the store. Assume that the seller knows in advance what products each customer in the queue wants to buy.
- Develop software that implements the Huffman algorithm for compressing text file data in the form of a class. The class should have methods that allow you to specify a file with data, perform data compression, determine the parameters of the compression and inverse transformation, and write the results of encoding/decoding to a file.

regarding the code, here's some on the huffman:

```python
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
```

```python
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
```

here's some on the shopkeeper:

```python
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
```

```python
def greedyTaskPlaceOrder(order):
    global greedyTaskResults
    order = order.split(",")
    startTimer = time.time()

    queueTime, productTimes = greedyTaskShop.solveProblem(order)
    time.sleep(0.1)
    timeTaken = time.time() - startTimer
    memoryTaken = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024

    productTimesString = "\nTime taken to fetch each product:"
    for product in productTimes:
        productTimesString += f"\n{product} minutes"

    AlertPopup(f"Queue time: {queueTime}\n{productTimesString}")
    console.log(f"Placed order to shopkeeper, took {timeTaken:.2f} seconds")

    greedyTaskOrders.append(order)
    greedyTaskUpdateOrdersContainer()

    resultObjects = {"time": timeTaken, "memory": memoryTaken}
    greedyTaskResults.append(resultObjects)

    def showResultsTable():
        resultsTable = Table(title="Shopkeeper Results")
        resultsTable.add_column("Iteration Number", style="white")
        resultsTable.add_column("Time - [cyan]seconds[/]")
        resultsTable.add_column("Memory - [cyan]bytes[/]")

        averageTime = sum(result["time"] for result in greedyTaskResults) / len(
            greedyTaskResults
        )
        averageMemory = sum(result["memory"] for result in greedyTaskResults) / len(
            greedyTaskResults
        )
        resultsTable.add_row(
            "[bold]Average[/]",
            f"[bold]{averageTime:.2f}[/]",
            f"[bold]{averageMemory:.2f}[/]",
        )

        for i, result in enumerate(greedyTaskResults):
            resultsTable.add_row(
                f"{i+1}",
                f"{result['time']:.2f}",
                f"{result['memory']:.2f}",
            )

        console.print(resultsTable)

    showResultsTable()
```

everything else is pretty straight forwards so lets move onto the dynamic programming. here are the individual tasks:

- During the experimental training of the robots, they were put on bicycles. The entire group of robots is sent on bicycles along a narrow bike path in the same direction with some intervals. Each robot controls the bicycle at a given speed, which changes only if the robot catches up with a slower cyclist: unable to overtake the slower cyclist, it will slow down to the speed of the cyclist in front of it. Thus, after a while, the robots will be divided into groups, each of which will move at its own constant speed. The programmer's task is to divide the robots into a certain number of groups. Determine how many ways there are to start the robots (i.e., the order in which each robot will start moving along the bike path) that will result in a given number of groups.
- On one of the streets of a town, the buildings are classified into three types: the first is ordinary residential buildings, the second is industrial buildings, and the third is city institutions (hospitals, schools, etc.). As a result, the street is schematically represented by a set of letters, each of which defines the type of building. In the process of collecting information about the city, a matrix was created - a table in which each column and row corresponds to one of the building types. Accordingly, a cell in such a table determines whether there are buildings of a given type located nearby on a given street. The matrix is symmetric. Determine how many ways there are to arrange the buildings of these types among themselves according to the given matrix for a given number of buildings on the street, that is, the number of possible sets of letters of a given length corresponding to the given matrix.
- Compare the obtained results of the tests, analyze the accuracy, correctness and adequacy of the developed software and the methods used.

here's some code on the robots:

```python
def _count_ways(self, groups, robots):
    if groups == 0 and robots == 0:
        return 1
    if groups == 0 or robots == 0:
        return 0
    if self.dp[groups][robots] != -1:
        return self.dp[groups][robots]

    ways = 0
    for i in range(1, robots + 1):
        ways += self._count_ways(groups - 1, i - 1)
    self.dp[groups][robots] = ways
    return ways
```

```python
def solveRobotsTask(robotsCount, speeds, groupsCount):
    global robotsTaskResults
    robotGroup = RobotGroup(robotsCount, speeds, groupsCount)

    startTimer = time.time()
    res = robotGroup.countWays()
    time.sleep(0.1)
    timeTaken = time.time() - startTimer

    AlertPopup(f"Number of ways to arrange {groupsCount} groups is {res}")
    console.log(f"Completed robots DP task in {timeTaken:.2f} seconds")

    resultsObject = {
        "time": timeTaken,
        "memory": sys.getsizeof(robotGroup.dp),
    }
    robotsTaskResults.append(resultsObject)

    def showResultsTable():
        resultsTable = Table(
            title="Robots DP Task Results",
        )
        resultsTable.add_column("Attempt Number", style="white")
        resultsTable.add_column("Time - [cyan]seconds[/]")
        resultsTable.add_column("Memory - [cyan]bytes[/]")

        averageTimes = []
        averageMemories = []

        for result in robotsTaskResults:
            averageTimes.append(result["time"])
            averageMemories.append(result["memory"])

        averageTime = sum(averageTimes) / len(averageTimes)
        averageMemory = sum(averageMemories) / len(averageMemories)
        resultsTable.add_row(
            "[bold]Average[/]",
            f"[bold]{averageTime:.2f}[/]",
            f"[bold]{averageMemory:.2f}[/]",
        )

        for result in robotsTaskResults:
            resultsTable.add_row(
                str(robotsTaskResults.index(result) + 1),
                f"{result['time']:.2f}",
                f"{result['memory']:.2f}",
            )
        console.print(resultsTable)

    showResultsTable()
```

and here's some on the buildings arrangements:

```python
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
```

```python
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
    global buildingsTaskResults
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

    startTimer = time.time()
    try:
        res = arrangements.solveTask(int(buildingsCount))
    except:
        AlertPopup("Woah... That is too many buildings")
        console.log(
            "Failed to solve buildings arrangement due to maximum recursion depth exceeded"
        )
        return
    time.sleep(0.1)
    timeTaken = time.time() - startTimer

    AlertPopup(f"Number of arrangements: {res}")
    console.log(f"Solved buildings arrangement in {timeTaken:.2f} seconds")

    resultObject = {"time": timeTaken, "memory": sys.getsizeof(arrangements.memo)}
    buildingsTaskResults.append(resultObject)

    def showResultsTable():
        resultsTable = Table(title="Buildings Arrangements Results")
        resultsTable.add_column("Iteration Number", style="white")
        resultsTable.add_column("Time - [cyan]seconds[/]")
        resultsTable.add_column("Memory - [cyan]bytes[/]")

        averageTimes = []
        averageMemories = []

        for result in buildingsTaskResults:
            averageTimes.append(result["time"])
            averageMemories.append(result["memory"])

        averageTime = sum(averageTimes) / len(averageTimes)
        averageMemory = sum(averageMemories) / len(averageMemories)
        resultsTable.add_row(
            "[bold]Average[/]",
            f"[bold]{averageTime:.2f}[/]",
            f"[bold]{averageMemory:.2f}[/]",
        )

        for result in buildingsTaskResults:
            resultsTable.add_row(
                f"{buildingsTaskResults.index(result) + 1}",
                f"{result['time']:.2f}",
                f"{result['memory']:.2f}",
            )

        console.print(resultsTable)

    showResultsTable()
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

The section on advanced methods of development and analysis should contain the following data:

- individual task, features of using the greedy algorithm and, in particular, the Huffman algorithm to solve the problem, a description of the software in terms of implementing this algorithm with the corresponding screen forms, results of solving the problem, characteristics of the algorithm;
- an individual task, features of using dynamic programming to solve the task, a description of the software in terms of implementing this algorithm with the corresponding screen forms, results of solving the task, characteristics of the algorithm.

## Алгоритми роботи з графами

The section on algorithms for working with graphs should include the following information

- a brief description of graph traversal algorithms, peculiarities of own application of algorithms, description of software in terms of implementation of these algorithms with the corresponding screen forms, characteristics of algorithms;
- a brief description of shortest path search algorithms, peculiarities of their own application, description of software in terms of implementing these algorithms with the corresponding screen forms, characteristics of the algorithms;
- a brief description of the Ford-Falkerson algorithm, features of its own application of algorithms, a description of the software in terms of implementing this algorithm with the corresponding screen forms, characteristics of the algorithm
