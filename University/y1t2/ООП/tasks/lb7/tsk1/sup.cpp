#include "sup.h"
#include "D:\repos\university\lib.h"

// Створити клас Delta таким чином, щоб кожний об’єкт вміщував свій персональний номер (дескриптор об’єкта) та функцію, яка повертає його значення. Дескриптор об’єкта – унікальне для об’єктів даного типу ціле число.
// Виконати завдання з лабораторної роботи №1, де тип елементу заданої структури даних довільний. Використати шаблонні функції.

template <typename T = int>
class Delta
{
private:
    ll descriptor;
    T value;

public:
    Delta() : value(), descriptor(nextDescriptor()) {}
    Delta(T inValue) : value(inValue), descriptor(nextDescriptor()) {}
    static ll nextDescriptor()
    {
        static ll nextDescriptor = 0;
        return nextDescriptor++;
    }
    T getValue() const { return value; }
    ll getDescriptor() const { return descriptor; }
    void setValue(T inValue) { value = inValue; }
    ~Delta() {}
};

template <typename T>
void createObjects(vector<unique_ptr<Delta<T>>> &container)
{
    ll initSize = container.size();

    cout << "Enter number of objects to create: ";
    ll objectsAmount = getNum();

    if (objectsAmount < 1)
    {
        bad("Invalid amount of objects");
        return;
    }

    cout << "\nAdding objects (" << objectsAmount << "):\n";
    for (ll i = 0; i < objectsAmount; i++)
    {
        cin.ignore();
        T value;
        cout << i + 1 << ". Enter value for object: ";
        cin >> value;
        container.eb(make_unique<Delta<T>>(value));
    }

    if (container.size() == initSize + objectsAmount)
        good("Objects successfully added");
    else
        bad("Failed to add objects");

    cout << endl;
    printObjects(container);
}

template <typename T>
void printObjects(vector<unique_ptr<Delta<T>>> &container)
{
    ll vectorSize = container.size();
    if (vectorSize == 0)
    {
        bad("No objects to print");
        return;
    }

    cout << BOLD << "\nYour objects (" << vectorSize << "): \n"
         << UNBOLD;
    for (ll i = 0; i < vectorSize; i++)
    {
        cout << container[i]->getDescriptor() << ". " << container[i]->getValue() << endl;
    }
}

template <typename T>
void deleteObjects(vector<unique_ptr<Delta<T>>> &container)
{
    ll initSize = container.size();

    if (initSize == 0)
    {
        bad("No objects to delete");
        return;
    }

    cout << endl;
    printObjects(container);
    cout << endl;

    cout << "Enter a number of object to delete: ";
    ll numToDelete = getNum();

    if (numToDelete >= initSize || numToDelete < 0)
    {
        bad("Invalid object number");
        return;
    }

    container.erase(container.begin() + numToDelete);
    cout << endl;

    if (container.size() == initSize - 1)
        good("Object successfully deleted");
    else
        bad("Failed to delete object");

    cout << endl;
    printObjects(container);
}

template <typename T>
void outputMenu(vector<unique_ptr<Delta<T>>> &container)
{
    char doContinue;
    do
    {
        vector<string> menuItems = {
            "Add objects",
            "Delete objects",
            "Print objects",
            "Exit"};
        ll userDecision = showMenu(menuItems);

        if (userDecision == 1)
        {
            createObjects(container);
        }
        else if (userDecision == 2)
        {
            deleteObjects(container);
        }
        else if (userDecision == 3)
            printObjects(container);

        cout << "\nWould you like to return to menu? (Y | N): ";
        cin >> doContinue;
        if (doContinue == 'y' || doContinue == 'Y')
        {
            cout << endl;
            continue;
        }
        else
            break;
    } while (doContinue == 'y' || doContinue == 'Y');
}