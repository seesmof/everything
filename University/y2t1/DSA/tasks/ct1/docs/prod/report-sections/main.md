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

lets tackle data structures section first

The section on data structures should include the following information

- a brief description of the pyramidal sorting algorithm, an individual task, features of the algorithm application for solving an individual task, a description of the software in terms of implementing this algorithm with the corresponding screen forms, results of solving the task, characteristics of the algorithm, comparison of the efficiency of using three sorting algorithms;
- a brief description of hashing and B-trees as data structures and their corresponding algorithms, an individual task, features of applying the algorithm to solve an individual task, a description of the software in terms of implementing hash tables and B-trees with the corresponding screen forms, results of solving the task, characteristics of the algorithms and comparison of data structures in terms of task efficiency.

so in terms of the info you might need for writing it:

heap sort algorithm:

```python
def sort(self):
    sortedItems = []

    for _ in range(len(self.heap)):
        sortedItems.append(self.delete())

    return sortedItems
```

and the delete method just pops the root and returns it which is the largest element since its a max heap.

the individual task that i've got for using heap sort is:

- The HR department contains information about employee illnesses, including: employee's surname, name, patronymic; department, position; age; date of start of sick leave; date of end of sick leave; disease. Display information about all diseases that employees have had, in descending order of the number of cases.

and here's how i solved it:

```python
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
    console.log("Heap Sort Task Completed")
```

say that the three sorting algorithms are listed in the heap demo section where user can define whatever heap they want, and then add, delete and search elements in it as well as sort it in 3 different ways: heap sort, quick sort and python built in sort function. they get to see the average times for each sorting algorithm as a table outputted in the console, so that is covered. not sure what screenshots they're talking about here, i'd love to hear what you have to say on this, and the results im gonna add as images. now onto the b-tree and hashing.

here are the tasks i have for hash table and a b-tree:

- Create a hash table that uses the chain method to resolve collisions and the hash multiplication function. Fill in the hash table based on the selection of information from a text file that contains the names of the company's employees and their positions. Determine the position of a given employee.
- A mobile operator must have information about subscribers to provide services. Each subscriber is characterized by a number, surname, name, patronymic, and tariff plan. Form a tree from the relevant information about subscribers, provide search for information about the subscriber by his phone number and determine the number of connections for each of the tariffs.

and here's how i solve them:

```python
def bTreeTaskSearchForSub(data):
    def retrieveSubscribersData(phoneNumber):
        for currentSubscriber in subscribersTaskElementsList:
            if currentSubscriber["phone"] == phoneNumber:
                return currentSubscriber

        return None

    if not subscribersTaskElementsList or len(subscribersTaskElementsList) == 0:
        console.log("No subscribers found in the database")
        AlertPopup("No subscribers found in the database")

    isFound = subscribersTaskElements.search(data)
    subscriberData = retrieveSubscribersData(data)

    AlertPopup(
        f"+{data} was found in the database\nName - {subscriberData['name']}, Type - {subscriberData['type']}"
    ) if isFound else AlertPopup(f"+{data} was NOT found in the database")
    console.log(f"+{data} {'was' if isFound else 'was not'} found in the database")

def subscribersTaskCountTypes():
    if not subscribersTaskElementsList or len(subscribersTaskElementsList) == 0:
        console.log("No subscribers found in the database")
        AlertPopup("No subscribers found in the database")

        return

    typesCount = {}
    for subscriber in subscribersTaskElementsList:
        if subscriber["type"] in typesCount:
            typesCount[subscriber["type"]] += 1
        else:
            typesCount[subscriber["type"]] = 1

    resultsString = "Count of occurences of each subscription type:\n"
    for type in typesCount:
        resultsString += f"{type}: {typesCount[type]}\n"

    AlertPopup(resultsString)
    console.log("Counted subscription types")
```

```python
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
        console.log(f"{givenName} was found in the hash table")
    else:
        AlertPopup(f"{givenName} is NOT found")
        console.log(f"{givenName} was NOT found in the hash table")
```

well i have no idea what they mean in the rest of the paragraph, so you'll have to figure it all out yourself. if you need any other code, just let me know. other than that, lets start with this section and go from there

---

## Стуктури даних

The section on data structures should include the following information

- a brief description of the pyramidal sorting algorithm, an individual task, features of the algorithm application for solving an individual task, a description of the software in terms of implementing this algorithm with the corresponding screen forms, results of solving the task, characteristics of the algorithm, comparison of the efficiency of using three sorting algorithms;
- a brief description of hashing and B-trees as data structures and their corresponding algorithms, an individual task, features of applying the algorithm to solve an individual task, a description of the software in terms of implementing hash tables and B-trees with the corresponding screen forms, results of solving the task, characteristics of the algorithms and comparison of data structures in terms of task efficiency.

## Удосконалені методи розробки та аналізу

The section on advanced methods of development and analysis should contain the following data:

- individual task, features of using the greedy algorithm and, in particular, the Huffman algorithm to solve the problem, a description of the software in terms of implementing this algorithm with the corresponding screen forms, results of solving the problem, characteristics of the algorithm;
- an individual task, features of using dynamic programming to solve the task, a description of the software in terms of implementing this algorithm with the corresponding screen forms, results of solving the task, characteristics of the algorithm.

## Алгоритми роботи з графами

The section on algorithms for working with graphs should include the following information

- a brief description of graph traversal algorithms, peculiarities of own application of algorithms, description of software in terms of implementation of these algorithms with the corresponding screen forms, characteristics of algorithms;
- a brief description of shortest path search algorithms, peculiarities of their own application, description of software in terms of implementing these algorithms with the corresponding screen forms, characteristics of the algorithms;
- a brief description of the Ford-Falkerson algorithm, features of its own application of algorithms, a description of the software in terms of implementing this algorithm with the corresponding screen forms, characteristics of the algorithm
