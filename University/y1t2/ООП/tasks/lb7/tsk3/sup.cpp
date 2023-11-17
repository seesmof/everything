#include "D:\repos\university\lib.h"
#include "sup.h"

// Виконати завдання з лабораторної роботи #1 використавши, для зберігання даних класи Standard Template Library (STL) або list або vector. Поясніть різницю в використанні цих класів.

class Delta
{
private:
    ll m_id;

public:
    Delta() : m_id(nextID()) {}
    ll nextID()
    {
        static ll id = 0;
        return id++;
    }
    ll getID() const { return m_id; }
    ~Delta() {}
};

void showObjs(vector<unique_ptr<Delta>> &container)
{
    ll objsNum = container.size();
    if (objsNum == 0)
    {
        bad("No objects to show");
        return;
    }

    cout << "Available objects (" << objsNum << "):\n";
    for (ll i = 0; i < objsNum; i++)
    {
        cout << i + 1 << ". Descriptor: " << container[i]->getID() << endl;
    }
}

void showObjs(list<unique_ptr<Delta>> &container)
{
    ll objsNum = container.size();
    if (objsNum == 0)
    {
        bad("No objects to show");
        return;
    }

    cout << "Available objects (" << objsNum << "):\n";
    ll i = 0;
    for (auto it = container.begin(); it != container.end(); it++)
    {
        cout << i + 1 << ". Descriptor: " << it->get()->getID() << endl;
        i++;
    }
}

void addObjs(vector<unique_ptr<Delta>> &container)
{
    ll initSize = container.size();

    cout << "Enter number of objects to add: ";
    ll numToAdd = getNum();
    cout << endl;

    if (numToAdd < 1)
    {
        bad("Enter a valid number of objects");
        return;
    }

    for (ll i = 0; i < numToAdd; i++)
    {
        container.push_back(make_unique<Delta>());
    }
    cout << endl;

    if (container.size() == initSize + numToAdd)
        good("Objects added successfully");
    else
        bad("Failed to add objects");

    cout << endl;
    showObjs(container);
}

void addObjs(list<unique_ptr<Delta>> &container)
{
    ll initSize = container.size();

    cout << "Enter number of objects to add: ";
    ll numToAdd = getNum();
    cout << endl;

    if (numToAdd == 0)
    {
        bad("Enter a valid number of objects");
        return;
    }

    for (ll i = 0; i < numToAdd; i++)
    {
        container.push_back(make_unique<Delta>());
    }
    cout << endl;

    if (container.size() == initSize + numToAdd)
        good("Objects added successfully");
    else
        bad("Failed to add objects");

    cout << endl;
    showObjs(container);
}

void delObjs(vector<unique_ptr<Delta>> &container)
{
    ll initSize = container.size();

    if (initSize == 0)
    {
        bad("No objects found");
        return;
    }

    cout << endl;
    showObjs(container);
    cout << endl;

    cout << "Enter object number to remove: ";
    ll numToRemove = getNum();
    numToRemove--;

    if (numToRemove < 0 || numToRemove >= initSize)
    {
        bad("Enter a valid object number");
        return;
    }

    container.erase(container.begin() + numToRemove);
    cout << endl;

    if (container.size() == initSize - 1)
        good("Object succesfully removed");
    else
        bad("Object was not removed");

    cout << endl;
    showObjs(container);
}

void delObjs(list<unique_ptr<Delta>> &container)
{
    ll initSize = container.size();

    if (initSize == 0)
    {
        bad("No objects found");
        return;
    }

    cout << endl;
    showObjs(container);
    cout << endl;

    cout << "Enter object number to remove: ";
    ll numToRemove = getNum();
    numToRemove--;

    if (numToRemove < 0 || numToRemove >= initSize)
    {
        bad("Enter a valid object number");
        return;
    }

    auto it = next(container.begin(), numToRemove);
    container.erase(it);

    if (container.size() == initSize - 1)
        good("Object succesfully removed");
    else
        bad("Object was not removed");

    cout << endl;
    showObjs(container);
}

void outputMenu(vector<unique_ptr<Delta>> &container)
{
    vector<string> menuItems = {
        "Show objects",
        "Add objects",
        "Remove objects",
        "Exit"};
    ll userDecision = showMenu(menuItems);

    if (userDecision == 1)
    {
        showObjs(container);
    }
    else if (userDecision == 2)
    {
        addObjs(container);
    }
    else if (userDecision == 3)
    {
        delObjs(container);
    }
}

void outputMenu(list<unique_ptr<Delta>> &container)
{
    vector<string> menuItems = {
        "Show objects",
        "Add objects",
        "Remove objects",
        "Exit"};
    ll userDecision = showMenu(menuItems);

    if (userDecision == 1)
    {
        showObjs(container);
    }
    else if (userDecision == 2)
    {
        addObjs(container);
    }
    else if (userDecision == 3)
    {
        delObjs(container);
    }
}
